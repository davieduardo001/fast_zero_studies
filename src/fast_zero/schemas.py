from pathlib import Path

from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Html(BaseModel):
    file: Path

    @property
    def content(self) -> str:
        return self.file.read_text()
