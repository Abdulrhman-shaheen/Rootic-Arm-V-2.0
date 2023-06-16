import rospy
from std_msgs.msg import UInt16
import time
from ds4drv.driver import DS4Drv

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

def publish_data(topic, message):
    pub = rospy.Publisher(topic, UInt16, queue_size=10)
    rospy.init_node('Talker', anonymous=True)
    pub.publish(message)
    rate = rospy.Rate(200)
    rate.sleep()

def angle_change():
    global servo
    controller = DS4Drv(verbose=False)
    print("Wait plz")
    initial_gyro = [0, 0, 0]
    for _ in range(200):
        data = controller.poll()
        if 'gyro' in data:
            gyro = data['gyro']
            initial_gyro[0] += gyro[0]ي
            initial_gyro[1] += gyro[1]
            initial_gyro[2] += gyro[2]
        time.sleep(0.01)
    initial_gyro[0] /= 100
    initial_gyro[1] /= 100
    initial_gyro[2] /= 100
    print("Done")
    while not rospy.is_shutdown():
        data = controller.poll()
        if 'gyro' in data:
            gyro = data['gyro']
            gyro[0] -= initial_gyro[0]
            gyro[1] -= initial_gyro[1]
            gyro[2] -= initial_gyro[2]
            if abs(gyro[0]) > abs(gyro[1]):
                if gyro[0] > 0:
                    servo = Servo4
                else:
                    servo = Servo3
            else:
                if gyro[1] > 0:
                    servo = Servo2
                else:
                    servo = Servo1
            if abs(gyro[2]) > 10:
                if gyro[2] > 0:
                    servo.inc_angle()
                else:
                    servo.dec_angle()
            publish_data(servo.name, servo.get_angle())

if __name__ == '__main__':
    angle_change()