from src.lib.interfaces import IAbstractTask

import dataclasses
import openai
import logging
import sys


@dataclasses.dataclass
class GPTQuery(IAbstractTask):

    def __init__(self):
        super().__init__()
        self.question: str = ''

        self.logger = logging.getLogger(__name__)

    def initialize(self, params) -> bool:
        self.question = params['question']
        openai.api_key = params['api_key']

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
            self.res['res'] = openai.Completion.create(
                engine="text-davinci-003",
                prompt=self.question,
                temperature=0.6,
                max_tokens=150).choices[0].text
        except openai.error.APIError:
            self.logger.exception('OpenAI API returned an API Error')
        except openai.error.APIConnectionError:
            self.logger.exception('Failed to connect to OpenAI API')
        except openai.error.RateLimitError:
            self.logger.exception('OpenAI API request exceeded rate limit')
        self.logger.info(f'Task finished: {self.uuid}')
        return self.res
