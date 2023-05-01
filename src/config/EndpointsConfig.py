import dataclasses


@dataclasses.dataclass
class RunTaskConfig:
    prefix: str = '/api/v1/run_task'


@dataclasses.dataclass
class GetOutputConfig:
    prefix: str = '/api/v1/get_output'


@dataclasses.dataclass
class EndpointsConfig:
    run_task_config: RunTaskConfig = RunTaskConfig()
    get_output_config: GetOutputConfig = GetOutputConfig()
