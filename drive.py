#!/usr/local/bin/python3.10 -u
from kipr import motor, freeze, ao, msleep, motor_power, get_motor_position_counter, clear_motor_position_counter
from time import time

import constants as c


def drive(l_speed: int, r_speed: int):
    motor_power(c.RMOTOR, r_speed)
    motor_power(c.LMOTOR, l_speed)


def freeze_bot():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    msleep(500)


def drive_straight(power, inches):
    clear_motor_position_counter(c.LMOTOR)
    clear_motor_position_counter(c.RMOTOR)
    drive(power, power)
    steves = inches * 181

    p = 0.25
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    while (total_left + total_right)/2 < steves:
        clear_motor_position_counter(c.LMOTOR)
        clear_motor_position_counter(c.RMOTOR)
        msleep(50)
        total_left += get_motor_position_counter(c.LMOTOR)
        total_right += get_motor_position_counter(c.RMOTOR)
        error = get_motor_position_counter(c.RMOTOR) - (get_motor_position_counter(c.LMOTOR)*0.942)
        print(get_motor_position_counter(c.LMOTOR), get_motor_position_counter(c.RMOTOR), error)
        l_speed += int(p * error)
        r_speed -= int(p * error)
        print(l_speed, r_speed)
        drive(l_speed, r_speed)

    freeze_bot()
    print((total_left + total_right)/2)


def left_pivot(power, drive_time):
    drive(0, power)
    msleep(drive_time)
    freeze_bot()


def right_pivot(power, drive_time):
    drive(power * c.PRIME_ADJUST_SPEED, 0)
    msleep(drive_time)
    freeze_bot()


def spin(sp_sp, drive_time):
    drive(sp_sp, -sp_sp)
    msleep(drive_time)
    freeze_bot()
