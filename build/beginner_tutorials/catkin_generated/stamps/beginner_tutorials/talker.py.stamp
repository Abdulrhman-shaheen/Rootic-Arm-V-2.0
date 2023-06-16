import rospy
from std_msgs.msg import String
import getch
from std_msgs.msg import UInt16
import time

class Servo:
    def __init__(self, angle,name):
        self.angle = angle
        self.name = name

    def set_angle(self, angle):
        self.angle = angle

    def set_name(self, name):
        self.name = name


    def inc_angle(self):
        if self.angle < 180:
            self.angle+=5
        else:
            pass 

    def dec_angle(self):
        if self.angle > 0:
            self.angle+=-5
        else:
            pass

    def get_angle(self):
        return self.angle
    
Servo1 = Servo(0,"Servo1")
Servo2 = Servo(0,"Servo2")
Servo3 = Servo(0,"Servo3")
Servo4 = Servo(0,"Servo4")
Servo5 = Servo(0,"Servo5") 
Servo6 = Servo(0,"Servo6")
servo = Servo(0,"Name")


pubServo1 = rospy.Publisher("Servo1", UInt16, queue_size=1)
pubServo2 = rospy.Publisher("Servo2", UInt16, queue_size=1)
pubServo3 = rospy.Publisher("Servo3", UInt16, queue_size=1)
pubServo4 = rospy.Publisher("Servo4", UInt16, queue_size=1)
pubServo5 = rospy.Publisher("Servo5", UInt16, queue_size=1)
pubServo6 = rospy.Publisher("Servo6", UInt16, queue_size=1)
        
def publish_data(topic, message):

    pub = globals()["pub" + topic]   
    pub.publish(message)
    rate = rospy.Rate(200) # publish at 10 Hz
    rate.sleep()



def angle_change():
    
    global servo

    while not rospy.is_shutdown():
        
        k = ord(getch.getch())
        if k == ord("q") or k == ord("a") :
            servo = Servo1
            
        elif k == ord("w") or k == ord("s") :
            servo = Servo2

        elif k == ord("e") or k == ord("d") :
            servo = Servo3

        elif k == ord("r") or k == ord("f") :
            servo = Servo4

        elif k == ord("t") or k == ord("g") :
            servo = Servo5
            
        elif k == ord("y") or k == ord("h") :
            servo = Servo6


        increase_val=[ord("q"),ord("w"),ord("e"),ord("r"),ord("t"),ord("y")]
        decrease_val=[ord("a"),ord("s"),ord("d"),ord("f"),ord("g"),ord("h")]

        if k in increase_val:
            servo.inc_angle()
        
            
        if k in decrease_val:
           servo.dec_angle()

    
        publish_data(servo.name, servo.get_angle())
        

if __name__ == '__main__':
    rospy.init_node('Talker', anonymous=True)
    angle_change()




