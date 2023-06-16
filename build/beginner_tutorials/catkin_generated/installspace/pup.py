#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from pyPS4Controller.controller import Controller

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
    
Servo1 = Servo(0, "Servo1")
Servo2 = Servo(0, "Servo2")
Servo3 = Servo(0, "Servo3")
Servo4 = Servo(0, "Servo4")
Servo5 = Servo(0, "Servo5") 
Servo6 = Servo(0, "Servo6")
servo = Servo(0, "Name")


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

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

        # Initialize ROS node and publisher
        rospy.init_node('ps4_controller_publisher')
        
    def on_left_arrow_press(self):
        global servo
        servo = Servo1
        publish_data(servo.name,servo.get_angle())

    def on_up_arrow_press(self):
        global servo
        servo = Servo2
        publish_data(servo.name,servo.get_angle())

    def on_right_arrow_press(self):
        global servo
        servo = Servo3
        publish_data(servo.name,servo.get_angle())

    def on_down_arrow_press(self):
        global servo
        servo = Servo4
        publish_data(servo.name,servo.get_angle())

    def on_circle_press(self):
        global servo
        servo = Servo5
        publish_data(servo.name,servo.get_angle())

    def on_x_press(self):
        global servo
        servo = Servo6
        publish_data(servo.name,servo.get_angle())

    def on_L3_up(self, value):
        servo.inc_angle()
        publish_data(servo.name,servo.get_angle())

    def on_L3_down(self, value):
        servo.dec_angle()
        publish_data(servo.name,servo.get_angle())

while not rospy.is_shutdown():
    try:
        controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
        controller.listen()
        rospy.spin()  # wait for the node to be shutdown
    except:
        pass