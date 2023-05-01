CONTRACT = '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11'


class APIMock:
    def __init__(self):
        self.sum = SumTwoNumsMock()
        self.gpt = GPTQueryMock()
        self.blockchain = GPTQueryMock()


class SumTwoNumsMock:
    def __init__(self):
        self.uuid = '123'

    def run(self):
        return self.uuid


class GPTQueryMock:
    def __init__(self):
        self.uuid = '123'

    def __call__(self, address, *args, **kwargs):
        return self


class BlockchainQueryMock:
    def __init__(self):
        self.uuid = '123'
        self.params = {}
        self.api_key = 'APIKEY'

    def __call__(self, address, *args, **kwargs):
        return self
