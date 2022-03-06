import os

from github import Github
from github.GithubException import UnknownObjectException

DEFAULT_COLOUR = "b6d7a8"


class GithubRepo:
    def __init__(self, reponame, ui):
        token = os.environ.get("GITHUB_AUTH_TOKEN", None)
        if token is None:
            ui.error("GITHUB_AUTH_TOKEN not set.")
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


def create_issues(reponame, ui, comments, labels=None):
    repo = GithubRepo(reponame, ui)
    if labels is None:
        labels = []
    ui.status(f"* Creating issues in {reponame}")
    for issue_type in comments.issues.keys():
        issues = comments.issues[issue_type]
        for issue in issues:
            title = f"{issue_type}: {issue[0]}"
            content = issue[1]
            number = repo.create_issue(title, content, labels)
            ui.status(f"* Created issue {number}: {title}")
