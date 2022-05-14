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
"""

IS_PRIME = not digital(0)

if IS_PRIME:
    ARM_OFFSET = 0
    WRIST_OFFSET = -15
    F = 1.065
else:
    ARM_OFFSET = 100
    WRIST_OFFSET = 0
    F = 1.02  # 0.995

LEFT_MOTOR = 3
RIGHT_MOTOR = 2

BACK_TOPHAT = 0
FRONT_TOPHAT = 1
START_LIGHT = 2
START_LIGHT_THRESHOLD = 0

ARM = 2
WRIST = 1

BLACK = 2000

ARM_UP_MAX = 0 + ARM_OFFSET
ARM_UP = 405 + ARM_OFFSET
ARM_UP_HIGH = 740 + ARM_OFFSET
ARM_MID = 890 + ARM_OFFSET
ARM_DELIVER_RINGS_1 = 1250 + ARM_OFFSET
# ARM_DELIVER_RINGS_2 = 1330 + ARM_OFFSET
ARM_PICK_UP_1 = 1445 + ARM_OFFSET
ARM_PRE_PUSH = 1715 + ARM_OFFSET
ARM_PICK_UP_2 = 1895 + ARM_OFFSET

WRIST_DELIVER_RINGS_1 = 750 + WRIST_OFFSET
WRIST_START = 870 + WRIST_OFFSET
# WRIST_DELIVER_RINGS_2 = 890 + WRIST_OFFSET
WRIST_TILT = 1272 + WRIST_OFFSET
WRIST_PUSH = 1340 + WRIST_OFFSET
WRIST_PICK_UP_2 = 1235
WRIST_PICK_UP_1 = 1540 + WRIST_OFFSET
WRIST_UP = 1710 + WRIST_OFFSET

PI = 3.14159
