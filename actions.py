from drive import drive_straight, pivot, spin, drive, freeze_bot
import constants as c
from elevator import move_timed
from kipr import motor, freeze, ao, msleep, motor_power, get_motor_position_counter, clear_motor_position_counter


def init():
    print("Starting up")
   # drive_straight(30, 5)
   # right_pivot(30, 1000)


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


def get_rings(distance, height):
    # lift elevator to height
    move_elevator_down(35, 0)
    # position elevator at height 0 level to pick up top 3 rings
    drive_straight(50, distance)  # drive forward
    move_elevator_up(35, height)

    freeze_bot()


def deliver_rings():
    drive_straight(-75, 6)  # back up to horizontal tube
    # turn wrist
    # turn turntable
    # move forward to place rings on tube
    # turn to free claw from tube


def elevator_up():
    move_timed(c.ELEVATOR, 50, 500)


def shutdown():
    print("Shutting down")
