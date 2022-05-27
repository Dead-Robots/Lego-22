from kipr import push_button, msleep, freeze, disable_servos, analog
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


def calibrate(port):
    print("Press button with light on")
    while not push_button():
        pass
    while push_button():
        pass
    light_on = analog(port)
    print("On value =", light_on)
    if light_on > 200:
        print("Bad calibration")
        return False
    msleep(1000)
    print("Press button with light off")
    while not push_button():
        pass
    while push_button():
        pass
    light_off = analog(port)
    print("Off value =", light_off)
    if light_off < 3000:
        print("Bad calibration")
        return False

    if (light_off - light_on) < 2000:
        print("Bad calibration")
        return False
    c.START_LIGHT_THRESHOLD = (light_off - light_on) / 2
    print("Good calibration! ", c.START_LIGHT_THRESHOLD)
    return True


def wait_4(port):
    print("waiting for light!! ")
    while analog(port) > c.START_LIGHT_THRESHOLD:
        pass


def wait_4_light(ignore=False):
    if ignore:
        wait_for_button()
        return
    while not calibrate(c.START_LIGHT):
        pass
    wait_4(c.START_LIGHT)