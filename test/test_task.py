from test.mocks import APIMock

from src.lib.domains import SumTwoNums, GPTQuery


class TestAPITask:

    def test_run_all_tasks(self):

        task_sum = APIMock().sum
        task_sum.first = 1
        task_sum.second = 2

        SumTwoNums.run(task_sum)

        assert task_sum['res'] == 3

        task_gpt = APIMock().gpt
        task_gpt.question = 'Hello There'
        GPTQuery.run(task_gpt)

        assert task_gpt.uuid


