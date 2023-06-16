import tkinter as tk
from PIL import Image, ImageTk
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
import time
import signal
import subprocess
import os 

Main_list = []
pubServo1 = rospy.Publisher("Servo1", UInt16, queue_size=1)
pubServo2 = rospy.Publisher("Servo2", UInt16, queue_size=1)
pubServo3 = rospy.Publisher("Servo3", UInt16, queue_size=1)
pubServo4 = rospy.Publisher("Servo4", UInt16, queue_size=1)
pubServo5 = rospy.Publisher("Servo5", UInt16, queue_size=1)
pubServo6 = rospy.Publisher("Servo6", UInt16, queue_size=1)




rospy.Subscriber("Servo1", UInt16, lambda data: callback(1, data))
rospy.Subscriber("Servo2", UInt16, lambda data: callback(2, data))
rospy.Subscriber("Servo3", UInt16, lambda data: callback(3, data))
rospy.Subscriber("Servo4", UInt16, lambda data: callback(4, data))
rospy.Subscriber("Servo5", UInt16, lambda data: callback(5, data))
rospy.Subscriber("Servo6", UInt16, lambda data: callback(6, data))

def publish_data_once(topic, message): 
    '''
    A function that is used to publish data by passing the topic 
    and the desired msg as arguments 
    '''
    pub = globals()["pub" + topic]   
    print(f"Publishing message {message} to topic {topic}")
    pub.publish(message)


def callback(servo_num, data):
    '''
    The callback function that is excuted when the topic recieve a msg, the servo number
    is passed as an argument along with the angle to be stored in a dictionary used in the 
    recorded moves() function.
    '''
    servo_dict={"Servo": servo_num, "angle":data.data}
    Main_list.append(servo_dict)


def controller():
    '''
    The function for the controller button.
    '''
    command1 = "rosrun beginner_tutorials listener.py"
    command_DS4 = "rosrun beginner_tutorials DS4_Pub.py"

    terminal = subprocess.Popen(['gnome-terminal', '--title', 'Display', '-e', command1])
    p = subprocess.run(['gnome-terminal', '--geometry', '--title', 'Controller', '135x15', '-e', command_DS4])


def keyboard():
    '''
    The function for the keyboard button.
    '''

    command1 = "rosrun beginner_tutorials listener.py"
    command_talker = "rosrun beginner_tutorials keyboard_talker.py"

    terminal = subprocess.Popen(['gnome-terminal', '--title', 'Display', '-e', command1])
    p = subprocess.Popen(['gnome-terminal', '--title', 'Sender','-e', command_talker])    


def play_recorded():
    '''
    The function for the play the previous recorded moves button.
    '''
    
    global Main_list
    Main_list_justnow = []

    for g in Main_list:
        new_dict = {"Servo": g["Servo"], "angle": g["angle"]}
        Main_list_justnow.append(new_dict)

    reset()

    for d in Main_list_justnow:
        publish_data_once(f"Servo{d['Servo']}", d['angle'])
        time.sleep(0.05)
    
    Main_list=[]


def reset():
    '''
    The function for reseting the arm to its original postion.
    '''

    global Main_list
    publish_data_once("Servo1", 180)
    time.sleep(1)
    publish_data_once("Servo2", 130)
    time.sleep(1)
    publish_data_once("Servo3", 105)
    time.sleep(1)
    publish_data_once("Servo4", 40)
    time.sleep(1)
    publish_data_once("Servo5", 40)
    time.sleep(1)
    publish_data_once("Servo6", 0)
    time.sleep(1)
    Main_list=[]


def start_gui():
    '''
    Starting the GUI.
    '''
    rospy.init_node('Talker', anonymous=True)
    arm = tk.Tk()
    arm.title("Robotics Arm GUI")
    arm.geometry("1200x1000")

    # Load and resize the background image $ 

    background_image = Image.open("Arm_image.png")

    resized_image = background_image.resize((1200, 1000), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(resized_image)

    # Create a label for the background image
    background_label = tk.Label(arm, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.lower(background_label)

    label = tk.Label(arm, text="Robotic Arm", font=('Ubuntu', 26), bg="#6363B8", fg="black")
    label.pack(padx=20, pady=20)
    buttons = tk.Frame(arm)
    buttons.columnconfigure(0, weight=1)
    buttons.columnconfigure(1, weight=1)
    buttons.columnconfigure(2, weight=1)

    button1 = tk.Button(buttons, text="controller", font=('Ubuntu', 18), width=10, command=lambda: controller(),
                        bg="#6363B8", fg="black", relief=tk.RAISED)
    
    button1.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)



    button2 = tk.Button(buttons, text="Reset", font=('Ubuntu', 18), width=10, command=lambda: reset(),
                        bg="#5C5CAC", fg="black", relief=tk.RAISED)
    
    button2.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)



    button3 = tk.Button(buttons, text="Play Recorded Moves", font=('Ubuntu', 18), width=10, command=lambda: play_recorded(),
                        bg="#4F4F94", fg="black", relief=tk.RAISED)
    
    button3.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=10)


    button4 = tk.Button(buttons, text="Keyboard Controlling", font=('Ubuntu', 18), width=10, command=lambda: keyboard(),
                        bg="#4F4F94", fg="black", relief=tk.RAISED)
    
    button4.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=10)



    buttons.pack(fill="x", pady=20)
    arm.mainloop()


start_gui()
