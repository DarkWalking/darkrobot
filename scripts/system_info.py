#!/usr/bin/env python3

import rospy
import platform
import subprocess
from gpiozero import CPUTemperature


def getInfo():
    try:
        cpu = CPUTemperature()
        return cpu.temperature

    except Exception as ex:
        rospy.logerr(ex)
    finally:
        return cpu.temperature


def run():
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        temp = getInfo()
        rospy.loginfo("cpu: %s", temp)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node("SystemInfo")
    rospy.loginfo("Inciando bo de informaçoes do sistema")
    run()