from kipr import msleep, enable_servos, disable_servos, analog_et
from time import time
import constants as c
import utilities as u
import drive
import servo


start_time = 0


def power_on_self_test():
    print("power on self test")
    if c.IS_PRIME:
        print("I am prime")
    else:
        print("I am clone")
    enable_servos()
    servo.move(c.ARM, c.ARM_MID)
    drive.self_test()
    servo.self_test()
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 60)
    u.wait_for_button()


def init():
    print("starting up :)")
    enable_servos()
    servo.move(c.WRIST, c.WRIST_START)
    servo.move(c.ARM, c.ARM_PICK_UP_1)
    u.calibrate(c.START_LIGHT)
    u.wait_4(c.START_LIGHT)
    # u.wait_for_button()  # wait for light
    global start_time
    start_time = time()


def get_rings_1():
    print("get rings 1")
    drive.until_line(-50, c.FRONT_TOPHAT)
    if c.IS_PRIME:
        drive.pivot(50, 19, "l")
    else:
        drive.pivot(50, 18, "l")
    drive.until_line(50)
    servo.move(c.WRIST, c.WRIST_PICK_UP_1)
    drive.pivot(-50, 13, "l")
    drive.distance_straight(60, 4)
    drive.distance_straight(30, 1)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 20)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)
    msleep(250)


def deliver_rings_1():
    print("deliver rings 1")
    drive.distance_straight(-80, 12, False)
    drive.pivot(50, 5, "l")
    drive.until_line(-50)
    drive.distance_straight(-80, 9)
    drive.pivot(50, 5, "l")
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 150)
    msleep(500)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 + 100)
    # servo.move(c.ARM, c.ARM_DELIVER_RINGS_1)
    drive.distance_straight(40, 5)
    # if not c.IS_PRIME:
    #     drive.pivot(50, 3, "l")
    drive.distance_straight(40, 8)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 + 30)
    servo.move(c.ARM, c.ARM_PRE_PUSH)
    servo.move(c.WRIST, c.WRIST_PUSH)


def return_to_rings():
    print("return to rings")
    drive.distance_straight(-60, 10)
    servo.move(c.ARM, c.ARM_UP_MAX)
    servo.move(c.WRIST, c.WRIST_UP)
    drive.distance_straight(60, 12)
    drive.until_line(50, c.FRONT_TOPHAT)  # straightens out in case the wheel gets caught
    drive.pivot(50, 5, "l")
    drive.until_line(50)
    servo.move(c.WRIST, c.WRIST_PICK_UP_2)
    servo.move(c.ARM, c.ARM_PICK_UP_2)


def get_rings_2():
    print("get rings 2")
    drive.pivot(-50, 15, "l")
    drive.distance_straight(60, 6)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 25)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP_MAX)
    servo.move(c.ARM, c.ARM_UP_MAX + 50, 10)
    msleep(250)


def deliver_rings_2():
    print("deliver rings 2")
    drive.distance_straight(-80, 12, False)
    drive.pivot(50, 5, "l")
    drive.until_line(-50)
    drive.distance_straight(-80, 9)
    drive.pivot(50, 5, "l")
    servo.move(c.ARM, 660)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_UP - 60)
    msleep(250)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 70)  # TRY DECREASING THIS VALUE NEXT TIME (HIGHER)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 - 60)  # was 150
    msleep(250)
    drive.distance_straight(40, 13)
    servo.move(c.ARM, c.ARM_PRE_PUSH)
    servo.move(c.WRIST, c.WRIST_PUSH)


def shutdown():
    print("run time:", time() - start_time)
    print("Shutting down")
    disable_servos()
