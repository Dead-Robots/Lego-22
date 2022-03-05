from drive import drive_straight, right_pivot, left_pivot, spin
import constants as c
from elevator import move_timed


def init():
    print("Starting up")


def get_rings(height, distance):
    # position elevator at height
    drive_straight(75, distance)  # drive forward
    # lift elevator -height


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
