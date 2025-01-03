# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/lifecycle/booted.py

This script defines the Booted class.

Copyright (C) 2024-today rydnr's pythoneda-shared-runtime/lifecycle-events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import Event
from typing import List


class Booted(Event):
    """
    Represents a PythonEDA domain has booted up.

    Class name: Booted

    Responsibilities:
        - Represent a domain has booted up.

    Collaborators:
        - None
    """

    def __init__(
        self,
        defUrl: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new Booted instance.
        :param defUrl: The url of the definition repository.
        :type defUrl: str
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._def_url = defUrl
        super().__init__(previousEventIds, reconstructedId)

    @property
    def def_url(self) -> str:
        """
        Retrieves the url of the definition repository.
        :return: Such url.
        :rtype: str
        """
        return self._def_url


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
