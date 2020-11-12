from Camera import *
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
from subprocess import call

cam = Camera
sleep(3)
cam.make_random_setting("iso")
sleep(3)
cam.make_random_setting("aperture")
sleep(3)
cam.make_random_setting("shutter")
sleep(3)
one = cam.get_camera_setting("shutter")
two = cam.get_camera_setting("aperture")
three = cam.get_camera_setting("iso")
result = "Shutter " + one + two + "ISO " + three
print(result)