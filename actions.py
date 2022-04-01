import kipr

import drive
from drive import drive_straight, pivot, spin, drive, freeze_bot, drive_until_line, drive_drift_to_left
import constants as c
from elevator import move_timed
from kipr import motor, freeze, ao, msleep, motor_power, get_servo_position, set_servo_position, \
    get_motor_position_counter, clear_motor_position_counter, \
    enable_servos, disable_servos, push_button, digital
import servo


def init():
    print("Starting up")
    enable_servos()
    # test everything
    servo.move(c.ARM, c.ARM_START)
    servo.move(c.WRIST, c.WRIST_START)
    print("push button to continue")
    while not kipr.push_button():
        pass
    msleep(500)
    drive_straight(-50, 5)
    servo.start_servos_parallel()


def test_servo():
    print("testing servos")
    servo.set_servo_position(c.ARM, 0)
    msleep(1000)
    servo.move(c.ARM, 1002)
    msleep(1000)
    servo.move(c.ARM, 7)
    print("done")


def start_position():  # not being used, delete
    print("testing servos")
    s.move_servo(30)
    msleep(100)
    s.move_servo(c.WRIST, c.WRIST_TO_LEFT)
    msleep(100)
    s.move_servo(c.WRIST, c.WRIST_PARALLEL)
    msleep(100)
    s.move_servo(c.ARM, c.ARM_TO_LEFT)
    msleep(100)
    s.move_servo(c.ARM, c.ARM_TO_MIDDLE)
    msleep(100)
    s.move_servo(c.ARM, c.ARM_TO_RIGHT)
    msleep(100)
    print("Push button to move to start position")
    while not push_button():
        pass
    while push_button():
        pass
    print("moving to start position")
    s.move_servo(c.ARM, c.ARM_TO_RIGHT)
    msleep(100)
    s.move_servo(c.WRIST, c.WRIST_PARALLEL)
    msleep(100)
    move_elevator_zero(30)
    print("Push button to continue")
    while not push_button():
        pass
    msleep(500)


def debug():
    disable_servos()
    freeze(c.RMOTOR)
    freeze(c.LMOTOR)
    freeze(c.ELEVATOR)
    msleep(500)
    exit(0)


def get_rings(arm_height_for_rings):
    servo.move_servos_parallel(arm_height_for_rings)
    msleep(100)
    drive_straight(50, 8)
    print("this is my wrist position")
    print(get_servo_position(c.WRIST))
    servo.move(c.WRIST, (get_servo_position(c.WRIST) - 200))
    print(get_servo_position(c.WRIST))
    servo.move_servos_parallel_with_drive(c.ARM_UP_MAX)


def get_rings_2(arm_height_for_rings):
    servo.move_servos_parallel(arm_height_for_rings)
    servo.move(c.WRIST, 70) # tilt down
    msleep(1000)
    drive_straight(50, 8)
    servo.move(c.WRIST, 0) # tilt up
    servo.move_servos_parallel(c.ARM_GET_RINGS_1)
    servo.move(c.WRIST, get_servo_position(c.WRIST)- 200)
    servo.move_servos_parallel_with_drive(c.ARM_UP_MAX)


def deliver_rings():
    drive_straight(-50, 12)
    drive_until_line(-50)
    drive_straight(-50, 1)
    parallel_parking()
    pivot(-50, 105, "r")
    servo.move_servos_parallel(c.ARM_DELIVER_RINGS)
    drive_straight(-50, 1)
    servo.move_servos_parallel_with_drive(c.ARM_MIDDLE)
    drive_straight(-50, 6)


def parallel_parking():
    pivot(-50, 20, "l")
    drive_straight(-50, 6)
    pivot(50, 15, "l")
    drive_straight(50, 11)
    pivot(-50, 8, "l")
    drive_until_line(-50)


def return_to_rings():
    pivot(50, 20, "r")
    servo.move(c.ARM, c.ARM_UP_MAX)
    servo.move(c.WRIST, c.WRIST_FOR_ARM_UP_MAX)
    drive_straight(60, 16)
    pivot(-50, 78, "l")
    drive_straight(50, 3)
    drive_until_line(50)
    parallel_parking()
    drive_straight(-50, 3)
    print("moving arm down")
    servo.move_servos_parallel(c.ARM_GET_RINGS_2)
    msleep(1000)
    drive_until_line(50)
    get_rings_2(c.ARM_GET_RINGS_2)


def shutdown():
    print("Shutting down")
    disable_servos()
