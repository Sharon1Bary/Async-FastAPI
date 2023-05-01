from fastapi import APIRouter, FastAPI, Query, BackgroundTasks

from src.config import EndpointsConfig
from src.lib.domains import Core

import json

# Create FastAPI
app = FastAPI(title="Tasker")

# The endpoint config (include the endpoints prefixes).
endpoint_config = EndpointsConfig()

# Create the API Routers
api_router_run_task = APIRouter()
api_router_get_task_output = APIRouter()


# Health Check endpoint
@app.get('/', status_code=200, tags=['Health Check'])
def health_check():
    return "Tasker service is up and running."


@api_router_run_task.get(endpoint_config.run_task_config.prefix, status_code=200)
async def run_task(background_tasks: BackgroundTasks,
                   name: str = Query(None, alias='Task Name'),
                   params: str = Query(None, alias='Add the params')):

    """
    run_task() is asynchronous function, meaning based on a provided Task Name and Task params
    the function execute a new Task, returns immediately the task UUID to the client and running
    the Task on the Background.

        :param name: str - identify the task should be run.
        :param params: dict - the params to execute the task.
        :param background_tasks: fastapi.BackgroundTasks - asynchronous function.
        :return: UUID
    """
    try:
        task = core.supported_classes[name]()
        logger.info(f'Task created: {task.uuid}')

        if task.initialize(params=json.loads(params)):
            background_tasks.add_task(task.run)
            core.tasks[str(task.uuid)] = task.res
        else:
            logger.error(f'There is no UUID for the task.')
        return task.uuid
    except ValueError:
        logger.exception('The input is not integer')
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


@api_router_get_task_output.get(endpoint_config.get_output_config.prefix, status_code=200)
def get_task_output(
        uuid: str = Query(None, alias='UUID')):
    """
    get_task_output() is synchronous function that returns the task results.
        :param uuid: task uuid.
        :return: res included uuid.
    """
    try:
        return core.tasks[uuid]
    except KeyError:
        logger.exception('The UUID provided is wrong')


# add the routs to the app.
app.include_router(api_router_run_task, tags=["Run Task"])
app.include_router(api_router_get_task_output, tags=["Get Task Output"])

if __name__ == "__main__":

    """
    The main is creating logger, core and activatign the fast-api using uvicorn.
    To login the swagger please go to - http://127.0.0.1:8000/docs#/
    """

    import uvicorn
    import logging
    import sys

    # Create the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(handler)

    try:
        core = Core()
        core.initialize()

        # Activate the app
        uvicorn.run(app, port=8000, host="0.0.0.0", log_level="debug")
    except Exception as e:
        logger.exception(e)
