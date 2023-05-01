from src.lib.domains import SumTwoNums, GPTQuery, BlockchainQuery

import dataclasses
import uuid


@dataclasses.dataclass
class Core:

    def __init__(self):
        self.uuid: uuid = uuid.uuid4()
        self.tasks: dict = {}
        self.supported_classes: dict = {}

    def initialize(self) -> bool:
        self.supported_classes['sum_tow_nums'] = SumTwoNums
        self.supported_classes['ask_gpt'] = GPTQuery
        self.supported_classes['blockchain_query'] = BlockchainQuery
        if self.supported_classes:
            return True
        else:
            return False
