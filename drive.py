from kipr import msleep, motor_power, analog_et, get_motor_position_counter, \
    clear_motor_position_counter, gyro_z
from time import time
import constants as c
import utilities as u

# clockwise is positive
gyro_offset = 0


def calibrate_gyro():
    global gyro_offset
    s = 0
    for _ in range(100):
        s += gyro_z()
        msleep(10)
    gyro_offset = s / 100


def get_gyro():
    return gyro_z() - gyro_offset


def blind(l_speed: int, r_speed: int):
    motor_power(c.RIGHT_MOTOR, r_speed)
    motor_power(c.LEFT_MOTOR, l_speed)


def time_straight(power, drive_time, freeze=True):
    """
    :param power: range -100 to 100
    :param drive_time: milliseconds
    :param freeze: True stops motors at end
    """
    end_time = time() + (drive_time / 1000)
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    blind(power, power)

    p = 0.25
    i = 0.04
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    while time() < end_time:
        clear_motor_position_counter(c.LEFT_MOTOR)
        clear_motor_position_counter(c.RIGHT_MOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LEFT_MOTOR))  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR))
        total_left += l_position
        total_right += r_position
        p_error = (r_position * c.F - l_position)
        i_error = total_right * c.F - total_left
        if power > 0:
            l_speed += int(p * p_error + i * i_error)
            r_speed -= int(p * p_error + i * i_error)
        else:
            l_speed -= int(p * p_error + i * i_error)
            r_speed += int(p * p_error + i * i_error)
        blind(l_speed, r_speed)

    if freeze:
        u.freeze_bot()
    else:
        pass


def distance_straight(power, inches, freeze=True, bias=0):
    """
    :param power: range -100 to 100
    :param inches: inches
    :param freeze: True stops motors at end
    """
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    blind(power, power)
    distance = inches * 180.0

    F = c.F + bias

    p = 0.25
    i = 0.04
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    while (total_left + total_right) / 2 < distance:
        clear_motor_position_counter(c.LEFT_MOTOR)
        clear_motor_position_counter(c.RIGHT_MOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LEFT_MOTOR))  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR))
        total_left += l_position
        total_right += r_position
        p_error = (r_position * F - l_position)
        i_error = total_right * F - total_left
        if power > 0:
            l_speed += int(p * p_error + i * i_error)
            r_speed -= int(p * p_error + i * i_error)
        else:
            l_speed -= int(p * p_error + i * i_error)
            r_speed += int(p * p_error + i * i_error)
        blind(l_speed, r_speed)

    if freeze:
        u.freeze_bot()
    else:
        pass


def until_line(power, sensor=c.BACK_TOPHAT, freeze=True, bias=0):
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    blind(power, power)

    p = 0.25
    i = 0.04
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0
    F = c.F + bias

    if power > 0:
        while analog_et(sensor) < c.BLACK:
            clear_motor_position_counter(c.LEFT_MOTOR)
            clear_motor_position_counter(c.RIGHT_MOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LEFT_MOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            l_speed += int(p * p_error + i * i_error)
            r_speed -= int(p * p_error + i * i_error)
            blind(l_speed, r_speed)

    else:
        while analog_et(sensor) < c.BLACK:
            clear_motor_position_counter(c.LEFT_MOTOR)
            clear_motor_position_counter(c.RIGHT_MOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LEFT_MOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            # print(l_position, r_position, p_error)
            # print(total_left, total_right)
            l_speed -= int(p * p_error + i * i_error)
            r_speed += int(p * p_error + i * i_error)
            # print(l_speed, r_speed)
            blind(l_speed, r_speed)
    if freeze:
        u.freeze_bot()


def pivot(power, angle, stationary_wheel):
    """
    :param power: range -100 to 100
    :param angle: degrees
    :param stationary_wheel: "l" for left or "r" for right
    """
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    arc_length = (angle * 12 * c.PI) * 180 / 360
    print("arc length", arc_length)

    speed = power
    total_left = 0
    total_right = 0

    while total_right < arc_length and total_left < arc_length:
        clear_motor_position_counter(c.LEFT_MOTOR)
        clear_motor_position_counter(c.RIGHT_MOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LEFT_MOTOR))  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR))
        total_left += l_position
        total_right += r_position
        if stationary_wheel == "l":
            blind(0, speed)
        if stationary_wheel == "r":
            blind(speed, 0)

    u.freeze_bot()


def gyro_pivot(speed, angle, non_moving_tire):
    a = 0
    pt = time()
    if non_moving_tire == "r":
        blind(speed, 0)
    else:
        blind(0, speed)
    while abs(a) < abs(angle):
        now = time()
        dt = now - pt
        a += abs(get_gyro()) * dt / 8
        pt = now

    u.freeze_bot()


def gyro_pivot_precise(speed, angle, non_moving_tire):
    a = 0
    pt = time()
    if non_moving_tire == "r":
        blind(speed, 0)
    else:
        blind(0, speed)
    while abs(a) < abs(angle):
        now = time()
        dt = now - pt
        a += abs(get_gyro()) * dt / 8
        pt = now

    u.freeze_bot()

    end = time() + 1

    while time() < end:
        now = time()
        dt = now - pt
        a += abs(get_gyro()) * dt / 8
        pt = now

    while abs(a) > abs(angle): # new code
        print("in second loop", a)
        pt = time()
        if non_moving_tire == "r":
            blind(-speed, 0)
            print("drivin")
        else:
            blind(0, -speed)
        now = time()
        dt = now - pt
        a -= abs(get_gyro()) * dt / 8
        pt = now
    u.freeze_bot()


def self_test():
    print("testing motors")
    distance_straight(80, 5)
    msleep(250)
    distance_straight(-80, 5)
    msleep(250)
    gyro_pivot(-80, 45, "l")
    msleep(250)
    gyro_pivot(-80, 45, "r")
    msleep(250)
    until_line(-80, c.FRONT_TOPHAT)
    msleep(250)
    until_line(80, c.BACK_TOPHAT)
    msleep(250)
    print("done testing motors")
