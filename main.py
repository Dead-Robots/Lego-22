#!/usr/local/bin/python3.10 -u
import actions as a
import drive as d
from kipr import msleep, push_button


def main():
    a.init()
    a.start_position()
    msleep(500)
    a.get_rings(2, 0)
    a.debug()
    msleep(500)
    a.deliver_rings()
    msleep(500)
    a.return_to_rings(2)
    msleep(500)
    a.deliver_rings()
    msleep(500)
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
