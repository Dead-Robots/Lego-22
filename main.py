#!/usr/local/bin/python3.10 -u
import actions as a
import drive as d
from kipr import msleep


def main():
    a.init()
    d.pivot(30, 90, "l")
    # d.drive_straight_1(75, 68)
    # a.get_rings(0, 15)
    # a.deliver_rings()
    # a.get_rings(50, 5500)
    # a.deliver_rings()
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
