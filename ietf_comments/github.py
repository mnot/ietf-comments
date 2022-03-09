import os

from github import Github
from github.GithubException import UnknownObjectException

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
        content = link_sections(comment[1], base, ui)
        number = repo.create_issue(title, content, labels)
        ui.status(f"* Created issue {number} in {reponame}: {title}")


SECTION_MARKERS = ["section", "sections", "s", "§"]


def link_sections(text, base, ui):
    in_link = False
    text_out = []
    for line in text.split("\n"):
        line_out = []
        for word in line.split(" "):
            if in_link:
                section_id = word
                rest = ""
                extra_chars = 0
                try:
                    while not section_id[-1].isnumeric():
                        extra_chars += 1
                        section_id = word[:-extra_chars]
                        rest = word[-extra_chars]
                except IndexError:
                    ui.warn(f"Section ID '{word}' isn't numeric.")
                line_out.append(f"{section_id}]({base}#section-{section_id}){rest}")
                in_link = False
            elif word.lower().strip() in SECTION_MARKERS:
                line_out.append(f"[{word}")
                in_link = True
            else:
                line_out.append(word)
        text_out.append(" ".join(line_out))
    return "\n".join(text_out)
