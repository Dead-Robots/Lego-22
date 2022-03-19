import drive
from drive import drive_straight, pivot, spin, drive, freeze_bot, drive_diagonal
import constants as c
from elevator import move_timed
from kipr import motor, freeze, ao, msleep, motor_power, get_motor_position_counter, clear_motor_position_counter, \
    enable_servos, disable_servos, push_button
import servos as s


def init():
    print("Starting up")
    enable_servos()
    # drive_straight(30, 5)
    # right_pivot(30, 1000)


def start_position():
    print("moving to start position")
    s.move_servo(c.ARM, c.ARM_TO_RIGHT)
    msleep(100)
    s.move_servo(c.WRIST, c.WRIST_PARALLEL)
    msleep(100)
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
    # lift elevator to height
    # position elevator at height 0 level to pick up top 3 rings
    drive_straight(50, distance)  # drive forward
    msleep(500)
    drive_straight(-50, distance)
    # move_elevator_up(35, height)


def deliver_rings():
    s.move_servo(c.ARM, 650)  # moves arm so it doesn't hit the side pvc pipe
    msleep(100)
    drive_straight(-70, 29)
    # can use to gyro to go until bump instead
    s.move_servo(c.ARM, c.ARM_TO_LEFT)
    s.move_servo(c.WRIST, c.WRIST_TO_LEFT)
    # move forward to place rings on tube
    drive_straight(70, 6)
    msleep(500)
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


def move_wrist_left(position):
    s.move_servo(c.WRIST, position)
    freeze(c.WRIST)


def move_elevator_down(power, height):
    position = get_motor_position_counter(c.ELEVATOR)
    while position > height:
        print(position)
        motor_power(c.ELEVATOR, -power)
        position = get_motor_position_counter(c.ELEVATOR)
    freeze(c.ELEVATOR)


def move_elevator_up(power, height):
    position = get_motor_position_counter(c.ELEVATOR)
    while position < height:
        print(position)
        motor_power(c.ELEVATOR, power)
        position = get_motor_position_counter(c.ELEVATOR)
    freeze(c.ELEVATOR)


def elevator_up():
    move_timed(c.ELEVATOR, 50, 500)


def shutdown():
    print("Shutting down")
    disable_servos()
