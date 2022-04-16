from kipr import msleep, get_servo_position, set_servo_position
import constants as c
import drive


def move(port: int, end_position: int, speed: int = 25):
    """
    For speed, 1 is very slow, and 100 is very fast
    """
    speed = abs(speed)
    current_position = get_servo_position(port)
    if current_position > end_position:
        speed = -speed
    while current_position != end_position:
        if abs(speed) > abs(end_position - current_position):
            current_position = end_position
        else:
            current_position += speed
        set_servo_position(port, current_position)
        msleep(25)


def move_servos_parallel(arm_end_position: int, speed: int = 15):
    """
    For speed, 1 is very slow, and 100 is very fast
    """
    speed = abs(speed)
    arm_current_position = get_servo_position(c.ARM)
    wrist_current_position = get_servo_position(c.WRIST)

    if arm_current_position > arm_end_position:
        speed = -speed

    while arm_current_position != arm_end_position:
        if abs(speed) > abs(arm_end_position - arm_current_position):
            arm_current_position = arm_end_position
        else:
            arm_current_position += speed
            wrist_current_position -= int(speed * 1.03)  # tilt the wrist slightly up
        set_servo_position(c.ARM, arm_current_position)
        set_servo_position(c.WRIST, wrist_current_position)
        msleep(25)


def move_servos_parallel_with_drive(arm_end_position: int, speed: int = 15):
    """
    For speed, 1 is very slow, and 100 is very fast
    """
    speed = abs(speed)
    arm_current_position = get_servo_position(c.ARM)
    wrist_current_position = get_servo_position(c.WRIST)

    if arm_current_position > arm_end_position:
        speed = -speed

    drive.blind(-23, -25)
    msleep(100)
    while arm_current_position != arm_end_position:
        if abs(speed) > abs(arm_end_position - arm_current_position):
            arm_current_position = arm_end_position
        else:
            arm_current_position += speed
            wrist_current_position -= int(speed * 1.03)  # tilt the wrist slightly up
        set_servo_position(c.ARM, arm_current_position)
        set_servo_position(c.WRIST, wrist_current_position)
        msleep(25)
