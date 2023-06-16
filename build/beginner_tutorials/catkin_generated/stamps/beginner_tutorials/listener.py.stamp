import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16


def callback(servo_num, data):
    rospy.loginfo("Servo{}".format(servo_num))
    rospy.loginfo(data.data)

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("Servo1", UInt16, lambda data: callback(1, data))
    rospy.Subscriber("Servo2", UInt16, lambda data: callback(2, data))
    rospy.Subscriber("Servo3", UInt16, lambda data: callback(3, data))
    rospy.Subscriber("Servo4", UInt16, lambda data: callback(4, data))
    rospy.Subscriber("Servo5", UInt16, lambda data: callback(5, data))
    rospy.Subscriber("Servo6", UInt16, lambda data: callback(6, data))

    rospy.spin()

if __name__ == '__main__':
    listener()
