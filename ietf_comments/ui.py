import argparse
import sys

from . import __version__
from .md_comments import parse_markdown_comments
from .xml_comments import parse_xml_comments
from .github import create_issues

from blessings import Terminal

term = Terminal()


class Cli:
    @classmethod
    def out(cls, content):
        sys.stdout.write(content)

    @classmethod
    def status(cls, name, value):
        sys.stderr.write(f"{term.green}{name}:{term.normal} {value}\n")

    @classmethod
    def warn(cls, message, source=""):
        if source:
            source = f"{source} "
        sys.stderr.write(f"{term.yellow}{source}Warning{term.normal}: {message}\n")

    @classmethod
    def error(cls, message, source=""):
        if source:
            source = f"{source} "
        sys.stderr.write(f"{term.red}{source}Error{term.normal}: {message}\n")
        sys.exit(1)

    def comment(self, comment):
        self.out(f"{term.blue}## {comment[0]}{term.normal}\n")
        self.out(f"{comment[1]}\n")
        self.out("\n")


def base_arg_parser(description):
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


def ietf_comments_cli():
    args = parse_ietf_args()
    cli = Cli()
    comments = parse_markdown_comments(args.comment_file, cli)
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


def parse_ietf_args():
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


def rfced_comments_cli():
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


def parse_rfced_args():
    parser = base_arg_parser("Process an AUTH48 draft for RFC Editor comments")
    parser.add_argument(
        "rfc",
        metavar="NNNN",
        help="RFC-to-be number or filename to process",
    )
    return parser.parse_args()
