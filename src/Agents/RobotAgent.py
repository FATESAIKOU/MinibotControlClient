"""
An simple agent to instantiate Minibot(Third).

@author: FATESAIKOU
@date  : 06/21/2018
"""

class RobotAgent:
    def __init__( self, api_url ):
        self.__api_url = api_url;

    def GetUrl( self ):
        return self.__api_url;

