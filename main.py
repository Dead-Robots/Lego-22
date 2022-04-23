#!/usr/local/bin/python3.10 -u
import actions as a
import drive
import utilities


def main():
    a.init()
    drive.pivot(50, 360, "l") # what we want to work on next time
    utilities.debug()
    a.get_rings_1()
    a.deliver_rings_1()
    a.return_to_rings()
    a.get_rings_2()
    a.deliver_rings_2()
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
