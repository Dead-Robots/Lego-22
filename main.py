#!/usr/local/bin/python3.10 -u
import actions as a


def main():
    a.init()
    a.get_rings_1()
    a.deliver_rings_1()
    a.return_to_rings()
    a.get_rings_2()
    a.deliver_rings_2()
    a.shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
