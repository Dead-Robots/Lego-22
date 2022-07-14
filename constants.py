from kipr import digital

"""
ALL PORTS:
- left motor: 3
- right motor: 2
- back tophat: 0
- front tophat: 1
- arm servo: 2
- wrist servo: 1
- clone switch: 0
- tail stick: 0
"""

IS_PRIME = not digital(0)

if IS_PRIME:
    ARM_OFFSET = 0
    WRIST_OFFSET = 60
    F = 1.065
    return_turn = 5 # angle of that one turn on the way back where clone often is too far from the wallnn
    tennis_ball_spin_1 = 110
    tennis_ball_spin_2 = 180
    WRIST_UP_MAX = 2000 + WRIST_OFFSET
    WRIST_PICK_UP_2 = 1225 + WRIST_OFFSET
    TAIL_OUT = 25

else:
    ARM_OFFSET = 0
    WRIST_OFFSET = 80
    F = 1.00  # 1.02, was trying to fix the drift to the right
    return_turn = 7
    tennis_ball_spin_1 = 108 # was 115
    tennis_ball_spin_2 = 180
    WRIST_UP_MAX = 2047 + WRIST_OFFSET
    WRIST_PICK_UP_2 = 1225 + WRIST_OFFSET - 60
    TAIL_OUT = 100

LEFT_MOTOR = 3
RIGHT_MOTOR = 2
TAIL_STICK = 0

BACK_TOPHAT = 0
FRONT_TOPHAT = 1
START_LIGHT = 2
START_LIGHT_THRESHOLD = 0

ARM = 2
WRIST = 1

BLACK = 2000

ARM_UP_MAX = 105 + ARM_OFFSET
ARM_UP = 405 + ARM_OFFSET
ARM_UP_HIGH = 740 + ARM_OFFSET
ARM_MID = 890 + ARM_OFFSET
ARM_DELIVER_RINGS_1 = 1200 + ARM_OFFSET  #
ARM_DELIVER_RINGS_1_HALFWAY = 750 + ARM_OFFSET
# ARM_DELIVER_RINGS_2 = 1330 + ARM_OFFSET
ARM_PICK_UP_1 = 1435 + ARM_OFFSET  # was 1445, 1385
ARM_PRE_PUSH = 1715 + ARM_OFFSET
ARM_PICK_UP_2 = 1895 + ARM_OFFSET  # was 1895

WRIST_DELIVER_RINGS_1 = 820 + WRIST_OFFSET
WRIST_START = 870 + WRIST_OFFSET
# WRIST_DELIVER_RINGS_2 = 890 + WRIST_OFFSET
WRIST_TILT = 1272 + WRIST_OFFSET
WRIST_PUSH = 1340 + WRIST_OFFSET
WRIST_PICK_UP_1 = 1540 + WRIST_OFFSET
WRIST_UP = 1710 + WRIST_OFFSET
WRIST_DELIVER_RINGS_1_HALFWAY = 1260 + WRIST_OFFSET
# WRIST_UP_MAX = 2047 + WRIST_OFFSET

TAIL_HIDE = 2047
TAIL_LIFT = 950
TAIL_HALF = 500

PI = 3.14159
