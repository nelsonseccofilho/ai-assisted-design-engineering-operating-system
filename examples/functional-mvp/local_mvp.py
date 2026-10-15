"""Fictional local card workflow. Actor contexts are trusted test inputs, not authentication."""
import argparse
from contextlib import closing
from dataclasses import dataclass
import json
from pathlib import Path
import sqlite3
import sys


class WorkflowError(Exception):
    pass


class Denied(WorkflowError):
    pass


class Invalid(WorkflowError):
    pass


class InjectedFailure(WorkflowError):
    pass


@dataclass(frozen=True)
class Actor:
    """Trusted fictional context; the CLI deliberately lets the operator select it."""
    alias: str
    role: str
    scope: str


def connect(path):
    # mode=rw prevents a typo from silently creating another database.
    connection = sqlite3.connect(Path(path).resolve().as_uri() + "?mode=rw", uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys=ON")
    return connection


def initialize(path):
    path = Path(path).resolve()
    # Reserve only an explicitly named new file. Never replace an existing database.
    with path.open("xb"):
        pass
    with closing(connect(path)) as connection:
        connection.executescript("""
            CREATE TABLE cards (
                id TEXT PRIMARY KEY, scope TEXT NOT NULL, title TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('DRAFT','PUBLISHED')),
                revision INTEGER NOT NULL CHECK(revision > 0));
            CREATE TABLE approvals (
                card_id TEXT NOT NULL REFERENCES cards(id), revision INTEGER NOT NULL,
                actor TEXT NOT NULL, PRIMARY KEY(card_id, revision));
            CREATE TABLE events (
                id INTEGER PRIMARY KEY, card_id TEXT NOT NULL REFERENCES cards(id),
                action TEXT NOT NULL, actor TEXT NOT NULL, revision INTEGER NOT NULL);
        """)
        with connection:
            connection.executemany("INSERT INTO cards VALUES (?,?,?,?,?)", [
                ("CARD-A", "ALPHA", "Fictional Alpha card", "DRAFT", 1),
                ("CARD-B", "BETA", "Fictional Beta card", "DRAFT", 1)])
    return {"initialized": True, "fictional_records": 2}


def check_actor(actor):
    if (not isinstance(actor, Actor) or not isinstance(actor.alias, str)
            or not isinstance(actor.scope, str) or not actor.alias.strip() or not actor.scope.strip()):
        raise Invalid("A fictional actor and scope are required")
    if not isinstance(actor.role, str) or actor.role not in {"READER", "EDITOR", "REVIEWER"}:
        raise Denied("Unsupported fictional role")


def scoped_card(connection, actor, card_id):
    check_actor(actor)
    row = connection.execute("SELECT * FROM cards WHERE id=? AND scope=?",
                             (card_id, actor.scope)).fetchone()
    if row is None:
        raise Denied("Card unavailable in this scope")
    return row


def read_card(path, actor, card_id):
    with closing(connect(path)) as connection:
        row = dict(scoped_card(connection, actor, card_id))
        row["current_approval"] = connection.execute(
            "SELECT 1 FROM approvals WHERE card_id=? AND revision=?",
            (row["id"], row["revision"])).fetchone() is not None
        return row


def act(path, actor, action, card_id, title=None, inject_failure=False):
    """Apply one atomic local action; injected failure is a test hook, absent from the CLI."""
    check_actor(actor)
    with closing(connect(path)) as connection:
        with connection:
            connection.execute("BEGIN IMMEDIATE")
            card = scoped_card(connection, actor, card_id)
            if card["status"] != "DRAFT":
                raise Invalid("This fixture only changes draft cards")
            revision = card["revision"]
            if action == "rename":
                if actor.role != "EDITOR":
                    raise Denied("Rename requires the fictional editor role")
                if not isinstance(title, str) or not 1 <= len(title.strip()) <= 80:
                    raise Invalid("Title must contain 1 to 80 nonblank characters")
                revision += 1
                connection.execute("UPDATE cards SET title=?,revision=? WHERE id=?",
                                   (title.strip(), revision, card_id))
            elif action == "approve":
                if actor.role != "REVIEWER":
                    raise Denied("Approval requires the fictional reviewer role")
                connection.execute("INSERT INTO approvals VALUES (?,?,?)",
                                   (card_id, revision, actor.alias))
            elif action == "publish":
                if actor.role != "EDITOR":
                    raise Denied("Publish requires the fictional editor role")
                approved = connection.execute(
                    "SELECT 1 FROM approvals WHERE card_id=? AND revision=?",
                    (card_id, revision)).fetchone()
                if approved is None:
                    raise Denied("The current revision needs fictional review approval")
                connection.execute("UPDATE cards SET status='PUBLISHED' WHERE id=?", (card_id,))
            else:
                raise Invalid("Unknown fixture action")
            connection.execute("INSERT INTO events(card_id,action,actor,revision) VALUES (?,?,?,?)",
                               (card_id, action, actor.alias, revision))
            if inject_failure:
                raise InjectedFailure("Fictional failure after writes, before commit")
    return read_card(path, actor, card_id)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, required=True)
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("init")
    for action in ("show", "rename", "approve", "publish"):
        command = sub.add_parser(action)
        command.add_argument("card_id")
        command.add_argument("--actor", required=True)
        command.add_argument("--role", choices=("READER", "EDITOR", "REVIEWER"), required=True)
        command.add_argument("--scope", required=True)
        if action == "rename":
            command.add_argument("--title", required=True)
    args = parser.parse_args()
    try:
        if args.action == "init":
            result = initialize(args.db)
        else:
            actor = Actor(args.actor, args.role, args.scope)
            result = read_card(args.db, actor, args.card_id) if args.action == "show" else act(
                args.db, actor, args.action, args.card_id, getattr(args, "title", None))
    except (WorkflowError, sqlite3.Error, OSError) as error:
        print(json.dumps({"error": type(error).__name__, "message": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
