#!/usr/bin/env python3

import time
import sys
import os

sys.path.insert(0, '../src')

from EtherCAT import EtherCAT
from pprint import pprint

def main():
    ethercat = EtherCAT('http://140.116.78.232:5000/api')
    robot_agent = ethercat.GetRobot(0)
    camera_agent = ethercat.GetCamera(0)

    i = 0
    while True:
        time.sleep(5)
        i += 1
        os.system('clear')
        pprint(robot_agent.GetStatus(fresh=True))
        if i == 10:
            i = 0
            camera_agent.SaveImg('wtf.png')

if __name__ == '__main__':
    main()
