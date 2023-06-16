#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from pyPS4Controller.controller import Controller
import time
import threading
class Servo:
    def __init__(self, angle, name):
        self.angle = angle
        self.name = name

    def set_angle(self, angle):
        self.angle = angle

    def set_name(self, name):
        self.name = name


    def inc_angle(self):
        if self.angle < 180:
            self.angle += 5
        else:
            pass 

    def dec_angle(self):
        if self.angle > 0:
            self.angle -= 5
        else:
            pass

    def get_angle(self):
        return self.angle
    
Servo1 = Servo(180, "Servo1")
Servo2 = Servo(130, "Servo2")
Servo3 = Servo(105, "Servo3")
Servo4 = Servo(40, "Servo4")
Servo5 = Servo(40, "Servo5") 
Servo6 = Servo(0, "Servo6")



pubServo1 = rospy.Publisher("Servo1", UInt16, queue_size=1)
pubServo2 = rospy.Publisher("Servo2", UInt16, queue_size=1)
pubServo3 = rospy.Publisher("Servo3", UInt16, queue_size=1)
pubServo4 = rospy.Publisher("Servo4", UInt16, queue_size=1)
pubServo5 = rospy.Publisher("Servo5", UInt16, queue_size=1)
pubServo6 = rospy.Publisher("Servo6", UInt16, queue_size=1)
        
def publish_data(topic, message):

    pub = globals()["pub" + topic]   
    pub.publish(message)
    rate = rospy.Rate(20) # publish at 10 Hz
    rate.sleep()

servos = [None, None, Servo(130, "Servo2"), Servo(105, "Servo3"), Servo(40, "Servo4"), Servo(40, "Servo5")]
number = 2
angle6 = 180
servo = servos[number]


class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        rospy.init_node('ps4_controller_publisher')
        art = r"""
___________              ____.               __    __________      ___.           __  .__                _________ .__       ___.    
\_   _____/             |    |__ __  _______/  |_  \______   \ ____\_ |__   _____/  |_|__| ____   ______ \_   ___ \|  |  __ _\_ |__  
 |    __)_   ______     |    |  |  \/  ___/\   __\  |       _//  _ \| __ \ /  _ \   __\  |/ ___\ /  ___/ /    \  \/|  | |  |  \ __ \ 
 |        \ /_____/ /\__|    |  |  /\___ \  |  |    |    |   (  <_> ) \_\ (  <_> )  | |  \  \___ \___ \  \     \___|  |_|  |  / \_\ \
/_______  /         \________|____//____  > |__|    |____|_  /\____/|___  /\____/|__| |__|\___  >____  >  \______  /____/____/|___  /
        \/                              \/                 \/           \/                    \/     \/          \/               \/ 
"""

        rospy.loginfo(art)

        self.l3_pressed_up = threading.Event()
        self.l3_pressed_down = threading.Event()
        self.r3_pressed_right = threading.Event()
        self.r3_pressed_left = threading.Event()
        
    def on_R1_press(self):
        global servos
        global number
        global servo
        if number < 5:
            number += 1
        else:
            number = 2
        servo = servos[number]
        print(servo.name)

    def on_L1_press(self):
        global servos
        global servo
        global number
        if number > 2:
            number -= 1
        else:
            number = 5
        servo = servos[number]
        print(servo.name)


    def on_L3_up(self, value):
            self.l3_pressed_up.set()
            threading.Thread(target=self.l3_control_thread_up).start()

    def on_L3_down(self, value):
            self.l3_pressed_down.set()
            threading.Thread(target=self.l3_control_thread_down).start()
    
    def on_L3_y_at_rest(self):
        self.l3_pressed_up.clear()
        self.l3_pressed_down.clear()

    def l3_control_thread_up(self):
        while self.l3_pressed_up.is_set():
            if servo.name == "Servo3":
                servo.dec_angle()
                time.sleep(0.05)
                publish_data(servo.name, servo.get_angle())
            else:
                servo.inc_angle()
                time.sleep(0.05)
                publish_data(servo.name, servo.get_angle())

    def l3_control_thread_down(self):
        while self.l3_pressed_down.is_set():
            if servo.name == "Servo3":
                servo.inc_angle()
                time.sleep(0.05)
                publish_data(servo.name, servo.get_angle())
            else:    
                servo.dec_angle()
                time.sleep(0.05)
                publish_data(servo.name, servo.get_angle())


    def on_R3_right(self, value):
        self.r3_pressed_right.set()
        threading.Thread(target=self.r3_control_thread_right).start()

    def on_R3_left(self, value):
        self.r3_pressed_left.set()
        threading.Thread(target=self.r3_control_thread_left).start()        



    def on_R3_x_at_rest(self):
        self.r3_pressed_right.clear()
        self.r3_pressed_left.clear()



    def r3_control_thread_right(self):
        while self.r3_pressed_right.is_set():
            Servo1.inc_angle()
            time.sleep(0.05)
            publish_data("Servo1", Servo1.get_angle())

    def r3_control_thread_left(self):
        while self.r3_pressed_left.is_set():
            Servo1.dec_angle()
            time.sleep(0.05)
            publish_data("Servo1", Servo1.get_angle())


    def on_x_press(self):
        global angle6
        if angle6 == 180:
            publish_data("Servo6", angle6)
            angle6 = 0
        else:
            publish_data("Servo6", angle6)
            angle6 =180


    def on_R1_release(self):
        pass

    def on_L1_release(self):
        pass
    def on_x_release(self):
        pass

while not rospy.is_shutdown():
    try:
        controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
        controller.listen()
        rospy.spin()  # wait for the node to be shutdown
    except:
        pass