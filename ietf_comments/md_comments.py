import commonmark
from commonmark.render.renderer import Renderer

from .changes import DocChanges


class CommentRenderer(Renderer):
    sections = ["discuss", "comment", "nit"]
    section_map = {"discusses": "discuss", "comments": "comment", "nits": "nit"}
    BLOCK = "block"

    def __init__(self, ui, options={}):
        self.ui = ui
        self.options = options
        self._buffer = []
        self._section = None
        self._current_issue = None
        self._context = None
        self._context_buffer = []
        self.title = None
        self.doc = None
        self.revision = None
        self.cc = None
        self.changes = None
        self.issues = {"discuss": [], "comment": [], "nit": []}

    def document(self, node, entering):
        if not entering:
            self.cleanup()
            if sum([len(l) for l in self.issues.values()]) == 0:
                self.ui.warn("Did not find any issues.")

    def softbreak(self, node, entering=None):
        self._buffer.append(" ")
        if self._context_buffer:
            self._context_buffer.append(" ")

    def linebreak(self, node, entering):
        self._buffer.append("\n\n")

    def text(self, node, entering=None):
        self._buffer.append(node.literal)
        if self._context is not None:
            self._context_buffer.append(node.literal)

    def emph(self, node, entering):
        self._buffer.append("_")

    def strong(self, node, entering):
        self._buffer.append("**")

    def paragraph(self, node, entering):
        if not entering and node.parent.t != "item":
            self._buffer.append("\n\n")

    def link(self, node, entering):
        if entering:
            self._buffer.append("[")
        else:
            self._buffer.append(f"]({node.destination})")

    def code(self, node, entering):
        self._buffer.append(f"`{node.literal}`")

    def code_block(self, node, entering):
        info = node.info or ""
        self._buffer.append(f"~~~ {info}\n{node.literal}~~~\n")

    def item(self, node, entering):
        if entering:
            self._buffer.append("* ")

    def block_quote(self, node, entering):
        if entering:
            self._buffer.append("> ")
            self._context = self.BLOCK
        else:
            self._context = None
            content = "".join(self._context_buffer)
            self._context_buffer = []
            change_location = self.changes.find_change_line(content)
            if change_location is None:
                self.ui.warn(f"Can't find quoted text in document: {content}")

    def heading(self, node, entering):
        if node.level < 4:
            if entering:
                self.cleanup()
            else:
                content = self.get_buffer()
                getattr(self, f"handle_h{node.level}")(content)
        else:
            if entering:
                self._buffer.append(f"{'#' * (node.level - 1)} ")
            else:
                self._buffer.append("\n\n")

    def handle_h1(self, content):
        if self.doc is not None:
            self.ui.error("More than one h1 header.")
        self.title = content
        docname = None
        words = content.lower().split()
        for word in words:
            if word.startswith("draft-"):
                docname = word
                break
        if docname is None:
            self.ui.error(
                "h1 header doesn't contain draft name (starting with 'draft-')."
            )
        segments = docname.split("-")
        self.doc = "-".join(segments[:-1])
        revision = segments[-1]
        if revision.isnumeric():
            self.revision = revision
        else:
            self.ui.error("h1 header draft name doesn't include revision")
        self.changes = DocChanges(self.doc, self.revision, self.ui)

    def handle_h2(self, content):
        content = content.lower()
        if content in self.section_map:
            content = self.section_map[content]
        if content in self.sections:
            self._section = content
        else:
            self.ui.warn(f"Unrecognised h2 section {content}.")
            self._section = None

    def handle_h3(self, content):
        self._current_issue = content

    def get_buffer(self):
        content = "".join(self._buffer)
        self._buffer = []
        return content

    def cleanup(self):
        if self._section:
            text = self.get_buffer()
            if self._current_issue and text:
                self.issues[self._section].append((self._current_issue, text))
        else:
            self.process_preface()
        self._current_issue = None
        self._buffer = []

    def process_preface(self):
        text = self.get_buffer()
        if text:
            for line in text.split("\n"):
                if line.lstrip().lower().startswith("cc @"):
                    self.cc = line.strip().split("@", 1)[1]
                    break


def parse_markdown_comments(fd, ui):
    parser = commonmark.Parser()
    doc = parser.parse(fd.read())
    renderer = CommentRenderer(ui)
    renderer.render(doc)
    return renderer
