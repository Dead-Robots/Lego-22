from kipr import digital

"""
ALL PORTS:
- left motor: 3
- right motor: 2
- back tophat: 0
- front tophat: 1
- arm servo: 0
- wrist servo: 1
- clone switch: 0
"""

IS_PRIME = not digital(0)

if IS_PRIME:
    ARM_OFFSET = 0
    WRIST_OFFSET = 0
    F = 1.065
else:
    ARM_OFFSET = 100
    WRIST_OFFSET = 30
    F = 1.02  # 0.995

LEFT_MOTOR = 3
RIGHT_MOTOR = 2

BACK_TOPHAT = 0
FRONT_TOPHAT = 1

ARM = 0
WRIST = 1

ARM_UP_MAX = 0 + ARM_OFFSET
ARM_UP = 405 + ARM_OFFSET
ARM_UP_HIGH = 740 + ARM_OFFSET
ARM_MID = 890 + ARM_OFFSET
ARM_DELIVER_RINGS_1 = 1250 + ARM_OFFSET  # 1300
# ARM_DELIVER_RINGS_2 = 1330 + ARM_OFFSET
ARM_PICK_UP_1 = 1445 + ARM_OFFSET
ARM_PRE_PUSH = 1715 + ARM_OFFSET
ARM_PICK_UP_2 = 1895 + ARM_OFFSET  # CLONE: 1880

WRIST_DELIVER_RINGS_1 = 750  # 710
WRIST_START = 870
# WRIST_DELIVER_RINGS_2 = 890
WRIST_TILT = 1272
WRIST_PUSH = 1340
WRIST_PICK_UP_2 = 1220 + WRIST_OFFSET
WRIST_PICK_UP_1 = 1540
WRIST_UP = 1710

PI = 3.14159
