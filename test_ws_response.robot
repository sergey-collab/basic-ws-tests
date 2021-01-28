*** Settings ***
Library               JSONLibrary
Library               Collections
Library               test_ws_response_steps.py
Suite Setup           Setup Suite

*** Comments ***
How to Run:
...   robot -V <test_variables.yaml> -v <variable> -b <debug_file> -t <test_name> test_suite.robot

*** Test Cases ***

Test to Validate Response Status
    Validate if response status code is ${response_code}

Test to Validate Dictionary has Keys
    Get Json Response Robot Variable
    :FOR  ${elem}  IN  @{dict_obj_keys}
    \  Check Each Dictionary  ${elem} 

Test to Validate Unique IDs
    @{id_lst}=  Create List
    Get Json Response Robot Variable
    :FOR  ${each_elem}  IN  @{resp_json}
    \  ${elem_id}=  Get Value From Json  ${each_elem}  $..id
    \  Append To List  ${id_lst}  ${elem_id[0]}
    List Should Not Contain Duplicates  ${id_lst}

Test to Check on Unique User Hits
    @{user_lst}=  Create List
    Get Json Response Robot Variable
    :FOR  ${each_elem}  IN  @{resp_json}
    \  ${elem}=  Get Value From Json  ${each_elem}  $..userId
    \  Append To List  ${user_lst}  ${elem[0]}
    :FOR  ${each_elem}  IN  @{user_lst}
    \  Run Keyword And Continue On Failure  
       ...  Should Contain X Times  ${user_lst}  ${each_elem}  ${user_hits}  ignore_case=True

Test to tag JSON Object Items
    Get Json Response Robot Variable
    ${has_msg}=	Create Dictionary	has_msg=${True}
    ${has_no_msg}=	Create Dictionary	has_msg=${False}
    :FOR  ${each_elem}  IN  @{resp_json}
    \  ${elem_body}=  Get Value From Json  ${each_elem}  $..body
    \  ${contains}=  Evaluate   """${custom_msg}""" in """${elem_body}"""
    \  Run Keyword if  ${contains} == ${True}
       ...  Add Object To Json  ${each_elem}  $  ${has_msg}
       ...  ELSE
       ...  Add Object To Json  ${each_elem}  $  ${has_no_msg}
    ${elem}=  Set Variable  has_msg
    Check Each Dictionary  ${elem}

*** Keywords ***

Check Each Dictionary
    [Arguments]    ${elem}
    :FOR  ${each_elem}  IN  @{resp_json}
    \  Run Keyword And Continue On Failure
       ...  Dictionary Should Contain Key  ${each_elem}  ${elem}

