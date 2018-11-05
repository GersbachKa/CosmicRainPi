# CosmicRainPi
This software is meant to run on a Raspberry Pi 3, running Raspbian

[Some more text about the system that I'm too lazy to add right now]

General outline:

The goal of this software is to command a Pi to autonomously play a Ukelele. The software is comprised of two main parts: 1) motor control and 2) environmental integration. Generally, a user will input a song in a specific format that the software can interpret. Then the Pi will command a set of motors to fret and pluck a Ukelele to play the song (part 1). Simultaneously, the Pi will sense its enviroment for changes in temperature, light, and the presence of radiation using a geiger counter. In response to signals from one of these sensors, the song being played will be modulated - so a song beginning in one register may end in another, or notes may be added, etc (part 2). This more-artistic side of things is something we want users to be able to control with a selection of dials.

Upcoming: a walk-through of using the software - how to "write" a song in a format that the Pi can interpret, how to start the song, and how to control integration of environmental triggers

Maybe upcoming: notes about the development process, lessons and best practices learned, etc.
