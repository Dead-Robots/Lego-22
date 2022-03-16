#!/usr/local/bin/python3.10 -u
import actions as a
import drive as d
from kipr import msleep


def main():
    a.init()
    # a.get_rings(10.5, 1750)
    # a.move_wrist_left(1135, 30)
    # d.drive_straight(-50, 4)
    # d.pivot(-75, 90, "l")
    # d.pivot(-75, 90, "r")
    # d.spin(50, 90)
    # d.drive_straight(75, 48)
    # a.get_rings(0, 15)
    a.deliver_rings()
    msleep(500)
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
