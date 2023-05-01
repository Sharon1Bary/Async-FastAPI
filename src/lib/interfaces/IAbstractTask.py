from abc import ABC, abstractmethod

import uuid


class IAbstractTask(ABC):

    def __init__(self):
        self.uuid: uuid = uuid.uuid4()
        self.res: dict = {}

    @abstractmethod
    def initialize(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def run(self, **kwargs):
        pass
