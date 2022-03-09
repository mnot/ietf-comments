SECTION_MARKERS = {
    "section": "section",
    "sections": "section",
    "s": "section",
    "§": "section",
    "appendix": "appendix",
}


def linkify(text, spec_uri):
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
                    f"[{link_word} {section_id}]({spec_uri}#{frag_base}-{section_id}){rest}"
                )
                link_word = None
            elif word.lower().strip() in SECTION_MARKERS:
                link_word = word
            else:
                line_out.append(word)
        text_out.append(" ".join(line_out))
    return "\n".join(text_out)
