import json
import os
import sys

from github import Github
from github.GithubException import UnknownObjectException

DEFAULT_COLOUR = "b6d7a8"


class GithubRepo:
    def __init__(self, repo):
        token = os.environ.get("GITHUB_AUTH_TOKEN", None)
        if token is None:
            sys.stderr.write("Error: GITHUB_AUTH_TOKEN not set.\n")
            sys.exit(1)
        g = Github(token)
        self.repo = g.get_repo(repo)

    def create_issue(self, title, content, labels=[]):
        _labels = []
        for label_text in labels:
            try:
                label = self.repo.get_label(label_text)
            except UnknownObjectException:
                label = self.repo.create_label(label_text, DEFAULT_COLOUR)
            _labels.append(label)
        issue = self.repo.create_issue(title=title, body=content, labels=_labels)
        return issue.number


def create_issues(repo, comments, labels=[]):
    repo = GithubRepo(repo)
    for issue_type in comments.issues.keys():
        issues = comments.issues[issue_type]
        for issue in issues:
            title = issue[0]
            content = issue[1]
            number = repo.create_issue(title, content, labels)
            sys.stderr.write(f"* Created issue {number}: {title}\n")
