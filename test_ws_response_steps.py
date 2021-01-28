import re
from robot.api.deco import keyword
from irest_library import irest_library
from robot.libraries.BuiltIn import BuiltIn

class test_ws_response_steps(irest_library):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        super(test_ws_response_steps,self).__init__()
    
    def setup_suite(self):
        # Get Input Variables
        resp_json = None
        self.session_url = self.get_variable_from_robot('session_url')
        if not self.session_url:
            BuiltIn().fail("Session URL is not provided")

        self.session_name = self.get_variable_from_robot('session_name')
        if not self.session_name:
            partial_name = str(self.get_current_epoch_time())
            self.session_name = "session_" + partial_name

        self.user_name = self.get_variable_from_robot('user_name')
        self.password = self.get_variable_from_robot('password')

        # Create Session
        self.session_name = self.establish_session(self.session_url, self.session_name, self.user_name, self.password)
        if not self.session_name:
            BuiltIn().fail("Failed to establish session with URL: " + self.session_url)
        
        # Get API response
        self.resp_code, self.resp_json = self.get_response(self.session_name, None)
        

    @keyword(name="Validate if response status code is ${code}")
    def status_code(self, code):
        if int(str(code)[:1]) != int(str(self.resp_code)[:1]):
            BuiltIn().fail("Test to Validate Response Status Code Failed. Expedted " + code + ". Got " + str(self.resp_code))

    def get_json_response_robot_variable(self):
        self.set_variable_to_robot("resp_json", self.resp_json)


    
    
        

    