from kipr import msleep, enable_servos, disable_servos, analog_et
from time import time
import constants as c
import utilities as u
import drive
import servo


start_time = 0


def init():
    if c.IS_PRIME:
        print("I am prime")
    else:
        print("I am clone")
    print("starting up")
    enable_servos()
    # drive.self_test()
    # servo.self_test()
    servo.move(c.WRIST, c.WRIST_START)
    servo.move(c.ARM, c.ARM_PICK_UP_1 + 75)
    u.wait_for_button()
    global start_time
    start_time = time()


def get_rings_1():
    drive.until_line(-80, c.FRONT_TOPHAT)
    drive.pivot(50, 8, "l")
    drive.until_line(60)
    servo.move(c.WRIST, c.WRIST_PICK_UP_1)
    drive.pivot(-50, 12, "l")
    drive.distance_straight(60, 4)
    drive.distance_straight(30, 1)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 25)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)
    msleep(250)


def deliver_rings_1():
    drive.distance_straight(-80, 12, False)
    drive.until_line(-80)
    drive.distance_straight(-80, 9)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 60)
    msleep(500)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1)
    drive.distance_straight(40, 13)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 + 20)
    servo.move(c.ARM, c.ARM_PRE_PUSH)
    servo.move(c.WRIST, c.WRIST_PUSH)


def return_to_rings():
    drive.distance_straight(-60, 10)
    servo.move(c.ARM, c.ARM_UP_MAX)
    servo.move(c.WRIST, c.WRIST_UP)
    drive.distance_straight(60, 12)
    drive.until_line(70, c.FRONT_TOPHAT)  # straightens out in case the wheel gets caught
    drive.pivot(50, 5, "l")
    drive.until_line(60)
    servo.move(c.WRIST, c.WRIST_PICK_UP_2)
    servo.move(c.ARM, c.ARM_PICK_UP_2)


def get_rings_2():
    drive.pivot(-50, 12, "l")
    drive.distance_straight(60, 6)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 25)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)
    msleep(250)


def deliver_rings_2():
    drive.distance_straight(-80, 12, False)
    drive.until_line(-80)
    drive.distance_straight(-80, 9)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 + 75)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1)
    msleep(250)
    drive.distance_straight(40, 13)
    servo.move(c.ARM, c.ARM_PRE_PUSH)
    servo.move(c.WRIST, c.WRIST_PUSH)


def shutdown():
    print("run time:", time() - start_time)
    print("Shutting down")
    disable_servos()
