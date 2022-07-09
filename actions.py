from kipr import msleep, enable_servos, disable_servos, analog_et, a_button, b_button, \
    c_button, shut_down_in
from time import time
import constants as c
import utilities as u
import drive
import servo

start_time = 0


def power_on_self_test():
    print("power on self test")
    if c.IS_PRIME:
        print("I am prime")
    else:
        print("I am clone")
    enable_servos()
    servo.move(c.ARM, c.ARM_MID, 35)
    drive.self_test()
    servo.self_test()
    servo.move(c.TAIL_STICK, c.TAIL_HIDE, 35)
    servo.move(c.TAIL_STICK, int(c.TAIL_OUT / 2), 35)
    servo.move(c.TAIL_STICK, c.TAIL_HIDE, 35)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 60)
    adjust_height()
    u.wait_for_button()


offset = 0


def adjust_height():
    print("A increase height, B decrease, C when done")
    starting_arm = c.ARM_DELIVER_RINGS_1 - 60
    starting_wrist = c.WRIST_DELIVER_RINGS_1
    global offset
    while True:
        servo.move(c.ARM, starting_arm + offset)
        servo.move(c.WRIST, starting_wrist - offset)
        if a_button():
            offset -= 15  # 25
        elif b_button():
            offset += 15  # 25
        elif c_button():
            break
    print("height adjusted! :D")


def init():
    print("starting up :)")
    enable_servos()
    servo.move(c.WRIST, c.WRIST_START)
    servo.move(c.ARM, c.ARM_PICK_UP_1)
    u.wait_4_light()
    # u.wait_for_button()  # wait for light
    global start_time
    start_time = time()
    shut_down_in(119)


def get_rings_1():
    print("get rings 1")
    drive.until_line(-50, c.FRONT_TOPHAT)
    if c.IS_PRIME:
        drive.pivot(50, 19, "l")
    else:
        drive.pivot(50, 18, "l")
    drive.until_line(50)
    servo.move(c.WRIST, c.WRIST_PICK_UP_1)
    drive.pivot(-50, 13, "l")
    drive.distance_straight(60, 4)
    drive.distance_straight(30, 1)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 20)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP)
    servo.move(c.ARM, c.ARM_UP)
    msleep(250)


def deliver_rings_1():
    print("deliver rings 1")
    drive.distance_straight(-80, 12, False)
    drive.pivot(50, 5, "l")
    drive.until_line(-50)
    drive.distance_straight(-80, 9)
    if c.IS_PRIME:
        pass  # prime working without pivot so don't want to mess with it
    else:
        drive.pivot(50, 5, "l")  # added bc front wheel on clone is not on wall so left side of claw snags on pipe
    # drive.pivot(50, 5, "l")
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 100 + offset)  # -150
    msleep(500)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 + 70 - offset)  # 100
    # servo.move(c.ARM, c.ARM_DELIVER_RINGS_1)
    drive.distance_straight(40, 12.5)  # 12
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 50 + offset)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 - offset)
    drive.distance_straight(40, 0.5)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 + 30 - offset)
    servo.move(c.ARM, c.ARM_PRE_PUSH + offset)
    servo.move(c.WRIST, c.WRIST_PUSH - offset)


def return_to_rings():
    print("return to rings")
    drive.distance_straight(-60, 10)
    servo.move(c.ARM, c.ARM_UP_MAX)
    servo.move(c.WRIST, c.WRIST_UP)
    drive.distance_straight(60, 12)
    drive.until_line(50, c.FRONT_TOPHAT)  # straightens out in case the wheel gets caught
    drive.pivot(50, c.return_turn, "l")
    drive.until_line(50)
    servo.move(c.WRIST, c.WRIST_PICK_UP_2 + (0 if c.IS_PRIME else 100))
    servo.move(c.ARM, c.ARM_PICK_UP_2)


def get_rings_2():
    print("get rings 2")
    drive.pivot(-50, 12, "l")  # angle used to be 15 - test for prime
    drive.distance_straight(60, 6)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 25)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP_MAX)
    servo.move(c.ARM, c.ARM_UP_MAX + 50, 10)
    msleep(250)


def deliver_rings_2():
    print("deliver rings 2")
    drive.distance_straight(-80, 12, False)
    drive.pivot(50, 5, "l")
    drive.until_line(-50)
    drive.distance_straight(-80, 9)
    drive.pivot(50, 5, "l")
    servo.move(c.ARM, 660)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_UP - 60)
    msleep(250)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 70 + offset)  # TRY DECREASING THIS VALUE NEXT TIME (HIGHER)
    msleep(250)
    servo.move(c.WRIST,
               c.WRIST_DELIVER_RINGS_1 - 110 - offset)  # was 50, try putting wrist back even more next time by subtracting more
    msleep(250)
    drive.distance_straight(40, 13)
    servo.move(c.ARM, c.ARM_PRE_PUSH + offset)
    servo.move(c.WRIST, c.WRIST_PUSH - offset)


def release_tennis_balls():
    servo.move(c.ARM, c.ARM_PRE_PUSH + offset)  # temporary
    servo.move(c.WRIST, c.WRIST_PUSH - offset)
    servo.move(c.TAIL_STICK, c.TAIL_HIDE)
    drive.until_line(-90, c.BACK_TOPHAT, False)
    drive.blind(-90, -60)
    msleep(1700)
    drive.pivot(90, c.tennis_ball_spin_1, "r")
    drive.until_line(90, c.FRONT_TOPHAT, False)
    drive.until_line(90, c.BACK_TOPHAT, False)
    drive.pivot(-90, c.tennis_ball_spin_2, "l")
    drive.until_line(-90, c.FRONT_TOPHAT)
    # move stick
    servo.move(c.TAIL_STICK, c.TAIL_OUT)
    msleep(100)
    drive.distance_straight(-80, 7.5)
    lift_ball_screen(3)
    drive.distance_straight(80, 5)
    drive.pivot(-80, 7, "l")
    drive.distance_straight(-80, 3.7) # was 3.7
    lift_ball_screen(3)


def lift_ball_screen(n):
    for x in range(n):
        if time() - start_time < 5:
            servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
            print("stopped in loop!")
            shutdown()
        else:
            servo.move(c.TAIL_STICK, c.TAIL_LIFT, 70)
            msleep(250)
            servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
            drive.pivot(70, 6, "l") # was 8
            drive.pivot(-70, 6, "l")


def shutdown():
    print("run time:", time() - start_time)
    print("Shutting down")
    disable_servos()
    exit(0)
