# The IETF Comments Markdown Format

The IETF Comment Markdown Format is a [markdown](https://commonmark.org) dialect for describing IETF review comments. Following common practice, it uses `h2` headings to identify three main levels of comments (or issues):

* **Discuss** - a significant issue that requires further discussion
* **Comment** - an issue that was noticed, but is not significant enough to block document progress
* **Nit** - a minor (usually, editorial) issue that the reviewer noticed; no response is necessary, but the author might want to take it into consideration.

See the [examples directory](https://github.com/mnot/ietf-comments/tree/main/examples) for examples of the format in use.

This page summarises the format for reviewers. Reviewers can validate a document using the command-line tool; e.g.,

~~~ shell
> ./ietf-comments _filename_
~~~

## Document Header

The document should start with a header indicating the title of the review; for example:

~~~ markdown
# Security AD comments for draft-ietf-whatever-document-08
~~~

It must:
* Be a `h1` header (i.e., one octothorp)
* Be the only `h1` header in the document
* Identify the reviewer, either by name or position
* Identify the draft being reviewed by its _with_ revision number

Optionally, a reviewer can indicate that they want their GitHub username to be `@` mentioned in any issues created by adding a line after the `h1` header that starts with `CC`, followed by their GitHub username; for example:

~~~ markdown
CC @mnot
~~~

This first part can contain other content (e.g., acknowledgements, a preface, etc.) that will not be converted into issues.

## Review Comments

Then, the document can contain `discuss`, `comment`, and `nit` positions, each in their own subsection indicated by a `h2` header (i.e., two octothorps), followed by optional free text and then any number of issues.

Issues within a section should each have a descriptive title in a `h3` header (i.e., three octothorps). Issues can contain any markdown, including blockquotes, links, emphasis, lists, etc.

For example:

~~~ markdown
# AD Review for draft-ietf-whatever-whenever-00

Thanks for a well-written document. My comments are below.

## Discuss

### Space/Time

This document has serious implications for the space/time continuum. We should
talk about that.

## Comments

### Wrong references

The references in section 2.1 are not correct.

### Does it work that way?

The widget in s 5.4.3 doesn't seem well-specified; are you sure?

### I don't like it.

The whole thing. But I won't make it a discuss.

## Nits

### Missing pages

The following pages are missing:

* 53
* 49
* 42

~~~



