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
    # test everything
    servo.move(c.ARM, c.ARM_START)
    servo.move(c.WRIST, c.WRIST_START)
    print("push button to continue")
    while not kipr.push_button():
        pass
    global start_time
    start_time = time()
    msleep(500)
    drive_straight(-70, 5)
    servo.start_servos_parallel()


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
    freeze(c.ELEVATOR)
    msleep(500)
    exit(0)


def get_rings_1():
    servo.move_servos_parallel(c.ARM_GET_RINGS_1)
    msleep(100)
    drive_straight(50, 8)
    servo.move(c.WRIST, (get_servo_position(c.WRIST) - 200))
    servo.move_servos_parallel_with_drive(c.ARM_UP_MAX)


def get_rings_2():
    servo.move_servos_parallel(c.ARM_GET_RINGS_2)
    servo.move(c.WRIST, 70)  # tilt down
    drive_straight(60, 5)
    servo.move(c.WRIST, 0)  # tilt up
    servo.move_servos_parallel(c.ARM_GET_RINGS_1)
    servo.move(c.WRIST, get_servo_position(c.WRIST) - 200)
    servo.move_servos_parallel_with_drive(c.ARM_UP_MAX)


def deliver_rings():
    pivot(-50, 20, "l")
    drive_straight(-80, 12, False)
    drive_until_line(-80)
    # parallel_parking()
    pivot(-50, 105, "r")
    servo.move_servos_parallel(c.ARM_DELIVER_RINGS)
    drive_straight(-70, 1)
    servo.move_servos_parallel_with_drive(c.ARM_MIDDLE)
    drive_straight(-70, 6)


def deliver_rings_2():
    pivot(-60, 20, "l")
    drive_straight(-80, 12, False)
    drive_until_line(-80)
    drive_straight(-70, 1)
    # parallel_parking()
    pivot(-50, 92, "r")  # 93 last time
    servo.move_servos_parallel(c.ARM_DELIVER_RINGS)
    drive_straight(-50, 2.5)
    servo.move_servos_parallel_with_drive(c.ARM_MIDDLE)
    drive_straight(-70, 6)


def return_to_rings():
    pivot(70, 20, "r")
    servo.move(c.ARM, c.ARM_UP_MAX)
    servo.move(c.WRIST, c.WRIST_FOR_ARM_UP_MAX)
    drive_straight(75, 16)
    pivot(-60, 76, "l")  # previously was 78
    drive_straight(60, 3, False)
    drive_until_line(70)
    # parallel_parking()
    drive_straight(-70, 3)
    print("moving arm down")
    servo.move_servos_parallel(c.ARM_GET_RINGS_2)
    drive_until_line(70)


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
