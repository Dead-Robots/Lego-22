from kipr import msleep, enable_servos, disable_servos, analog_et, a_button, b_button, \
    c_button, shut_down_in
from time import time
import constants as c
import utilities as u
import drive
import servo

start_time = 0


def pc(prime, clone):
    if c.IS_PRIME:
        return prime
    else:
        return clone


def power_on_self_test():
    print("power on self test")
    if c.IS_PRIME:
        print("I am prime")
    else:
        print("I am clone")
    enable_servos()
    servo.move(c.ARM, c.ARM_MID, 35)
    print("calibrate gryo with btn")
    drive.calibrate_gyro()
    print('k thnx')
    drive.self_test()
    servo.self_test()
    servo.move(c.TAIL_STICK, c.TAIL_HIDE, 55)
    servo.move(c.TAIL_STICK, int(c.TAIL_OUT / 2), 55)
    servo.move(c.TAIL_STICK, c.TAIL_HIDE, 55)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 60)
    adjust_delivery_height()

    u.wait_for_button()
    adjust_pickup_1_height()

    u.wait_for_button()
    adjust_pickup_2_height()

    u.wait_for_button()


delivery_offset = 0
pickup_1_offset = 0
pickup_2_offset = 0


def adjust_delivery_height():
    print("A increase height, B decrease, C when done")
    starting_arm = c.ARM_DELIVER_RINGS_1 - 60
    starting_wrist = c.WRIST_DELIVER_RINGS_1
    global delivery_offset
    while True:
        servo.move(c.ARM, starting_arm + delivery_offset)
        servo.move(c.WRIST, starting_wrist - delivery_offset)
        if a_button():
            delivery_offset -= 15  # 25
        elif b_button():
            delivery_offset += 15  # 25
        elif c_button():
            break
    print("height adjusted! :D")


def adjust_pickup_1_height():
    print("pick up 1")
    print("A increase height, B decrease, C when done")
    starting_arm = c.ARM_PICK_UP_1
    starting_wrist = c.WRIST_PICK_UP_1
    global pickup_1_offset
    while True:
        servo.move(c.ARM, starting_arm + pickup_1_offset)
        servo.move(c.WRIST, starting_wrist - pickup_1_offset)
        if a_button():
            pickup_1_offset -= 15  # 25
        elif b_button():
            pickup_1_offset += 15  # 25
        elif c_button():
            break
    print("pick up 1 adjusted! :D")


def adjust_pickup_2_height():
    print("pick up 2")
    print("A increase height, B decrease, C when done")
    starting_wrist = c.WRIST_PICK_UP_2
    starting_arm = c.ARM_PICK_UP_2
    global pickup_2_offset
    while True:
        servo.move(c.WRIST, starting_wrist - pickup_2_offset)
        servo.move(c.ARM, starting_arm + pickup_2_offset)
        if a_button():
            pickup_2_offset -= 15  # 25
        elif b_button():
            pickup_2_offset += 15  # 25
        elif c_button():
            break
    print("pick up 1 adjusted! :D")


def init():
    print("starting up :)")
    enable_servos()
    servo.move(c.WRIST, c.WRIST_START)
    servo.move(c.ARM, c.ARM_PICK_UP_1 + pickup_1_offset)
    u.wait_4_light()
    # u.wait_for_button()  # wait for light
    global start_time
    start_time = time()
    shut_down_in(119)


def get_rings_1():
    print("get rings 1")
    drive.until_line(-50, c.FRONT_TOPHAT)
    if c.IS_PRIME:
        drive.pivot(50, 13, "l")  # was 19
    else:
        drive.pivot(50, 14, "l")  # was 18
    drive.until_line(50)
    servo.move(c.WRIST, c.WRIST_PICK_UP_1 - pickup_1_offset)
    drive.pivot(-50, pc(17, 13), "l")  # change 9:48
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
    drive.distance_straight(-80, 12, False, pc(0.04, 0.03))
    drive.pivot(50, pc(6, 12), "l")  # was 5 for prime
    drive.until_line(-50)
    drive.distance_straight(-80, 9, True, pc(0.00, 0.00))
    if c.IS_PRIME:
        # drive.pivot(-50, 6, "l")
        pass
    else:
        drive.pivot(50, 5, "l")  # added bc front wheel on clone is not on wall so left side of claw snags on pipe
    # drive.pivot(50, 5, "l")
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1_HALFWAY + delivery_offset)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1_HALFWAY - delivery_offset)
    msleep(250)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 + delivery_offset)  # -150
    msleep(250)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 - delivery_offset)  # 100
    # servo.move(c.ARM, c.ARM_DELIVER_RINGS_1)
    drive.distance_straight(40, 12.5)  # 12
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 - 50 + delivery_offset)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 - delivery_offset)
    drive.distance_straight(40, 0.5)
    servo.move(c.WRIST, c.WRIST_DELIVER_RINGS_1 + 30 - delivery_offset)
    servo.move(c.ARM, c.ARM_PRE_PUSH + delivery_offset)
    servo.move(c.WRIST, c.WRIST_PUSH - delivery_offset)


