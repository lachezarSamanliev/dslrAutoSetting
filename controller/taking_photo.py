from Camera import *
from analyze_sides import *
#from separate_circles import *
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
#import gphoto2 as gp
import signal, os, subprocess
from subprocess import call

global cam
global scan
scan = Scanner
cam = Camera
picID = "pic"
save_location = "/var/www/html/gallery/"
def trigger_camera():
    os.chdir(save_location)
    call(["gphoto2", "--delete-all-files"])
    call(["gphoto2", "--capture-image-and-download", "--force-overwrite"])
    sleep(2)
    shot_date = datetime.now().strftime("%Y-%m-%d")
    shot_time = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    clearCommand = ["gphoto2","--folder","/store_00010001/DCIM/100D5100", "-R", "--delete-all-files"]
    downloadCommand = ["--get-all-files"]
    fixed_time = shot_time
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".jpg"):
                os.rename(filename, (fixed_time + ".JPG"))
                print ("renamed jpeg")

            elif filename.endswith(".nef"):
                os.rename(filename, (fixed_time + ".NEF"))
                print ("renamed nef")
            else:
                print("Photo Taken")           
    value_iso = cam.get_camera_setting("iso")
    value_shutter = cam.get_camera_setting("shutter")
    value_aperture = cam.get_camera_setting("aperture")
    combined_response = ("Shutter " + str(value_shutter) + " " + str(value_aperture) + " " + "ISO " + str(value_iso))
    result_scan = scan.initial_scan(fixed_time + ".JPG")
    if result_scan[2] == 1:
        print(combined_response + " Photo is Bright")
    elif result_scan[2] == 0:
        print(combined_response + " Photo is Dark")
    else:
        print(combined_response + " Initial settings seem fine")
trigger_camera()

    

