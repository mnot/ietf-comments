import re
from io import StringIO
import os
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
            comment = result.group(2)
            self.comments.append((source.lower(), comment))


def parse_xml_comments(rfc, ui):
    if not os.path.isfile(rfc):
        rfcxml = fetch_rfcxml(rfc, ui)
        rfc = StringIO(rfcxml)
    parser = xml.sax.make_parser()
    handler = XmlCommentHandler()
    parser.setProperty("http://xml.org/sax/properties/lexical-handler", handler)
    parser.parse(rfc)
    return [
        ("RFC Editor Comment", comment[1])
        for comment in handler.comments
        if comment[0] == "rfced"
    ]


def fetch_rfcxml(rfcnum, ui):
    if not rfcnum.isnumeric():
        ui.error(f"'{rfcnum}' is not a file and not numeric.")
    url = f"https://www.rfc-editor.org/authors/rfc{rfcnum}.xml"
    res = requests.get(url)
    if res.status_code != 200:
        ui.error(f"RFC{rfcnum}-to-be not found on RFC Editor server.")
    return res.text
