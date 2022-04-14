#!/usr/local/bin/python3.10 -u
from kipr import motor, freeze, ao, msleep, motor_power, analog_et, get_motor_position_counter, \
    clear_motor_position_counter
from time import time

import constants as c


# clockwise is positive


def drive(l_speed: int, r_speed: int):
    motor_power(c.RMOTOR, r_speed)
    motor_power(c.LMOTOR, l_speed)


def freeze_bot():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    msleep(500)


def drive_straight(power, inches, freeze=True): # edited for blue bot
    clear_motor_position_counter(c.LMOTOR)
    clear_motor_position_counter(c.RMOTOR)
    drive(power, power)
    steves = inches * 180.0

    F = 0.96  # CLONE: 1.02

    p = 0.25
    i = 0.04
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    if power > 0:
        while (total_left + total_right) / 2 < steves:
            clear_motor_position_counter(c.LMOTOR)
            clear_motor_position_counter(c.RMOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LMOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RMOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            l_speed += int(p * p_error + i * i_error)
            r_speed -= int(p * p_error + i * i_error)
            drive(l_speed, r_speed)

    else:
        while (total_left + total_right) / 2 < steves:
            clear_motor_position_counter(c.LMOTOR)
            clear_motor_position_counter(c.RMOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LMOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RMOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            l_speed -= int(p * p_error + i * i_error)
            r_speed += int(p * p_error + i * i_error)
            drive(l_speed, r_speed)
    if freeze:
        freeze_bot()
    else:
        pass


def drive_until_line(power): # edited for blue bot
    clear_motor_position_counter(c.LMOTOR)
    clear_motor_position_counter(c.RMOTOR)
    drive(power, power)

    F = 0.96  # CLONE: 1.02

    p = 0.25
    i = 0.04
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    if power > 0:
        while analog_et(0) < 3200:
            clear_motor_position_counter(c.LMOTOR)
            clear_motor_position_counter(c.RMOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LMOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RMOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            l_speed += int(p * p_error + i * i_error)
            r_speed -= int(p * p_error + i * i_error)
            drive(l_speed, r_speed)

    else:
        while analog_et(0) < 3200:
            clear_motor_position_counter(c.LMOTOR)
            clear_motor_position_counter(c.RMOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LMOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RMOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            print(l_position, r_position, p_error)
            print(total_left, total_right)
            l_speed -= int(p * p_error + i * i_error)
            r_speed += int(p * p_error + i * i_error)
            print(l_speed, r_speed)
            drive(l_speed, r_speed)

    freeze_bot()


def pivot(power, angle, stationary_wheel): # edited now for new blue horizontal deliver robot
    # angle in degrees
    clear_motor_position_counter(c.LMOTOR)
    clear_motor_position_counter(c.RMOTOR)
    arc_length = (angle * 12 * c.PI)
    print("arc length", arc_length)

    F = 1.75

    speed = power
    total_left = 0
    total_right = 0

    while total_right < arc_length and total_left < arc_length:
        clear_motor_position_counter(c.LMOTOR)
        clear_motor_position_counter(c.RMOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LMOTOR)) * F  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RMOTOR)) * F
        total_left += l_position
        total_right += r_position
        if stationary_wheel == "l":
            drive(0, speed)
        if stationary_wheel == "r":
            drive(speed, 0)

    freeze_bot()


def spin(power, angle): # not yet edited
    # angle in degrees
    clear_motor_position_counter(c.LMOTOR)
    clear_motor_position_counter(c.RMOTOR)
    inches = (angle * 6 * c.PI) // 360
    print("arc length", inches)
    steves = inches * 180

    F = 0.94

    p = 0.25
    i = 0.05
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    while total_right < steves and total_left < steves:
        clear_motor_position_counter(c.LMOTOR)
        clear_motor_position_counter(c.RMOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LMOTOR)) * F  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RMOTOR)) * F
        total_left += l_position
        total_right += r_position
        p_error = (r_position - l_position)
        i_error = total_right - total_left
        # l_speed += int(p * p_error + i * i_error)
        # r_speed -= int(p * p_error + i * i_error)
        drive(l_speed, -r_speed)

    freeze_bot()
