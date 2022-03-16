import os

from github import Github, GithubException
from github.GithubException import UnknownObjectException

from .linkify import linkify

DEFAULT_COLOUR = "b6d7a8"


class GithubRepo:
    def __init__(self, reponame, ui):
        token = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        if token is None:
            ui.error(
                "GITHUB_ACCESS_TOKEN not set. See: <https://github.com/settings/tokens>"
            )
        try:
            g = Github(token)
            self.repo = g.get_repo(reponame)
        except GithubException as err:
            ui.error(err.data["message"])

    def create_issue(self, title, content, labels, cc):
        _labels = []
        for label_text in labels:
            try:
                label = self.repo.get_label(label_text)
            except UnknownObjectException:
                label = self.repo.create_label(label_text, DEFAULT_COLOUR)
            _labels.append(label)
        if cc:
            content = f"_Comment by @{cc}_\n\n{content}"
        issue = self.repo.create_issue(title=title, body=content, labels=_labels)
        return issue.number


def create_issues(reponame, ui, base, comments, labels, cc=None):
    repo = GithubRepo(reponame, ui)
    if labels is None:
        labels = []
    for comment in comments:
        title = f"{comment[0]}"
        content = linkify(comment[1], base)
        number = repo.create_issue(title, content, labels, cc)
        ui.status(f"* Created issue {number} in {reponame}", f"{title}")
