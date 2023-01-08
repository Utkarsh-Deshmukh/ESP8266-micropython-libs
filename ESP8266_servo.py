from machine import Pin, PWM
import time

'''
Tested on: servor motor: SG51R micro-servo: https://www.amazon.com/Servo-Motors-Sub-Micro-SG51R-piece/dp/B0137LG0KW/?_encoding=UTF8&pd_rd_w=eEHkj&content-id=amzn1.sym.f05f10a7-d30f-4cc9-9521-a1dfe37686ab&pf_rd_p=f05f10a7-d30f-4cc9-9521-a1dfe37686ab&pf_rd_r=CY2K2X9KGHVCCEBHVTYF&pd_rd_wg=Ksfpk&pd_rd_r=ee54afdc-6125-4901-8bc9-7da21f50089a&ref_=pd_gw_ci_mcx_mi
Servo PWM pin connected to Pin5 (D1 pin on the ESP board)
Servo frequency = 100Hz
'''

class Servo:
    def __init__(self, pin, freq=100, duty_cycle=150):
        self.__pin = pin
        self.__freq = freq
        self.__duty_cycle = duty_cycle
        self.__pwm_object = PWM(self.__pin, self.__freq, self.__duty_cycle)

    '''
    @brief
    function to run the servo motor to the specified location via the duty cycle 
    '''
    def run(self, value):
        # NOTE : the servo does not perform a full 360 degree rotation. for a frequency of 100, the min and max duty cycles are 70 to 240
        # Hence in order to safeguard the servo, we must make sure we do not exceed these values. Please keep caution if modifying this part of the code
        if(value > 240):
            value = 240
        if(value < 70):
            value = 70
        self.__pwm_object.duty(value)

def run_servo_example():
    servo_obj = Servo(Pin(5, Pin.OUT))
    # create pwm object on motor_control pin
    # NOTE : the servo does not perform a full 360 degree rotation. for a frequency of 100, the min and max duty cycles are 70 to 240
    # exceeding these limits might ruin the servo motor
    while(True):
        servo_obj.run(240)
        time.sleep_ms(1000)
        servo_obj.run(70)
        time.sleep_ms(1000)