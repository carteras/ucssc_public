# Actuators and Basic Microcontrollers

## You will learn
* Gain an initial awareness of the Micro:Bit Ecosystem
* Build a basic system
* Gain knowledge of simple sensors by using a push button
* Understand how to use push buttons to create simple systems
* Gain knowledge on how to read digital data
* Understand how to accept that data in simple systems. 
* Gain knowledge of how simple conditions work

## Dictionary and Literacy Corner

Nobody would deny that having strong literacy skills is important for almost every part of life. The same is true in technical subjects: sharing a common technical literacy makes it easier for professionals to talk to each other.

What do the following terms mean. Create a word document and copy and paste these terms and what they mean. You might need to look up google
Words:
* Push-button 
* Micro:Bit
* USB
* Jump Cable/Wire
* LED
* actuator
* sensor

Code: 
* ![](2021-07-13-09-52-29.png)
* ![](2021-07-13-09-53-12.png)
* ![](2021-07-13-09-53-37.png)
* ![](2021-07-13-09-54-32.png)
* ![](2021-07-13-09-54-00.png)
* ![](2021-07-13-09-54-16.png)
* ![](2021-07-13-09-55-33.png)

## Introduction

This semester our focus is on designing and building completely new things. Things that we can't just go up to a store and buy. 

## Requirements

We will need a few components to make this work: 

### Micro:bit

First up, we are going to need a micro:bit
<img src="img/2021-02-15-09-58-07.png" width="250"/>

### Micro:bit prototype board connector

Something new in our mix is a connector for our micro:bit that allows us to connect our micro:bit to a breadboard or prototyping board. 

<img src="img/2021-02-15-09-58-51.png" width="250"/>

### Prototyping board

Prototyping boards allow us to connect components together without soldering or making full blown circuits. 

<img src="img/2021-02-15-09-59-19.png" width="250"/>

Essentially, breadboards are strips of metal that allow us to make connections

![](img/2021-02-15-19-08-38.png)

### LED 

LEDs are little lights that we can turn on or off. 

<img src="img/2021-02-15-09-59-54.png" width="250"/>

### Jump cables (red and black)

Jump cables allow us to plug into prototype boards to make a connection

<img src="img/2021-02-15-10-00-20.png" width="250"/>


### 220ohm resistor 
LEDs can only take 2.4 volts of power. Micro:bits deliver 5 volts. We use resistors to limit the flow of electricity to the LED to protect it. 

<img src="img/2021-02-15-10-00-54.png" width="250"/>

### Code design

The goal for this worked example is to turn an LED on and then turn it off. With each on/off change having a pause for 100 ms

<img src="img/2021-02-15-12-34-23.png"/>

### Code

Eventually, this is what our code is going to look like. 

![code](img/2021-02-15-12-30-26.png)
<img src="" width="250"/>

### Circuit Diagram

<img src="2021-02-15-20-04-03.png" width="250"/>

## instructions

### Digital Write 

Micro:bits give us the ability to power pins and read the power status of pins individually. This is called "digital write" and "digital read". Today we are going to use the digital write block. 

To find digital write, click advance

![](2021-02-15-20-07-13.png)

scroll down and find Pins

![](2021-02-15-20-05-43.png)

Inside the Pins section we can see the digital write block 

![](2021-02-15-20-07-52.png)

Let's make some code that allows us to turn a pin on if we press the A button and turn it off when we press the B button (in the simulator)

![](2021-02-15-20-12-04.png)

Go back to Pins digital write. Set the pin to 9 and select 1 on one Button Press and select 0 on the other. 

![](2021-02-15-20-12-26.png)


## Program Blinking Light

Save this project and make a new one called Blinking Light. 

We are going to make the following program. 
<img src="img/2021-02-15-12-34-23.png"/>

This diagram says that we are going to set the LED ENABLE to false. This turns off the LED on the Micro:bit and allows us to use the pins for our own devices. 

![](img/2021-02-15-12-53-54.png)

We can do this with the following code. (LED ENABLE is in LED -> Show more)

![](img/2021-02-15-13-00-07.png)

The next stage is to set digital write on pin 9 to 1 (ON). 
![](img/2021-02-15-12-57-32.png)
We can do this by selected Advanced -> Pins -> digital write pin (p9) to 1

![](img/2021-02-15-13-00-33.png)

Now we want the program to pause for a while. So we can see it turn on. 
![](img/2021-02-15-12-57-46.png)

We can go back to our old faithful Basic -> Pause(100ms)
![](img/2021-02-15-13-01-45.png)

Next we are going to turn the LED off. 
![](img/2021-02-15-12-57-58.png)

We can do that by going back to Advanced -> Pins -> digital write P9 0
![](img/2021-02-15-13-02-10.png)

Now, we want to pause the program so we can see it turns off. 
![](img/2021-02-15-12-58-14.png)

Again we can do that through Basic -> pause (100ms)
![](img/2021-02-15-13-03-28.png)

Now, because we are in a forever loop, this will happen forever!
![](img/2021-02-15-12-58-48.png)

## Challenges
When you complete a challenge, record it and save it to your google drive. Make sure you name it so you can remember it. 

### Blinking 2 LEDs

![](2021-07-13-10-00-03.png)
![](2021-07-13-09-36-53.png)

### Challenge 1

Your challenge is to make two blinking lights. On on Pin 9 and one on Pin 10. You want to make it so if P9 is on, then P10 is off and if P10 is on then P9 is off. 

### Challenge 2

