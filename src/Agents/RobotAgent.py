"""
An simple agent to instantiate Minibot(Third).

@author: FATESAIKOU
@date  : 06/21/2018
"""

import requests
import json

class RobotAgent:
    def __init__( self, api_url ):
        self.is_constructed = False
        self.SetUrl(api_url)


    """ Initialization """
    def GetUrl( self ):
        return self.__api_url;

    def SetUrl( self, api_url ):
        try:
            robot_resp = requests.get( api_url )
            self.CheckResponse(robot_resp)

            self.__api_url = api_url
            self.robot_status = json.loads(robot_resp.content)
            self.is_constructed = True
        except Exception as e:
            print('Unable to set url as "' + api_url + '"\n' + str(e))


    """ Get Status """
    def GetStatus( self, fresh = False ):
        if fresh or not hasattr(self, 'robot_status'):
            robot_resp = requests.get( self.__api_url )
            self.CheckResponse(robot_resp)

            self.robot_status = json.loads(robot_resp.content)
        
        return self.robot_status


    """ Exec """
    def Exec( self, action, *args ):
        robot_resp = requests.put(self.__api_url, json=['Robot', action, args])
        self.CheckResponse(robot_resp)

        self.robot_status = json.loads(robot_resp.content)

        return self.robot_status


    """ Utils """
    def CheckResponse( self, response ):
        if (response.status_code != 200):
            raise SystemError('Server responses with bad status code: ' + str(response.status_code))
