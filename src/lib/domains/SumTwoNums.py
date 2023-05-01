from src.lib.interfaces import IAbstractTask

import dataclasses
import logging
import sys


@dataclasses.dataclass
class SumTwoNums(IAbstractTask):

    def __init__(self):
        super().__init__()
        self.first: int = 0
        self.sec: int = 0

        self.logger = logging.getLogger(__name__)

    def initialize(self, params) -> bool:
        self.first = params['first']
        self.sec = params['second']

        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        self.logger.addHandler(handler)

        if self.uuid:
            self.res['uuid'] = self.uuid
            return True
        else:
            return False

    def run(self):
        try:
            self.res['res'] = self.first + self.sec
            self.logger.info(f'Task finished: {self.uuid}')
        except ValueError as e:
            self.logger.exception(f'Error: {self.uuid}: {e}')
        return self.res
