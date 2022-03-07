import sys

from colorama import Fore, Back, Style


class Cli:
    @classmethod
    def out(cls, content):
        sys.stdout.write(content)

    @classmethod
    def status(cls, message):
        sys.stderr.write(f"{message}\n")

    @classmethod
    def warn(cls, message):
        sys.stderr.write(f"{Fore.YELLOW}Warning{Style.RESET_ALL}: {message}\n")

    @classmethod
    def error(cls, message):
        sys.stderr.write(f"{Fore.RED}Error{Style.RESET_ALL}: {message}\n")
        sys.exit(1)