def return_to_rings():
    print("return to rings")
    drive.distance_straight(-60, 10, True, pc(0.06, 0.06))
    servo.move(c.ARM, c.ARM_UP_MAX)
    servo.move(c.WRIST, c.WRIST_UP)
    drive.distance_straight(60, 12)
    drive.until_line(50, c.FRONT_TOPHAT)  # straightens out in case the wheel gets caught
    drive.pivot(50, c.return_turn, "l")
    drive.until_line(50)
    servo.move(c.WRIST, c.WRIST_PICK_UP_2 - pickup_2_offset)
    servo.move(c.ARM, c.ARM_PICK_UP_2 + pickup_2_offset)


def get_rings_2():
    print("get rings 2")
    drive.pivot(-50, pc(15, 12), "l")  # angle used to be 15 - test for prime
    drive.distance_straight(60, 6)
    servo.move_parallel_with_drive(c.ARM_UP_HIGH, 25)
    msleep(250)
    drive.distance_straight(-70, 3)
    servo.move(c.WRIST, c.WRIST_UP_MAX)
    servo.move(c.ARM, c.ARM_UP_MAX + 50, 10)
    msleep(250)


def deliver_rings_2():
    print("deliver rings 2")
    drive.distance_straight(-80, 12, False, pc(0.03, 0.03))
    drive.pivot(50, pc(5, 11), "l")
    drive.until_line(-50)
    drive.distance_straight(-80, 9)
    # drive.pivot(50, 5, "l")
    servo.move(c.ARM, 660)
    msleep(250)
    servo.move(c.WRIST, c.WRIST_UP - 60)
    msleep(250)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 + 0 + delivery_offset)  # TRY DECREASING THIS VALUE NEXT TIME (HIGHER), 70
    msleep(250)
    servo.move(c.WRIST,
               c.WRIST_DELIVER_RINGS_1 - delivery_offset)  # was 110, try putting wrist back even more next time by subtracting more
    msleep(250)
    servo.move(c.ARM, c.ARM_DELIVER_RINGS_1 + 30 + delivery_offset)  # new
    msleep(250)
    drive.distance_straight(40, 13)
    servo.move(c.ARM, c.ARM_PRE_PUSH + delivery_offset)
    servo.move(c.WRIST, c.WRIST_PUSH - delivery_offset)


def release_tennis_balls():
    servo.move(c.ARM, c.ARM_PRE_PUSH + delivery_offset)  # temporary
    servo.move(c.WRIST, c.WRIST_PUSH - delivery_offset)
    servo.move(c.TAIL_STICK, c.TAIL_HIDE)
    drive.until_line(-90, c.BACK_TOPHAT, False)
    # drive.blind(-90, -60)
    # msleep(1700)
    drive.distance_straight(-50, 5)  # 7
    drive.pivot(-80, 5, "l")
    drive.distance_straight(-50, 5)
    drive.pivot(80, 5, "l")
    drive.until_line(90, c.BACK_TOPHAT, False)
    drive.distance_straight(-50, 7) # same place but squared against the wall

    drive.gyro_pivot_precise(90, 90, "r")
    msleep(100)
    drive.until_line(90, c.FRONT_TOPHAT, False)
    drive.until_line(90, c.BACK_TOPHAT, False)
    drive.gyro_pivot_precise(-90, 177, "l")  # was 180, but it drifts to the right consistently on the next drive
    drive.until_line(-90, c.FRONT_TOPHAT)
    servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
    servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
    msleep(100)
    drive.distance_straight(-80, 9.6)  # was 9
    lift_ball_screen(2)
    servo.move(c.TAIL_STICK, c.TAIL_HALF, 70)
    drive.distance_straight(80, 5)
    servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
    drive.pivot(-80, 7, "l")
    drive.distance_straight(-80, 5)  # was 6
    lift_ball_screen(2)  # was 3
    servo.move(c.TAIL_STICK, c.TAIL_HALF, 70)  # new
    drive.distance_straight(80, 5)
    servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
    drive.pivot(-80, 7, "r")
    lift_ball_screen(2)
    drive.distance_straight(80, 3)
    print("finished run!")


def lift_ball_screen(n):
    for x in range(n):
        if time() - start_time < 2:
            servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
            print("stopped in loop!")
            shutdown()
        else:
            servo.move(c.TAIL_STICK, c.TAIL_LIFT, 70)
            msleep(250)
            servo.move(c.TAIL_STICK, c.TAIL_OUT, 70)
            drive.pivot(70, 6, "l")  # was 8
            drive.pivot(-70, 6, "l")


def shutdown():
    print("run time:", time() - start_time)
    print("Shutting down")
    disable_servos()
    exit(0)


def gyro_test():
    print("gyro test")
    drive.calibrate_gyro()
    drive.gyro_pivot(60, 90, "l")
    u.wait_for_button()
    drive.gyro_pivot(60, 90, "l")
    u.wait_for_button()
    drive.gyro_pivot(60, 90, "l")
    u.wait_for_button()
    drive.gyro_pivot(60, 90, "l")
    u.wait_for_button()
    drive.gyro_pivot(60, 90, "l")
    u.wait_for_button()
