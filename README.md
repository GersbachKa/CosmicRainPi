# CosmicRainPi
This software is meant to run on a Raspberry Pi 3, running Raspbian

# Operation instructions:
**1) Find the IP of the Pi**

We control the Pi by SSHing into it using an SSH client (we use PuTTY). Since the Pi generates a new IP every time it starts up, the first step is to find the IP.

A) Plug the Pi into a monitor by using the HDMI out on the Pi. Plug a USB keyboard into the USB port of the Pi. If you're asked to login, the credentials are     username: pi      password: cosmic

B) Press ctrl+alt+T to open up a terminal window and type ifconfig (not ipconfig). Record the WLAN IP - so far it starst with 10.156. ... at least on the Bothell campus. 

**2) Connect to the Pi from your computer**

SSH into the Pi by using your favorite client and using the IP you recorded in step 1. For PuTTY, this is as easy as just typing the IP into the box and leaving all othe settings at their defaults.

**3) Navigate to the proper directory**

Type cd CosmicRainPi, and then cd into the proper folder (at the moment, proper folder = CurrentSoftware). Type the following command:

python3 UkeCLI.py

and you should get a message back giving you instructions on what to press for a given function (play a song, run a motor test, etc.)

**4) DO the thing**

To run a motor test, first type 4 for motortest. Then, the syntax is as follows

motornumber:location

where motornumber corresponds to one of the output pins on the servo hat, and location tells the motor where to move { not sure how to describe the range since I'm not sure it's stayed consistent?}. So for example:

1:400

will move the motor that is plugged into the first pin to the position "400," which is just some arbitrary point on a half-circle. Note that right now things are set up for unidirectional motion, so the motor will move to location "400" and then stay there until commanded to move again. 

To move all motors, type "all" instead of a number, e.x.  

all:400

will move all of the motors to location 400

**CAUTION!** Moving all of the motors at once seems to be a good way to get them to overheat, so if you do this you need to be standing next to the Pi ready to either unplug power from the hat, or unplug individual motors.

[end of operational overview]

# General Outline:

The goal of this software is to command a Pi to autonomously play a Ukelele. The software is comprised of two main parts: 1) motor control and 2) environmental integration. 

Generally, a user will input a song in a specific format that the software can interpret. Then the Pi will read the sheet of music and command a set of motors to fret and pluck a Ukelele to play the song (part 1). Simultaneously, the Pi will sense its enviroment for changes in temperature, light, and the presence of radiation using a geiger counter. In response to signals from one of these sensors, the song being played will be modulated - so a song beginning in one register may end in another, or notes may be added, etc (part 2). This more-artistic side of things is something we want users to be able to control with a selection of dials.

Upcoming: a walk-through of using the software - how to "write" a song in a format that the Pi can interpret, how to start the song, and how to control integration of environmental triggers

Maybe upcoming: notes about the development process, lessons and best practices learned, etc.
