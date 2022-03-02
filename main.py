#!/usr/local/bin/python3.10 -u
import actions as a


def main():
    a.init()
    a.drive_straight(90, 12)
    # a.get_rings(0, 2000)
    # a.deliver_rings()
    # a.get_rings(50, 5500)
    # a.deliver_rings()
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
