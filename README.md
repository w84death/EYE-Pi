# EYE-Pi
A Raspberry Pi camera for Infrared Photography

I read this tutorial [[https://www.raspberrypi.org/learning/python-picamera-setup/worksheet.md]] and modyfy the code to my needs. Also I added LED so I know when the camera is ready and making photo.

# Setup

## Hardware

- Raspberry Pi B+ (can be anything but not PiZero)
- Camera Module NoIR
- switch/Button
- LED + resistor
- PowerBank with 2.1Amps (it must be 2Amps!) or just use the wall adapter.

## Wires

- connect camera module to the camera slot (google how to proberly put the cable in!)
- connect button to the pin 17 and any ground
- connect LED (with resistor!) to the pin 4 and any ground

## Linux Enviroment

- rasbian Light (the ~300MB version)
- sudo raspi-config -> enable camera
- sudo apt-get install python-picamera python3-picamera python-rpi.gpio
- make folder for the camera stills
- put the camera script in ~/
- chmod +x EYE-Pi.sh

## Autorun
I did some changes to the linux to get:

- auto login as pi on boot
- autorun the script

I just use google/stackoverflow and finally get it to work. But it was chaotic and I do not remmember with command works best :)


# Usage

## Make photos

- run the raspberry and wait 20-30 sec to boot. 
- when the LED turns OFF this mean that camera script loaded and it's ready to shoot
- push the button :)
- LED on means that camera is making a photo and saving file
- wait for LED to turn OFF to make another picture

## Download photos

- sftp to the Pi
- download photos / delete old photos
- you can have open connection while making a photos
- just refresh and download new files

# WARNING
DO NOT EVER TURN OFF THE RASPBERRY AFTER MAKING A PHOTO! YOU WILL LOSE LAST PHOTOS!

- download photos on the go, or..
- turn off the camera after ~minute of idle
- TODO: add a button to power off the machine using "shutdown -h now"
