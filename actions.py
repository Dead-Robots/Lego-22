from drive import drive_straight, right_pivot, left_pivot, spin
import constants as c


def init():
    print("Starting up")


def get_rings(height, time):
    # position elevator at height
    drive_straight(75, time)    # drive forward
    # lift elevator -height


def deliver_rings():
    drive_straight(-75, 5500)    # back up to horizontal tube
    # turn wrist
    # turn turntable
    # move forward to place rings on tube
    # turn to free claw from tube


def shutdown():
    print("Shutting down")
