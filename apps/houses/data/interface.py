from abc import ABC, abstractmethod
from typing import final


class ReaderInterface(ABC):
    """Interface being used by all data reader"""

    def __init__(self):
        self._data = None

    @final
    @property
    def data(self):
        if self._data is None:
            raise ValueError
        return self._data

    @abstractmethod
    def read(self, *args, **kwargs):
        pass