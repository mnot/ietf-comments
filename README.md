
# The IETF Comments Processor

This is a script that processes the IETF Comments Format (see below) both to validate instances of it, and to create GitHub issues from it.

## Installation

To install ietf-comments, you'll need [Python 3](https://www.python.org/). Then, run:

> pip3 install ietf-comments

## Use

To validate a comments file and see the issues it contains, run:

> ietf-comments _filename_

To create a GitHub issue for each issue in the comments, set `GITHUB_ACCESS_TOKEN` in your environment to a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and run:

> ietf-comments -g _owner/repo_ _filename_

... where `owner/repo` is the repo owner and name, separated by a slash.

If you'd like these issues to have a specific label, run:

> ietf-comments -g _owner/repo_ _filename_ -l _labelname_


## The IETF Comments Format

The IETF Comment Format is a set of restrictions on the [markdown](https://commonmark.org) format that facilitates identifying the issues raised in the comments and their types, so that tooling can more easily digest it.

See the [examples directory](examples/) for examples of the format in use.


### Document Identity

The document should start with a header indicating the title of the review; for example:

~~~ markdown
# Security AD comments for draft-ietf-whatever-document-08
~~~

Note that it must:
* Be a `h1` header (i.e., one octothorp)
* Identifies the reviewer, either by name or position
* Identifies the subject of the review with the full draft name _with_ revision number
* Be the only `h1` header in the document


### Comment Sections

Then, the document can contain `discuss`, `comment`, and `nit` positions, each in their own subsection. For example:

~~~ markdown
## Comments

### Wrong references

The references in section 2.1 are not correct.

### Does it work that way?

The widget in s 5.4.3 doesn't seem well-specified; are you sure?
~~~

Note that:
* The type of comment is identified with `h2` headers (i.e., two octothorps)
* The type can be 'discuss', 'comment', or 'nit' with any capitalisation
* Each type header can occur exactly once in the document

Individual issues can be identified with `h3` headers, as they are above. Alternatively, if a section does not have `h3` headers, the text in that section will be considered to be a single issue.

Within text, section links are automatically added. It is assumed that the bare words 'section' and 's' are followed by a section number to be referenced in the document (as in the example above).
