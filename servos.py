from kipr import msleep, get_servo_position, set_servo_position


def move_servo(port, position):
    start = get_servo_position(port)
    print("Start pos", start)

    while start > position:
        start -= 1
        print(start)
        set_servo_position(port, start)
        msleep(1)
