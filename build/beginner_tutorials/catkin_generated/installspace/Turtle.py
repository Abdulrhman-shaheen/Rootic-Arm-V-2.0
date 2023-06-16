import rospy
from std_msgs.msg import String

rospy.init_node('publisher_node')

pub = rospy.Publisher('chatter', String, queue_size=10)

message = String()
message.data = "Shnabtshishini"

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(message)
    rate.sleep()
