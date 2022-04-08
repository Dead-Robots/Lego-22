import kipr

import drive
from drive import drive_straight, pivot, spin, drive, freeze_bot, drive_until_line
import constants as c
from elevator import move_timed
from kipr import motor, freeze, ao, msleep, motor_power, get_servo_position, set_servo_position, \
    get_motor_position_counter, clear_motor_position_counter, \
    enable_servos, disable_servos, push_button, digital
import servo
from time import time

start_time = 0


def init():
    print("Starting up")
    enable_servos()
    # add test everything
    servo.move(c.ARM, c.ARM_START)
    servo.move(c.WRIST, c.WRIST_START)
    print("push button to continue")
    while not kipr.push_button():
        pass
    global start_time
    start_time = time()
    msleep(500)
    drive_straight(-80, 5)
    servo.move(c.WRIST, c.WRIST_PICK_UP_1)
    servo.move(c.ARM, c.ARM_PICK_UP_1-40)


def test_servo():
    print("testing servos")
    servo.set_servo_position(c.ARM, 0)
    msleep(1000)
    servo.move(c.ARM, 1002)
    msleep(1000)
    servo.move(c.ARM, 7)
    print("done")


def debug():
    disable_servos()
    freeze(c.RMOTOR)
    freeze(c.LMOTOR)
    msleep(500)
    exit(0)


def get_rings_1():
    msleep(250)
    drive_straight(60, 8)
    servo.move(c.WRIST, c.WRIST_TILT)
    servo.move(c.ARM, c.ARM_UP_MAX)
    msleep(250)
    drive_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)


def get_rings_2():
    drive_straight(60, 6)
    servo.move(c.WRIST, c.WRIST_TILT)
    drive(-23, -25)
    servo.move(c.ARM, c.ARM_UP_MAX)
    msleep(250)
    drive_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)


def deliver_rings_1():
    pivot(-50, 15, "r")
    msleep(500)
    drive_straight(-80, 12, False)
    drive_until_line(-80)
    drive_straight(-80, 7)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS - 100)
    msleep(500)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS + 20)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS - 30)
    drive_straight(40, 11)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS + 40)
    servo.move(c.ARM, c.ARM_PRE_PUSH)
    servo.move(c.WRIST, c.WRIST_PUSH)


def deliver_rings_2():
    pivot(-50, 20, "r")
    drive_straight(-80, 12, False)
    drive_until_line(-80)
    drive_straight(-80, 5)
    pivot(-50, 10, "l")
    debug()
    # need to make rings not fly out
    servo.move(c.ARM, c.ARM_DELIVER_RINGS - 100)
    msleep(500)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS + 300)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS + 20)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS - 30)
    msleep(250)
    drive_straight(40, 13)



def return_to_rings():
    drive_straight(-70, 8)
    servo.move(c.WRIST, c.WRIST_START)
    servo.move(c.ARM, 200)
    pivot(-50, 15, "r")
    drive_straight(70, 12, False)
    drive_until_line(70)
    servo.move(c.WRIST, c.WRIST_PICK_UP_2)
    servo.move(c.ARM, c.ARM_PICK_UP_2)
    pivot(70, 14, "r")
    while not kipr.push_button():
        pass


def parallel_parking():
    pivot(-50, 20, "l")
    drive_straight(-50, 6)
    pivot(50, 15, "l")
    drive_straight(50, 9)
    pivot(-50, 8, "l")
    drive_until_line(-50)


def shutdown():
    print("run time:", time() - start_time)
    print("Shutting down")
    disable_servos()
