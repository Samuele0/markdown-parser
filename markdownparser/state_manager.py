# Copyright (C) 2020 Samuele
#
# This file is part of markdown_parser.
#
# markdown_parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# markdown_parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with markdown_parser.  If not, see <http://www.gnu.org/licenses/>.
from .states import *


class StateManager:
    def __init__(self):
        super().__init__()
        self.state_bind = {
            "line_start": lambda: NewLineState(),
            "header": lambda: HeaderState(),
            "bold": lambda: BoldState(),
            "text": lambda: TextState(),
            "enum": lambda: EnumState(),
            "bold_or_enum": lambda: BoldOrEnumState()
        }

    def get_root(self, document_node):
        return NewLineState(document_node)

    def get(self, name):
        return self.state_bind[name]
