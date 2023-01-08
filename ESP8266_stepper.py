from machine import Pin
import time

'''
Acknowledgement: Special thanks to https://github.com/zhcong/ULN2003-for-ESP32.
'''


'''
Tested on: Stepper motor: 28BYJ-48 : https://www.amazon.com/CenryKay-ULN2003-28BYJ-48-Compatible-Breadboard/dp/B086D5SXPV/ref=sr_1_1_sspa?crid=1KIREQNTCR3L0&keywords=28BYJ-48&qid=1673215602&sprefix=28byj-48%2Caps%2C151&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSUVKQkVPWkdYTUI1JmVuY3J5cHRlZElkPUEwMjc5MDkxMUpIODFCMjFHS1VGRiZlbmNyeXB0ZWRBZElkPUEwODU2ODA0MUVFSjdYQUIwM1o1QyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=
Motor driver: ULN2003
Connections: D0 (Pin 16) - 1N1
             D1 (Pin 5)  - 1N2
             D2 (Pin 4)  - 1N3
             D3 (Pin 0)  - 1N4
'''

class Stepper:
    FULL_ROTATION = int(4075.7728395061727 / 8)  # http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html

    HALF_STEP = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
    ]

    FULL_STEP = [
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]

    def __init__(self, pin1, pin2, pin3, pin4, delay, mode='FULL_STEP'):
        if mode == 'FULL_STEP':
            self.mode = self.FULL_STEP
        else:
            self.mode = self.HALF_STEP
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP

        # Initialize all to 0
        self.reset()

    '''
    @brief 
    function to move the motor by the specified count.
    count [in] : [int] - number of counts to perform the rotation
    direction [in]: [1, -1] - direction of rotation. 1 = direction_forward, -1 = direction_reverse
    '''
    def step(self, count, direction=1):
        """Rotate count steps. direction = -1 means backwards"""
        if count < 0:
            direction = -1
            count = -count
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1(bit[0])
                self.pin2(bit[1])
                self.pin3(bit[2])
                self.pin4(bit[3])
                time.sleep_ms(self.delay)
        self.reset()

    '''
    @brief 
    function to move the motor to the specified angle.
    r [in] : [int] - specified angle in degrees
    direction [in]: [1, -1] - direction of rotation. 1 = direction_forward, -1 = direction_reverse
    '''
    def angle(self, r, direction=1):
        self.step(int(self.FULL_ROTATION * r / 360), direction)

    '''
    @brief 
    function to reset the stepper object.
    '''
    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1(0)
        self.pin2(0)
        self.pin3(0)
        self.pin4(0)

def run_stepper_example():
    stepper_obj = Stepper(Pin(16, Pin.OUT), Pin(5, Pin.OUT), Pin(4, Pin.OUT), Pin(0, Pin.OUT), delay=2, mode='HALF_STEP')

    direction_forward, direction_reverse = 1, -1

    stepper_obj.step(100)
    time.sleep_ms(300)
    stepper_obj.angle(360, direction_forward)
    time.sleep_ms(300)
    stepper_obj.angle(360, direction_reverse)
