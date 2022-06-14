import argparse
import sys

# pylint: disable=wrong-import-position
# monkeypatch to use requests rather than xmlhttprequest. yes, this is nasty.
import ietf_comments_engine.util
import requests

ietf_comments_engine.util.get = requests.get  # type: ignore[assignment]

from blessings import Terminal  # type: ignore[import]
from ietf_comments_engine.md_comments import parse_markdown_comments
from ietf_comments_engine.types import CommentType, Ui

from . import __version__
from .github import create_issues

term = Terminal()


class Cli(Ui):
    @classmethod
    def out(cls, content: str) -> None:
        sys.stdout.write(content)

    def status(self, name: str, value: str) -> None:
        sys.stderr.write(f"{term.green}{name}:{term.normal} {value}\n")

    def warn(self, message: str, source: str = "") -> None:
        if source:
            source = f"{source} "
        sys.stderr.write(f"{term.yellow}{source}Warning{term.normal}: {message}\n")

    def error(self, message: str, source: str = "") -> None:
        if source:
            source = f"{source} "
        sys.stderr.write(f"{term.red}{source}Error{term.normal}: {message}\n")
        sys.exit(1)

    def comment(self, comment: CommentType) -> None:
        self.out(f"{term.blue}## {comment[0]}{term.normal}\n")
        self.out(f"{comment[1]}\n")
        self.out("\n")


def base_arg_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-g",
        "--github_repo",
        metavar="owner/repo",
        dest="github_repo",
        help="create issues in the named repo",
    )

    parser.add_argument(
        "-l",
        "--github-label",
        dest="github_label",
        action="append",
        help="label to assign to created GitHub issues",
    )

    parser.add_argument(
        "-s",
        "--start",
        dest="start_num",
        type=int,
        metavar="NN",
        default=None,
        help="Comment number to skip to when creating issues",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{__version__}",
        help="print version and exit",
    )
    return parser


def ietf_comments_cli() -> None:
    args = parse_ietf_args()
    cli = Cli()
    comments = parse_markdown_comments(args.comment_file.read(), cli)
    base = f"https://www.ietf.org/archive/id/{comments.doc}-{comments.revision}.html"
    cli.status("Document", comments.doc)
    cli.status("Revision", comments.revision)
    if comments.cc:
        cli.status("CC", f"@{comments.cc}")
    for issue_type in comments.sections:
        these_comments = comments.issues[issue_type]
        if args.github_repo:
            labels = args.github_label or []
            if args.auto_label:
                labels.extend(["review", issue_type])
            create_issues(
                args.github_repo,
                cli,
                base,
                these_comments,
                labels,
                comments.cc,
                args.start_num,
            )
        else:
            cli.out(f"\n{term.green}# {issue_type}{term.normal}\n")
            for comment in these_comments:
                cli.comment(comment)


def parse_ietf_args() -> argparse.Namespace:
    parser = base_arg_parser("Process a markdown file containing IETF comments")
    parser.add_argument(
        "-a",
        "--auto-label",
        dest="auto_label",
        action="store_true",
        help="Add a 'review' label, and 'discuss', 'comment', or 'nit' as appropriate",
    )
    parser.add_argument(
        "comment_file",
        metavar="filename",
        type=argparse.FileType("r"),
        help="comment file to process",
    )
    return parser.parse_args()


def rfced_comments_cli() -> None:
    if sys.version_info.minor < 10:
        sys.stderr.write("ERROR: rfced-comments requires Python 3.10.\n")
        sys.exit(1)
    from ietf_comments_engine.xml_comments import (  # pylint: disable=import-outside-toplevel
        parse_xml_comments,
    )

    args = parse_rfced_args()
    cli = Cli()
    comments = parse_xml_comments(args.rfc, cli)
    if args.rfc.isnumeric():
        rfcnum = args.rfc
    else:
        rfcnum = "NNNN"
    if args.github_repo:
        labels = args.github_label or []
        base = f"https://www.rfc-editor.org/authors/rfc{rfcnum}.html"
        create_issues(
            args.github_repo, cli, base, comments, labels, start_num=args.start_num
        )
    else:
        for comment in comments:
            cli.comment(comment)


def parse_rfced_args() -> argparse.Namespace:
    parser = base_arg_parser("Process an AUTH48 draft for RFC Editor comments")
    parser.add_argument(
        "rfc",
        metavar="NNNN",
        help="RFC-to-be number or filename to process",
    )
    return parser.parse_args()
