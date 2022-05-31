from typing import Tuple

CommentType = Tuple[str, str]


class Ui:
    @classmethod
    def out(cls, content: str) -> None:
        pass

    @classmethod
    def status(cls, name: str, value: str) -> None:
        pass

    @classmethod
    def warn(cls, message: str, source: str = "") -> None:
        pass

    @classmethod
    def error(cls, message: str, source: str = "") -> None:
        pass

    def comment(self, comment: CommentType) -> None:
        pass
