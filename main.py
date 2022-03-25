#!/usr/local/bin/python3.10 -u
import actions as a
import drive as d
from kipr import msleep, push_button


def main():
    a.init()
    a.test_servo()
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
