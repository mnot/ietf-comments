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


SECTION_MARKERS = {
    "section": "section",
    "sections": "section",
    "s": "section",
    "§": "section",
    "appendix": "appendix",
}


def link_sections(text, base, ui):
    in_link = False
    text_out = []
    for line in text.split("\n"):
        line_out = []
        link_word = None
        for word in line.split(" "):
            if link_word is not None:
                section_id = word
                rest = ""
                extra_chars = 0
                try:
                    while not section_id[-1].isnumeric():
                        extra_chars += 1
                        section_id = word[:-extra_chars]
                        rest = word[-extra_chars]
                except IndexError:
                    line_out.append(f"{link_word} {word}")
                    link_word = None
                    continue
                frag_base = SECTION_MARKERS[link_word.lower().strip()]
                line_out.append(
                    f"[{link_word} {section_id}]({base}#{frag_base}-{section_id}){rest}"
                )
                link_word = None
            elif word.lower().strip() in SECTION_MARKERS:
                link_word = word
            else:
                line_out.append(word)
        text_out.append(" ".join(line_out))
    return "\n".join(text_out)
