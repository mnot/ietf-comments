import os

from github import Github
from github.GithubException import UnknownObjectException

from ietf_comments.linkify import linkify

DEFAULT_COLOUR = "b6d7a8"


class GithubRepo:
    def __init__(self, reponame, ui):
        token = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        if token is None:
            ui.error("GITHUB_ACCESS_TOKEN not set.")
        g = Github(token)
        self.repo = g.get_repo(reponame)

    def create_issue(self, title, content, labels):
        _labels = []
        for label_text in labels:
            try:
                label = self.repo.get_label(label_text)
            except UnknownObjectException:
                label = self.repo.create_label(label_text, DEFAULT_COLOUR)
            _labels.append(label)
        issue = self.repo.create_issue(title=title, body=content, labels=_labels)
        return issue.number


def create_issues(reponame, ui, base, comments, labels=None):
    repo = GithubRepo(reponame, ui)
    if labels is None:
        labels = []
    for comment in comments:
        title = f"{comment[0]}"
        content = linkify(comment[1], base)
        number = repo.create_issue(title, content, labels)
        ui.status(f"* Created issue {number} in {reponame}: {title}")
