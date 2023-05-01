# Tasker Service Introduction:

Tasker is an exported asynchronous REST API service.

Once a new task is created, the API returns immediately the UUID and continue the Task on the Background. (fastapi.BackgroundTasks)

Tasker give us the ability to make the following requests:

1. Sum two numbers - Sum the two numbers provided.

2. Query ChatGPT - Ask GPT questions. (openai)

3. Query Ethereum Blockchain - Query Ethereum Blockchain liquidity pool based on a Smart Contract provided to get all the Balances and Tokens (erc20) of the contract. (Web3, Moralis and Defi)


## Endpoints: 
#### RunTask(task_name: str, params: dict) - return the UUID of the task. 
* task_name - Identify the task that should be run, can be one of the following:
1. sum_tow_nums
2. ask_gpt
3. blockchain_query
* params - Is the params of the task. (Please see Examples below).

#### GetTaskOutput(UUID: string) - returns the result of the task based on the UUID provided.
* Task UUID


## Examples: 
### RunTask(task_name: str, params: dict)

### sum_two_nums:
* task_name = sum_tow_nums 
* params = {"first": 2, "second": 2}
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/run_task?Task%20Name=sum_tow_nums&Add%20the%20params=%7B%22first%22%3A%202%2C%20%22second%22%3A%202%7D' \
  -H 'accept: application/json'
```
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/run_task?Task%20Name=sum_tow_nums&Add%20the%20params=%7B%22first%22%3A%202%2C%20%22second%22%3A%202%7D' \
  -H 'accept: application/json'
```
### ask_gpt:
* task_name = ask_gpt
* params = {"question": "Hello, tell me a nice story","api_key": "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"}

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/run_task?Task%20Name=ask_gpt&Add%20the%20params=%7B%22question%22%3A%20%22Hello%2C%20tell%20me%20a%20nice%20story%22%2C%22api_key%22%3A%20%22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%22%7D' \
  -H 'accept: application/json'
```
* To get ChatGPT Token please sign  here - https://platform.openai.com/
* Then get your api key - https://platform.openai.com/account/api-keys


### blockchain_query:

* task_name = blockchain_query
* params = {"params": {"address": "0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11", "chain": "eth"}, "api_key": "CHB8kMsmbtK2t7voBh1ZT8UQoODIemiDsdjp44bA0SCymhLU6q57c6cvP38dy6dP"}

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/run_task?Task%20Name=blockchain_query&Add%20the%20params=%7B%22params%22%3A%20%7B%22address%22%3A%20%220xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11%22%2C%20%22chain%22%3A%20%22eth%22%7D%2C%20%22api_key%22%3A%20%22CHB8kMsmbtK2t7voBh1ZT8UQoODIemiDsdjp44bA0SCymhLU6q57c6cvP38dy6dP%22%7D' \
  -H 'accept: application/json'
```
* To get Moralis Token please sign  here - https://admin.moralis.io/login
* Then create your on api key - https://docs.moralis.io/web3-data-api/evm/get-your-api-key

### GetTaskOutput(UUID: str)
* UUID - The UUID returns by RunTask(task_name: str, params: dict) endpoint.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/get_output?UUID=88c6d748-03c6-41e7-8be9-f3f2ad7fe45b' \
  -H 'accept: application/json'
```


## Installation

* Use python 3.8 version. https://www.python.org/downloads/release/python-380/

* Use Docker. https://docs.docker.com/language/python/build-images/


```bash
# Build the Image
docker build -t tasker-fast-api

# Run the Docker
docker run tasker-fast-api
```
* src.apps.Tasker.py can be run also using python IDE. (The service)


## Fast-API Swagger
To open the Swagger go to  http://127.0.0.1:8000/docs#/

## Notes

* src.lib.exception_handler.Exceptions.py need to be created to give our own Exceptions.
* More test should be written.
* DB should be connected.
### The Tokens provided in the Examples sections are for Test only.




