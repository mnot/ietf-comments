
# The IETF Comments Processor

Handling comments from the IESG, multiple directorate reviews, and in AUTH48 can be burdensome for document authors, because of the sheer number of comments, and because they come in an unstructured format that has to be manually processed.

This package installs two commands:

* `ietf-comments` processes comments from the IESG and directorates in a [markdown](https://commonmark.org)-based format.
* `rfced-comments` processes comments from the RFC Editor in RFC XML files.

Both can be used to create GitHub issues for the comments they find. When used properly, they can help automate formerly tiresome tasks.

For IESG and directorate comments, this tool uses the [IETF Comment Markdown format](#format), which is similar to the semi-structured format that ADs and directorates use now. Ideally, they will create comments in that format for easy processing, but even when they don't, most comments can easily be transformed into it for processing.


## Installation

To install ietf-comments, you'll need [Python 3](https://www.python.org/). Then, run:

> pip3 install ietf-comments


## Processing AD and Directorate Comments

To validate a AD or Directorate review in the [IETF Comment Markdown format](#format) and see the identified issues, run:

> ietf-comments _filename_

To create a GitHub issue for each issue, set `GITHUB_ACCESS_TOKEN` in your environment to a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and run:

> ietf-comments -g _owner/repo_ _filename_

... where `owner/repo` is the repo owner and name, separated by a slash.

If you'd like these issues to have a specific label, run:

> ietf-comments -g _owner/repo_ _filename_ -l _labelname_


## Processing RFC Editor Comments

To validate RFC Editor comments in a local RFC XML file and see the identified issues, run:

> rfced-comments _filename_

Alternatively, if you're in AUTH48 and the RFC Editor has published a draft of your RFC-to-be, you can just run

> rfced-comments _NNNN_

where `NNNN` is the RFC number.

To create a GitHub issue for each issue, set `GITHUB_ACCESS_TOKEN` in your environment to a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and run:

> rfced-comments -g _owner/repo_ _NNNN_or_filename_

... where `owner/repo` is the repo owner and name, separated by a slash.

If you'd like these issues to have a specific label, run:

> rfced-comments -g _owner/repo_ _NNNN_or_filename_ -l _labelname_


## The IETF Comments Format

The IETF Comment Format is a set of restrictions on the [markdown](https://commonmark.org) format that facilitates identifying the issues raised in the comments and their types, so that tooling can more easily digest it.

See the [examples directory](https://github.com/mnot/ietf-comments/tree/main/examples) for examples of the format in use.


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


### Issues

Individual issues within a comment section can be identified with `h3` headers, as they are above. Alternatively, if a comment section does not have `h3` headers, the text in that section will be considered to be a single issue.
