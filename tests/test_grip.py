#!/usr/bin/env python3

import json
import sys

sys.path.insert(0, '../src')

from EtherCAT import EtherCAT
from pprint import pprint


def GetRobotReady(robot_agent):
    if robot_agent.GetStatus()['state'] != 'GROUP_STAND_STILL':
        robot_agent.Exec('Reset')
        robot_agent.Exec('Enable')

    robot_agent.Exec('AcsPTP', [0, 90, 0, 0, -90, -15])
    robot_agent.Exec('HomeGripper')
    robot_agent.Exec('Wait', 576, 100)
    robot_agent.Exec('WaitGripper', 100)


def main():
    ethercat = EtherCAT('http://140.116.78.232:5000/api')
    robot_agent = ethercat.GetRobot(0)

    GetRobotReady(robot_agent)

    for i in range(1000):
        status_str = json.dumps(robot_agent.GetStatus()['status'])
        print('Round: ' + str(i) + ' Status: ' + status_str)
        robot_agent.Exec('AcsPTP', [0, 90, 0, -45, -90, -75])
        robot_agent.Exec('Release')
        robot_agent.Exec('Wait', 576, 100)
        robot_agent.Exec('WaitGripper', 100)

        robot_agent.Exec('AcsPTP', [0, 90, 0, 45, -90, 45])
        robot_agent.Exec('Grip', 40, 20)
        robot_agent.Exec('Wait', 576, 100)
        robot_agent.Exec('WaitGripper', 100)

    robot_agent.Exec('AcsPTP', [0, 90, 0, 0, -90, -15])
    robot_agent.Exec('Wait', 576, 100)
    robot_agent.Exec('Disable')


if __name__ == '__main__':
    main()
