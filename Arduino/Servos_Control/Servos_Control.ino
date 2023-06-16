/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;

  Servo servo1;
  Servo servo2;
  Servo servo3;
  Servo servo4;
  Servo servo5;
  Servo servo6;

void servo1_cb( const std_msgs::UInt16& cmd_msg){
  servo1.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}


void servo2_cb( const std_msgs::UInt16& cmd_msg){
  servo2.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}


void servo3_cb( const std_msgs::UInt16& cmd_msg){
  servo3.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}



void servo4_cb( const std_msgs::UInt16& cmd_msg){
  servo4.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}



void servo5_cb( const std_msgs::UInt16& cmd_msg){
  servo5.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}



void servo6_cb( const std_msgs::UInt16& cmd_msg){
  servo6.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}




ros::Subscriber<std_msgs::UInt16> sub1("Servo1", servo1_cb);
  
  ros::Subscriber<std_msgs::UInt16> sub2("Servo2", servo2_cb);
  
  ros::Subscriber<std_msgs::UInt16> sub3("Servo3", servo3_cb);
  
  ros::Subscriber<std_msgs::UInt16> sub4("Servo4", servo4_cb);
  
  ros::Subscriber<std_msgs::UInt16> sub5("Servo5", servo5_cb);
  
  ros::Subscriber<std_msgs::UInt16> sub6("Servo6", servo6_cb);
  
  void setup(){
  
    nh.initNode();
    nh.subscribe(sub1);
    nh.subscribe(sub2);
    nh.subscribe(sub3);
    nh.subscribe(sub4);
    nh.subscribe(sub5);
    nh.subscribe(sub6);
  
    
    servo1.attach(5); //attach it to pin 9
    servo2.attach(7);
    servo3.attach(6);
    servo4.attach(8);
    servo5.attach(9);
    servo6.attach(10);
  }
  
  void loop(){
    nh.spinOnce();
    delay(1);
}
