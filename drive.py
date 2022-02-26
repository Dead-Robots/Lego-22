#!/usr/local/bin/python3.10 -u
from kipr import motor, freeze, ao, msleep, motor_power
import constants as c


def drive(l_speed: int, r_speed: int):
    motor_power(c.RMOTOR, r_speed)
    motor_power(c.LMOTOR, l_speed)


def freeze_bot():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    msleep(500)


def drive_straight(power, time):
    drive(power, int(power * c.PRIME_ADJUST_SPEED))
    msleep(time)
    freeze_bot()


def left_pivot(power, time):
    drive(0, power)
    msleep(time)
    freeze_bot()


def right_pivot(power, time):
    drive(power * c.PRIME_ADJUST_SPEED, 0)
    msleep(time)
    freeze_bot()


def spin(sp_sp, time):
    drive(sp_sp, -sp_sp)
    msleep(time)
    freeze_bot()
