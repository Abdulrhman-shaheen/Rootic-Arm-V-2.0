import tkinter as tk
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
import time

Main_list = []


pubServo1 = rospy.Publisher("Servo1", UInt16, queue_size=1)
pubServo2 = rospy.Publisher("Servo2", UInt16, queue_size=1)
pubServo3 = rospy.Publisher("Servo3", UInt16, queue_size=1)
pubServo4 = rospy.Publisher("Servo4", UInt16, queue_size=1)
pubServo5 = rospy.Publisher("Servo5", UInt16, queue_size=1)
pubServo6 = rospy.Publisher("Servo6", UInt16, queue_size=1)

def publish_data_once(topic, message):
    
    pub = globals()["pub" + topic]   
    print(f"Publishing message {message} to topic {topic}")
    pub.publish(message)



def callback(servo_num, data):
    servo_dict={"Servo": servo_num, "angle":data.data}
    Main_list.append(servo_dict)


def play_recorded():

    global Main_list

    for i in range (1,7):
        publish_data_once("Servo{}".format(i), 0)
        time.sleep(0.5)

    Main_list_justnow = []

    for g in Main_list:
        new_dict = {"Servo": g["Servo"], "angle": g["angle"]}
        Main_list_justnow.append(new_dict)

    for d in Main_list_justnow:
        publish_data_once(f"Servo{d['Servo']}", d['angle'])
        time.sleep(0.5)
    
    Main_list=[]
    

def listener():

    rospy.Subscriber("Servo1", UInt16, lambda data: callback(1, data))
    rospy.Subscriber("Servo2", UInt16, lambda data: callback(2, data))
    rospy.Subscriber("Servo3", UInt16, lambda data: callback(3, data))
    rospy.Subscriber("Servo4", UInt16, lambda data: callback(4, data))
    rospy.Subscriber("Servo5", UInt16, lambda data: callback(5, data))
    rospy.Subscriber("Servo6", UInt16, lambda data: callback(6, data))


if __name__ == '__main__':
    rospy.init_node('PlayRecord', anonymous=True)
    listener()

    # create a GUI window
    root = tk.Tk()
    root.title("Play Recorded Motion")

    play_button = tk.Button(root, text="Play Recorded Motion", command=play_recorded)
    play_button.pack()

    # start the GUI event loop
    root.mainloop()
