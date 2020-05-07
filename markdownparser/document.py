from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Document:
    title: str = ""
    metadata: Dict = {}
    root: DocumentNode


class DocumentNode:
    children: list = []


class DocumentRoot(DocumentNode):
    pass


class Header(DocumentNode):
    level: int = 1


class TextBlock(DocumentNode):
    text: str


class BoldBlock(DocumentNode):
    pass


class EnumBlock(DocumentNode):
    class EnumStyle(Enum):
        NUMBERS = auto
        POINTS = auto
    style: EnumStyle = EnumStyle.POINTS


class EnumItem(DocumentNode):
    index: int = 0


class GenericBlock(DocumentNode):
    block_type: str
    content: str
