import re


flags = re.IGNORECASE | re.MULTILINE | re.VERBOSE
ref = r"[a-zA-Z0-9\-_]+"
section_finder = re.compile(
    rf"""
(?:
    \[(?P<comma_ref>{ref})\],\s*
)?
(?P<section>(?:section|sections|appendix|§)\s+)
(?P<num>[\d\.]*\d)\.?
(?:
    \s+of\s+\[(?P<of_ref>{ref})\]
)?
""",
    flags,
)


def linkify(text, spec_uri):
    def linker(matchobj):
        section = matchobj.group("section")
        if section.lower().strip() == "appendix":
            sref = "appendix"
        else:
            sref = "section"
        num = matchobj.group("num")
        if matchobj.group("comma_ref"):
            ref = matchobj.group("comma_ref")
            link = find_ref_uri(ref)
            if link:
                return f"[{ref}]({link}), [{section}{num}]({link}#{sref}-{num})"
            else:
                return f"[{ref}], {section}{num}"
        elif matchobj.group("of_ref"):
            ref = matchobj.group("of_ref")
            link = find_ref_uri(ref)
            if link:
                return f"[{section}{num}]({link}#{sref}-{num}) of [{ref}]({link})"
            else:
                return f"{section}{num} of [{ref}]"
        else:
            return f"[{section}{num}]({spec_uri}#{sref}-{num})"

    return section_finder.sub(linker, text)


def find_ref_uri(ref):
    if ref[:3].lower() == "rfc" and ref[3:].isnumeric():
        return f"https://rfc-editor.org/rfc/rfc{ref[3:]}.html"


if __name__ == "__main__":
    print(linkify("in section 4.3 of that", "https://www.example.com/"))
    print(linkify("in section 4.3. of that", "https://www.example.com/"))
    print(linkify("in [RFC3221], section 4.3 of that", "https://www.example.com/"))
    print(linkify("in Section  4.3 of [RFC2119]", "https://www.example.com/"))
    print(linkify("in section 4.3 of [OTHER_THING]", "https://www.example.com/"))
    print(linkify("in appendix 4.3 of [RFC1234]", "https://www.example.com/"))
    print(linkify("in section 4.3a of [OTHER_THING]", "https://www.example.com/"))
    print(linkify("in section 4a.3a of [OTHER_THING]", "https://www.example.com/"))
    print(linkify("in section a.3a of [OTHER_THING]", "https://www.example.com/"))
