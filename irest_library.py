import time
import requests
import urllib3
from urlparse import urlparse
from RequestsLibrary import RequestsLibrary
from robot.libraries.BuiltIn import BuiltIn
from requests.packages.urllib3.exceptions import (InsecureRequestWarning,InsecurePlatformWarning, SNIMissingWarning) 

class irest_library(RequestsLibrary):    
    
    def __init__(self):   
        super(irest_library,self).__init__() 
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        requests.packages.urllib3.disable_warnings(SNIMissingWarning)
        urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        urllib3.disable_warnings(urllib3.exceptions.SNIMissingWarning)

    def get_variable_from_robot(self, variablename):
        """Gets the given test variable from the list of variables declared.
        Args:
            variablename: The name of the variable

        Returns:
            None If variable is not found else returns the variable value.
        """
        try:
            return BuiltIn().get_variable_value('${'+variablename+'}')
        except Exception:
            return None

    def set_variable_to_robot(self, variablename, value):
        """Sets a value to the given test variable in the list of variables declared.

        Args:
            variablename: The name of the variable
            value: The new value to be set to the variable

        Returns:
             Assigned variable
        """
        return  BuiltIn().set_test_variable('${'+variablename+'}',value)
    
    def get_current_epoch_time(self):
        return int(time.time())

    def establish_session(self, session_url, session_name, user_name="", password=""):
        """Connect to REST API session.

        Args:
                session_url (str)             : The name URL the REST API session to be connected to.
                session_name (str)            : The name of the REST API session to be connected to.
                user_name (str/optional)      : The username of the REST API session to be connected to. By default, this takes "".
                password (str/optional)       : The password of the REST API session to be connected to. By default, this takes "".

        Return:
                session_name: Returns the session_name for which the connection was created.
        """
        auth = [user_name, password]
        try:
            if user_name == '':
                test = self.create_session(session_name, session_url)
            else:
                test = self.create_session(session_name, session_url, auth=auth)
            return  session_name
        except Exception:
            return None

    def get_response(self, session_name, url=None, params=None):
        """Gets the json response of the specified element.

        Args:
            session_name (str)            : The name of the REST API session to be connected to.
            uri (str)                     : The URL the REST API session to be connected to.
            params (str/optional)         : The additional parameters to be provided for the HTTP request object. Defaults to None.

        Returns: json response (content) and status code

        """
        resp = self.get_on_session(session_name, url=url, params=params)
        if int(resp.status_code) >= 200 and int(resp.status_code) < 300:
            return resp.status_code, resp.json()
        else:
            return resp.status_code, None
