# Copyright (C) 2017  Luca Carella

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3.0 of the License, or (at
# your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
"""Manage operators.

This module contain class for managing operator
that will be registered in blender, in future will be used also for drawing the
UI.
"""

class __OperatorManager:
    def __init__(self):
        self.__operator_list = []
        self.__ui_list = []

    def addOperator(self, operator):
        self.__operator_list.append(operator)

    def classList(self):
        return self.__operator_list

    def addUI(self, ui):
        self.__ui_list.append(ui)

    def draw(self, context, layout):
        for ui in self.__ui_list:
            ui.draw(context, layout)


om = __OperatorManager()
