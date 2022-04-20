from kipr import msleep, enable_servos, disable_servos
from time import time
import constants as c
import utilities as u
import drive
import servo


start_time = 0


def init():
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
    drive.distance_straight(-80, 5)
    servo.move(c.WRIST, c.WRIST_PICK_UP_1)
    u.wait_for_button()
    drive.distance_straight(60, 7)
    drive.distance_straight(30, 1)
    u.wait_for_button()
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 25)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)


def deliver_rings_1():
    drive.pivot(-50, 5, "r")
    msleep(500)
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
    drive.distance_straight(-70, 8)
    servo.move(c.WRIST, c.WRIST_START)
    servo.move(c.ARM, 200)
    drive.pivot(-50, 10, "r")
    drive.distance_straight(70, 12, False)
    drive.until_line(70)
    servo.move(c.WRIST, c.WRIST_PICK_UP_2)
    servo.move(c.ARM, c.ARM_PICK_UP_2)
    drive.pivot(70, 2, "r")


def get_rings_2():
    drive.distance_straight(60, 6)  # 5
    servo.move(c.ARM, c.ARM_UP_MAX, 10)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)


def deliver_rings_2():
    drive.pivot(-50, 18, "r")  # 24
    drive.distance_straight(-80, 12, False)
    drive.until_line(-80)
    drive.distance_straight(-80, 9)
    drive.pivot(-50, 10, "l")
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 + 75)
    msleep(500)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1)
    msleep(250)
    drive.distance_straight(40, 13)
    servo.move(c.ARM, c.ARM_PRE_PUSH)
    servo.move(c.WRIST, c.WRIST_PUSH)


def shutdown():
    print("run time:", time() - start_time)
    print("Shutting down")
    disable_servos()
