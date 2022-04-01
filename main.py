#!/usr/local/bin/python3.10 -u
import actions as a
import constants as c
import drive as d
from kipr import msleep, push_button, enable_servos


def main():
    a.init()
    a.get_rings(c.ARM_GET_RINGS_1)
    a.deliver_rings()
    a.return_to_rings()
    a.deliver_rings()
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
