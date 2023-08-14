
# Controlling 6-Servo-robotic-arm by Keyboard or PS4 Controller using ROS & Arduino. 

The robotic arm has 3 main control options that can be accessed from the `GUI_Main.py` along with a reset button that puts the arm into its default position. you can test for yours and modify the value of the `reset()` function in `GUI_Main.py`.
To open the Gui, run `roscore` on one instance, then run from the package `beginner_tutorials` run `GUI_Main.py`. All in `rosrun beginner_tutorials GUI_Main.py `.

`rosserial` is an essential package that receives the published data from  then do the Arduino part where it matches each Servo with the data sent on its topic.s
 
To clone with the `Rosserial` package use:

```
git clone --recurse-submodules https://github.com/Abdulrhman-shaheen/Rootic-Arm-V-2.0.git
```
To run `rosserial` you can use:

``` 
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```
(USB0 may change according to the port) in a separate terminal.
<br><br>

Upload the Arduino code, `Servos_Control.ino` found in the `Arduino` Folder to your Arduino board and you're good to go. 
## The Controller
The mode to use to connect the **PS4 controller** to the arm. In this mode **R1** and **L1** buttons are used to change the servo being controller (excluding the base and the gripper). 
<br> The **L3** Up and down joystick can move the current servo from 0 to 180, and the **R3** Right and Left moves the base of the arm.
<br> The button **X** is used to open and close the gripper.
<br> To operate on this mode Just click the **Controller** button from the GUI, and then connect your PS4 using Bluetooth.
> Listener.py is another node that opens automatically in this mode that receive the data independently just to view the servo you are controlling and its angle.


## Keyboard
To operate on this mode Just click the **Keyboard** button from the GUI, and then connect your PS4 using Bluetooth.

- Servo1 is controlled by **q** and "a" q to increase the angle and "a" to decrease.
- Servo2 is controlled by **w** and "s" w to increase the angle and "s" to decrease.
- Servo3 is controlled by **e** and "d" e to increase the angle and "d" to decrease.
- Servo4 is controlled by **r** and "f" r to increase the angle and "f" to decrease.
- Servo5 is controlled by **t** and "g" t to increase the angle and "g" to decrease.
- Servo6 is controlled by **y** and "h" y to increase the angle and "h" to decrease.
<br>
>Listener.py works here as well.

## Replaying Moves
This mode will first do the `reset()` Function then will move the arm with the same moves that was done either by the keyboard or the PS4 controller.
> You can monitor the data being sent in the terminal for this mode.
 
<sub>
Sorry for in the inconvenience in the name of the workspace and the packages, might fix them later but not now.
</sub>

