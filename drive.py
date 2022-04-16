from kipr import msleep, motor_power, analog_et, get_motor_position_counter, \
    clear_motor_position_counter
import constants as c
import utilities as u


# clockwise is positive


def blind(l_speed: int, r_speed: int):
    motor_power(c.RIGHT_MOTOR, r_speed)
    motor_power(c.LEFT_MOTOR, l_speed)


def time_straight(power, time, freeze=True):  # edited for blue bot
    end_time = time() + time
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    blind(power, power)

    F = 0.96  # CLONE: 1.02

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


def distance_straight(power, inches, freeze=True):  # edited for blue bot
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    blind(power, power)
    distance = inches * 180.0

    F = 0.96  # CLONE: 1.02

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


def until_line(power):  # edited for blue bot
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    blind(power, power)

    F = 0.96  # CLONE: 1.02

    p = 0.25
    i = 0.04
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    if power > 0:
        while analog_et(0) < 3200:
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
        while analog_et(0) < 3200:
            clear_motor_position_counter(c.LEFT_MOTOR)
            clear_motor_position_counter(c.RIGHT_MOTOR)
            msleep(50)
            l_position = abs(get_motor_position_counter(c.LEFT_MOTOR))  # abs to account for negative power
            r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR))
            total_left += l_position
            total_right += r_position
            p_error = (r_position * F - l_position)
            i_error = total_right * F - total_left
            print(l_position, r_position, p_error)
            print(total_left, total_right)
            l_speed -= int(p * p_error + i * i_error)
            r_speed += int(p * p_error + i * i_error)
            print(l_speed, r_speed)
            blind(l_speed, r_speed)

    u.freeze_bot()


def pivot(power, angle, stationary_wheel):  # edited now for new blue horizontal deliver robot
    # angle in degrees
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    arc_length = (angle * 12 * c.PI)
    print("arc length", arc_length)

    F = 1.75

    speed = power
    total_left = 0
    total_right = 0

    while total_right < arc_length and total_left < arc_length:
        clear_motor_position_counter(c.LEFT_MOTOR)
        clear_motor_position_counter(c.RIGHT_MOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LEFT_MOTOR)) * F  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR)) * F
        total_left += l_position
        total_right += r_position
        if stationary_wheel == "l":
            blind(0, speed)
        if stationary_wheel == "r":
            blind(speed, 0)

    u.freeze_bot()


def spin(power, angle):  # not yet edited
    # angle in degrees
    clear_motor_position_counter(c.LEFT_MOTOR)
    clear_motor_position_counter(c.RIGHT_MOTOR)
    inches = (angle * 6 * c.PI) // 360
    print("arc length", inches)
    distance = inches * 180

    F = 0.94

    p = 0.25
    i = 0.05
    l_speed = power
    r_speed = power
    total_left = 0
    total_right = 0

    while total_right < distance and total_left < distance:
        clear_motor_position_counter(c.LEFT_MOTOR)
        clear_motor_position_counter(c.RIGHT_MOTOR)
        msleep(50)
        l_position = abs(get_motor_position_counter(c.LEFT_MOTOR)) * F  # abs to account for negative power
        r_position = abs(get_motor_position_counter(c.RIGHT_MOTOR)) * F
        total_left += l_position
        total_right += r_position
        p_error = (r_position - l_position)
        i_error = total_right - total_left
        # l_speed += int(p * p_error + i * i_error)
        # r_speed -= int(p * p_error + i * i_error)
        blind(l_speed, -r_speed)

    u.freeze_bot()
