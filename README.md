
# The IETF Comments Processor

![Python version requirement](https://badgen.net/pypi/python/ietf-comments)
[![Package version](https://badgen.net/pypi/v/ietf-comments)](https://pypi.org/project/ietf-comments/)

Handling comments from the IESG, multiple directorate reviews, and in AUTH48 can be burdensome for document authors, because of the sheer number of comments, and because they come in an unstructured format that has to be manually processed.

This package installs two commands:

* `ietf-comments` processes comments from the IESG and directorates in a [markdown](https://commonmark.org)-based format.
* `rfced-comments` processes comments from the RFC Editor in RFC XML files.

Both can be used to create GitHub issues for the comments they find. When used properly, they can help automate formerly tiresome tasks.

For IESG and directorate comments, this tool uses the [IETF Comment Markdown format](https://github.com/mnot/ietf-comments/tree/main/format.md), which is a semi-structured format that is similar to that which ADs and directorates use now. Ideally, they will create comments in that format for easy processing, but even when they don't, most comments can easily be transformed into it for processing.


## Installation

To install ietf-comments, you'll need [Python 3.10](https://www.python.org/) or greater. Then, run:

> pip3 install ietf-comments

Note that if your pip is using another version of Python, it will silently install an outdated version of the package. To assure that Python 3.10 is being used, you may need to use something like:

> python3.10 -m pip install ietf-comments


## Use

### Processing AD and Directorate Comments

To validate a AD or Directorate review in the [IETF Comment Markdown format](https://github.com/mnot/ietf-comments/tree/main/format.md) and see the identified issues, run:

> ietf-comments _filename_

To create a GitHub issue for each issue, set `GITHUB_ACCESS_TOKEN` in your environment to a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and run:

> ietf-comments -g _owner/repo_ _filename_

... where `owner/repo` is the repo owner and name, separated by a slash.

If you'd like these issues to have a specific label, run:

> ietf-comments -g _owner/repo_ _filename_ -l _labelname_

If you'd like `discuss`, `comment`, and `nit labels` added as appropriate, along with a `review` label, pass `-a`:

> ietf-comments -g _owner/repo_ _filename_ -a



### Processing RFC Editor Comments

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




## Special Features

The following features are currently supported (more soon!):

* When recognised, internal section references (e.g., `Section 2.4`) are auto-linked in created issues.
* Likewise, references to external RFCs (e.g., `Section 5.3 of [RFC1234]`) will also be auto-linked in created issues when recognised.
* Text in blockquotes (preceded by `>`) in comments will be checked for presence in the document; if they aren't found, a warning will be raised.
