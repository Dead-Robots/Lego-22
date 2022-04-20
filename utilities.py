from kipr import push_button, msleep, freeze, disable_servos
import constants as c


def freeze_bot():
    freeze(c.LEFT_MOTOR)
    freeze(c.RIGHT_MOTOR)
    msleep(500)


def wait_for_button():
    print("push button to continue")
    freeze_bot()
    while not push_button():
        pass


def debug():
    disable_servos()
    freeze(c.RIGHT_MOTOR)
    freeze(c.LEFT_MOTOR)
    msleep(500)
    exit(0)



