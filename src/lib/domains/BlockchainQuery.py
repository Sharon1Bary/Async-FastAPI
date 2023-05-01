from src.lib.interfaces import IAbstractTask
from moralis import evm_api

import dataclasses
import logging
import sys


@dataclasses.dataclass
class BlockchainQuery(IAbstractTask):

    def __init__(self):
        super().__init__()
        self.params: dict = {}
        self.tokens_balances: dict = {}
        self.api_key: str = ''

        self.logger = logging.getLogger(__name__)

    def initialize(self, params) -> bool:
        self.params = params["params"]
        self.api_key = params["api_key"]

        # Create the logger
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
            for i in evm_api.token.get_wallet_token_balances(api_key=self.api_key, params=self.params):
                self.tokens_balances[i["token_address"]] = i["balance"]
            self.res['res'] = self.tokens_balances
            self.logger.info(f'Task finished: {self.uuid}')
        except Exception as e:
            self.logger.exception(f'Error: {self.uuid}: {e}')
        return self.res
