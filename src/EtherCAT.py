"""
An simple agent to structurize EtherCAT net.

@author: FATESAIKOU
@date  : 06/21/2018
"""

from Agents.RobotAgent import RobotAgent

class EtherCAT:
    def __init__( self, base_url ):
        self.__base_url = base_url
        """ Need some check """

        self.__robot_dict = {}


    def GetRobot( self, robot_id ):
        if robot_id not in self.__robot_dict.keys():
            robot_url = self.__base_url + '/robot/' + str(robot_id)
            robot_agent = RobotAgent(robot_url)

            if not robot_agent.is_constructed:
                return None
            
            self.__robot_dict[robot_id] = robot_agent

        return self.__robot_dict[robot_id]
