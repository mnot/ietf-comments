import requests


class DocChanges:
    URL_BASE = "https://www.ietf.org/archive/id/"

    def __init__(self, docname, revision, ui):
        self.docname = docname
        self.revision = revision
        self.ui = ui
        self.text_doc = self.get_doc("txt")

    def get_doc(self, doctype):
        res = requests.get(f"{self.URL_BASE}/{self.docname}-{self.revision}.{doctype}")
        if res.status_code != 200:
            self.ui.warn(
                f"Can't find {self.docname}-{self.revision} text on IETF servers."
            )
        doc = res.text
        return doc

    def find_change_line(self, old):
        old_words = old.split()
        old_word_count = len(old_words)
        line_no = 0
        lines_consumed = 0
        words_consumed = 0
        for line in self.text_doc.split("\n"):
            line_no += 1
            line_words = line.split()
            line_word_count = len(line_words)
            line_words_consumed = 0
            if old_words[0] in line_words or words_consumed > 0:
                if words_consumed > 0:
                    start_word = 0
                else:
                    try:
                        start_word = line_words.index(old_words[0])
                    except ValueError:
                        continue
                for line_word in line_words[start_word:]:
                    if line_word != old_words[words_consumed]:
                        words_consumed = lines_consumed = 0
                        break
                    line_words_consumed += 1
                    words_consumed += 1
                    if words_consumed == old_word_count:
                        return line_no - lines_consumed, lines_consumed + 1
                if line_words_consumed + start_word == line_word_count:
                    lines_consumed += 1
