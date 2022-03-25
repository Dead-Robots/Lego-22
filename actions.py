import drive
from drive import drive_straight, pivot, spin, drive, freeze_bot
import constants as c
from elevator import move_timed
from kipr import motor, freeze, ao, msleep, motor_power, get_motor_position_counter, clear_motor_position_counter, \
    enable_servos, disable_servos, push_button, digital
import servo


def init():
    print("Starting up")
    enable_servos()


def test_servo():
    print("testing servos")
    servo.set_servo_position(c.ARM, 0)
    msleep(1000)
    servo.move(c.ARM, 1002)
    msleep(1000)
    servo.move(c.ARM, 7)
    print("done")


def start_position():
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
    while push_button():
        pass
    msleep(500)


def debug():
    disable_servos()
    freeze(c.RMOTOR)
    freeze(c.LMOTOR)
    freeze(c.ELEVATOR)
    msleep(500)
    exit(0)


def get_rings(distance, height):
    drive_straight(-70, 6)
    msleep(100)
    s.move_servo(c.ARM, c.ARM_TO_MIDDLE)
    move_elevator_up(40, 1000)
    msleep(500)
    # lift elevator to height
    # position elevator at height 0 level to pick up top 3 rings
    drive_straight(50, distance)  # drive forward
    msleep(500)
    move_elevator_up(40, 4300)
    drive_straight(-50, distance)
    # move_elevator_up(35, height)


def deliver_rings():
    s.move_servo(c.ARM, c.ARM_TO_RIGHT)  # moves arm so it doesn't hit the side pvc pipe
    msleep(100)
    drive_straight(-70, 27)
    # can use to gyro to go until bump instead
    s.move_servo(c.ARM, c.ARM_TO_LEFT)
    s.move_servo(c.WRIST, c.WRIST_TO_LEFT)
    # move forward to place rings on tube
    drive_straight(70, 10)
    msleep(500)
    debug()
    drive_straight(-70, 6)
    msleep(500)
    s.move_servo(c.ARM, 650)  # moves arm so it doesn't hit the side pvc pipe
    msleep(500)


def return_to_rings(distance):
    s.move_servo(c.WRIST, c.WRIST_PARALLEL)
    msleep(100)
    drive_straight(70, 29)
    msleep(100)
    s.move_servo(c.ARM, c.ARM_TO_MIDDLE)
    drive_straight(50, distance)  # drive forward
    msleep(500)
    drive_straight(-50, distance)


def shutdown():
    print("Shutting down")
    disable_servos()
