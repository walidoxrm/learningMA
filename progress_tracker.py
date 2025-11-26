#!/usr/bin/env python3
"""
Simple CLI to track the learn-by-doing journey.
Data is stored locally in JSON so it can be shared/versionné.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

DATA_FILE = Path("progress.json")
TOPIC_FILE = Path("learn_path.json")

DEFAULT_TOPICS = [
    "Installation environnement",
    "Scripts Python de base",
    "Fonctions et modularisation",
    "Lecture/écriture fichiers",
    "Menus ou mini-UI",
    "Tests et debugging",
    "Git + README",
]


def timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


def sync_to_github() -> bool:
    """Synchronise progress.json sur GitHub si Git est configuré."""
    if not Path(".git").exists():
        return False
    
    try:
        # Vérifier si un remote est configuré
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            return False
        
        # Ajouter et commiter
        subprocess.run(["git", "add", "progress.json"], check=False, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "Mise à jour du suivi d'avancement"],
            check=False,
            capture_output=True
        )
        
        # Push (essayer main puis master)
        for branch in ["main", "master"]:
            result = subprocess.run(
                ["git", "push", "origin", branch],
                check=False,
                capture_output=True
            )
            if result.returncode == 0:
                return True
        
        return False
    except Exception:
        return False


def ensure_data_file() -> Dict[str, Any]:
    if not DATA_FILE.exists():
        print("Aucun projet initialisé. Lance `progress_tracker.py init --project ...`.", file=sys.stderr)
        sys.exit(1)
    return load_json(DATA_FILE)


def handle_init(args: argparse.Namespace) -> None:
    if DATA_FILE.exists() and not args.force:
        print(f"{DATA_FILE} existe déjà. Utilise --force pour réinitialiser.", file=sys.stderr)
        sys.exit(1)

    topics = [topic.strip() for topic in (args.topics or DEFAULT_TOPICS) if topic.strip()]
    data = {
        "project": args.project,
        "created_at": timestamp(),
        "sessions": [],
        "topics": [{"name": t, "done": False, "updated_at": None} for t in topics],
    }
    save_json(DATA_FILE, data)
    save_json(TOPIC_FILE, {"topics": topics, "generated_at": timestamp()})
    print(f"Projet « {args.project} » initialisé avec {len(topics)} notions.")
    
    if args.sync:
        if sync_to_github():
            print("✅ Synchronisé sur GitHub.")
        else:
            print("ℹ️  Git non configuré ou erreur de synchronisation.")


def handle_log(args: argparse.Namespace) -> None:
    data = ensure_data_file()
    sessions: List[Dict[str, Any]] = data.setdefault("sessions", [])

    entry = {
        "session": args.session,
        "focus": args.focus,
        "note": args.note or "",
        "timestamp": timestamp(),
    }
    # replace session if same id exists
    sessions = [sess for sess in sessions if sess.get("session") != args.session]
    sessions.append(entry)
    sessions.sort(key=lambda s: s["session"])
    data["sessions"] = sessions
    save_json(DATA_FILE, data)
    print(f"Séance {args.session} enregistrée.")
    
    if args.sync:
        if sync_to_github():
            print("✅ Synchronisé sur GitHub.")
        else:
            print("ℹ️  Git non configuré ou erreur de synchronisation.")


def handle_check(args: argparse.Namespace) -> None:
    data = ensure_data_file()
    topics: List[Dict[str, Any]] = data.setdefault("topics", [])

    for topic in topics:
        if topic["name"].lower() == args.topic.lower():
            topic["done"] = args.status == "done"
            topic["updated_at"] = timestamp()
            break
    else:
        topics.append(
            {"name": args.topic, "done": args.status == "done", "updated_at": timestamp()}
        )
    save_json(DATA_FILE, data)
    print(f"Sujet « {args.topic} » marqué comme {args.status}.")
    
    if args.sync:
        if sync_to_github():
            print("✅ Synchronisé sur GitHub.")
        else:
            print("ℹ️  Git non configuré ou erreur de synchronisation.")


def handle_report(_: argparse.Namespace) -> None:
    data = ensure_data_file()
    sessions = data.get("sessions", [])
    topics = data.get("topics", [])

    print(f"Projet : {data.get('project', 'Inconnu')}")
    print(f"Séances suivies : {len(sessions)}")
    for sess in sorted(sessions, key=lambda s: s["session"]):
        print(f"  #{sess['session']} - {sess['focus']} ({sess['timestamp']})")
        if sess["note"]:
            print(f"    Note : {sess['note']}")

    done = sum(1 for t in topics if t.get("done"))
    total = len(topics) or 1
    print(f"Notions maîtrisées : {done}/{total}")
    for topic in topics:
        status = "✅" if topic.get("done") else "🔜"
        print(f"  {status} {topic['name']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Suivi du parcours learn by doing.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialiser un nouveau suivi.")
    init_parser.add_argument("--project", required=True, help="Nom du projet fil rouge.")
    init_parser.add_argument(
        "--topics",
        nargs="*",
        help="Liste personnalisée de notions (sinon les notions par défaut sont utilisées).",
    )
    init_parser.add_argument(
        "--force", action="store_true", help="Réinitialiser les fichiers existants."
    )
    init_parser.add_argument(
        "--sync", action="store_true", help="Synchroniser automatiquement sur GitHub après l'opération."
    )
    init_parser.set_defaults(func=handle_init)

    log_parser = subparsers.add_parser("log", help="Ajouter ou mettre à jour une séance.")
    log_parser.add_argument("--session", type=int, required=True, help="Numéro de séance.")
    log_parser.add_argument("--focus", required=True, help="Thème principal travaillé.")
    log_parser.add_argument("--note", help="Observations ou axes d'amélioration.")
    log_parser.add_argument(
        "--sync", action="store_true", help="Synchroniser automatiquement sur GitHub après l'opération."
    )
    log_parser.set_defaults(func=handle_log)

    check_parser = subparsers.add_parser("check", help="Cocher une notion travaillée.")
    check_parser.add_argument("--topic", required=True, help="Nom de la notion.")
    check_parser.add_argument(
        "--status",
        choices=["done", "todo"],
        default="done",
        help="État de la notion (done = acquise, todo = à revoir).",
    )
    check_parser.add_argument(
        "--sync", action="store_true", help="Synchroniser automatiquement sur GitHub après l'opération."
    )
    check_parser.set_defaults(func=handle_check)

    report_parser = subparsers.add_parser("report", help="Afficher l’état d’avancement.")
    report_parser.set_defaults(func=handle_report)

    return parser


def main(argv: List[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()

