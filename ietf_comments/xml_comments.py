import re
from io import StringIO
import os
import textwrap
import xml.sax

import requests


class XmlCommentHandler(xml.sax.handler.LexicalHandler):
    source_regex = re.compile(
        r"^\s*\[\s*([a-zA-z0-9\-]+)\s*\]\s*(.+)", flags=re.MULTILINE | re.DOTALL
    )

    def __init__(self):
        self.comments = []

    def comment(self, content):
        result = self.source_regex.match(content)
        if result:
            source = result.group(1)
            comment = fix_blockquotes(result.group(2))
            title = extract_title(comment, "RFC Editor Comment")
            if source == "rfced":
                self.comments.append((title, comment))


def parse_xml_comments(rfc, ui):
    if not os.path.isfile(rfc):
        rfcxml = fetch_rfcxml(rfc, ui)
        rfc = StringIO(rfcxml)
    parser = xml.sax.make_parser()
    handler = XmlCommentHandler()
    parser.setProperty("http://xml.org/sax/properties/lexical-handler", handler)
    parser.parse(rfc)
    return handler.comments


def fetch_rfcxml(rfcnum, ui):
    if not rfcnum.isnumeric():
        ui.error(f"'{rfcnum}' is not a file and not numeric.")
    url = f"https://www.rfc-editor.org/authors/rfc{rfcnum}.xml"
    res = requests.get(url)
    if res.status_code != 200:
        ui.error(f"RFC{rfcnum}-to-be not found on RFC Editor server.")
    return res.text


colon_title = re.compile(r"^([^:]{,70}):")
question_title = re.compile(r"^([^?]{,70}\?)", re.MULTILINE)
sentence_title = re.compile(r"^(.{,70})(?=\.\s+)", re.MULTILINE)


def extract_title(text, default):
    colon_result = colon_title.match(text)
    if colon_result:
        return colon_result.group(1).strip()
    question_result = question_title.match(text)
    if question_result:
        return question_result.group(1).strip()
    sentence_result = sentence_title.match(text)
    if sentence_result:
        return sentence_result.group(1).strip()
    return default


quoted_start = re.compile(
    r"(Currently|Original|Suggested|Possibly):\s*\n(\s+.*?)(\n\n|$)", re.DOTALL
)


def blockquote_indent(match):
    indented = textwrap.indent(match.group(2), "    ", lambda line: True)
    return f"{match.group(1)}:\n\n{indented}{match.group(3)}"


def fix_blockquotes(text):
    return quoted_start.sub(blockquote_indent, text)
