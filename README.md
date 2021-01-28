# Web API Robot Framework Automated Tests
## About 
Test Suite to verify Rest API Get request results from a web server.
* Test Cases can be run in sequence or individually.
* Test Steps Python module provides suite setup and test cases steps. Keyword decorator enables to write test case steps in plain English format.
* iRest Library enables code re-use of often used methods to connect to server, get response, and utilities like obtaining current time.
## Input Variables
* Yaml test file is used for config variables:
```bash
session_url - IP/URL of the web server including http or https protocol.
user_name - (optional input) username where required.  
password- (optional input) password where required.
response_code - server response code to be tested i.e. 2xx or 200.
custom_msg - custom message to be searched.
user_hits - number of each user hit at JSON object items.
dict_obj_keys - keys to validate at each JSON item.
```
## Test Cases
* Test to Validate Response Status - validates web server response status code using variable response_code
* Test to Validate Dictionary has Keys - validates each dictionary contains items with user provided keys dict_obj_keys
* Test to Validate Unique IDs - checks if all object IDs are unique
* Test to Check on Unique User Hits - validates if number of users match the criteria provided at user_hits
* Test to tag JSON Object Items - adds a (bool) item into each JSON object based on custom message to be searched.

## How to Run
Each test case uses the suite setup - connection once established to a web server. Test cases can be run in sequence or individually.
* Command:
```bash
robot <path_to_robot_test_suite>
```
* Command options:
```bash
-t <test_case> - name of individual test case
-b <debug.txt> - file to be generated for debugging purposes
-V <test_config_file> - yaml test configuration file
-v <variable> - custom variable
```
## Notes
* Python Modules Installed:
```bash
pip install robotframework-requests
pip install robotframework-jsonlibrary
```
