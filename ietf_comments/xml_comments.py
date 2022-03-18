import re
from io import StringIO
import os
import textwrap
import xml.sax

import requests


def parse_xml_comments(rfc, ui):
    if not os.path.isfile(rfc):
        rfcxml = fetch_rfcxml(rfc, ui)
        rfc = StringIO(rfcxml)
    parser = xml.sax.make_parser()
    handler = XmlCommentHandler()
    parser.setProperty("http://xml.org/sax/properties/lexical-handler", handler)
    parser.parse(rfc)
    return handler.comments


class XmlCommentHandler(xml.sax.handler.LexicalHandler):
    source_regex = re.compile(
        r"^\s*\[\s*([a-zA-z0-9\-]+)\s*\]\s*(.+)", flags=re.MULTILINE | re.DOTALL
    )
    colon_title = re.compile(r"^([^:]{,70}):")
    question_title = re.compile(r"^([^?]{,70}\?)", re.MULTILINE)
    sentence_title = re.compile(r"^(.{,70})(?=\.\s+)", re.MULTILINE)
    quoted_start = re.compile(
        r"(Currently|Original|Suggested|Possibly):\s*\n(\s+.*?)(\n\n|$)", re.DOTALL
    )

    def __init__(self):
        self.comments = []

    def comment(self, content):
        result = self.source_regex.match(content)
        if result:
            source = result.group(1)
            if source == "rfced":
                raw_comment = result.group(2)
                title = self.extract_title(raw_comment)
                comment = self.process_comment(raw_comment)
                self.comments.append((title, comment))

    def extract_title(self, text):
        colon_result = self.colon_title.match(text)
        comment_num = len(self.comments) + 1
        comment_counter = f" (comment {comment_num})"
        if colon_result:
            return colon_result.group(1).strip() + comment_counter
        question_result = self.question_title.match(text)
        if question_result:
            return question_result.group(1).strip() + comment_counter
        sentence_result = self.sentence_title.match(text)
        if sentence_result:
            return sentence_result.group(1).strip() + comment_counter
        return f"RFC Editor comment {comment_num}"

    def process_comment(self, text):
        adjusted = self.quoted_start.sub(self.blockquote_indent, text)
        return adjusted

    @classmethod
    def blockquote_indent(cls, match):
        indented = textwrap.indent(match.group(2), "    ", lambda line: True)
        return f"{match.group(1)}:\n\n{indented}{match.group(3)}"


def fetch_rfcxml(rfcnum, ui):
    if not rfcnum.isnumeric():
        ui.error(f"'{rfcnum}' is not a file and not numeric.")
    url = f"https://www.rfc-editor.org/authors/rfc{rfcnum}.xml"
    res = requests.get(url)
    if res.status_code != 200:
        ui.error(f"RFC{rfcnum}-to-be not found on RFC Editor server.")
    return res.text
