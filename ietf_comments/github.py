import os
from typing import List

from github import Github, Label, GithubException
from github.GithubException import UnknownObjectException
from ietf_comments_engine.types import CommentType, Ui

from .linkify import linkify

DEFAULT_COLOUR = "b6d7a8"


class GithubRepo:
    def __init__(self, reponame: str, ui: Ui) -> None:
        token = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        if token is None:
            ui.error(
                "GITHUB_ACCESS_TOKEN not set. See: <https://github.com/settings/tokens>"
            )
        try:
            gh = Github(token)
            self.repo = gh.get_repo(reponame)
        except GithubException as err:
            ui.error(str(err.data["message"]), "GitHub Repo")

    def create_issue(self, title: str, content: str, labels: List[str], cc: str) -> int:
        _labels: List[Label.Label] = []
        for label_text in labels:
            try:
                label = self.repo.get_label(label_text)
            except UnknownObjectException:
                label = self.repo.create_label(label_text, DEFAULT_COLOUR)
            _labels.append(label)
        if cc:
            content = f"_Comment by @{cc}_\n\n{content}"
        issue = self.repo.create_issue(
            title=normalise_ws(title), body=content, labels=_labels
        )
        return issue.number


def create_issues(
    reponame: str,
    ui: Ui,
    base: str,
    comments: List[CommentType],
    labels: List[str],
    cc: str = None,
    start_num: int = None,
) -> None:
    repo = GithubRepo(reponame, ui)
    if labels is None:
        labels = []
    for num, comment in enumerate(comments, start=1):
        if start_num and num < start_num:
            continue
        title = f"{comment[0]}"
        content = linkify(comment[1], base)
        try:
            number = repo.create_issue(title, content, labels, cc)
        except GithubException as err:
            ui.error(
                f"{err.data['message']} - restart with --start={num}",
                "Github Issue Creation",
            )
        ui.status(f"* Created issue {number} in {reponame}", f"{title}")


def normalise_ws(text: str) -> str:
    return " ".join(text.split())
