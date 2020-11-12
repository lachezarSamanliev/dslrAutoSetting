from Camera import *
from analyze_sides import *
from separate_circles import *
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
from subprocess import call

global cam
global scan
global circle
scan = Scanner
cam = Camera
circle = Circle
picID = "pic"
save_location = "/var/www/html/gallery/"  
def trigger_and_color():
    os.chdir(save_location)
    call(["gphoto2", "--delete-all-files"])
    call(["gphoto2", "--capture-image-and-download", "--force-overwrite"])
    sleep(2)
    shot_date = datetime.now().strftime("%Y-%m-%d")
    shot_time = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    clearCommand = ["gphoto2","--folder","/store_00010001/DCIM/100D5100", "-R", "--delete-all-files"]
    downloadCommand = ["--get-all-files"]
    full_name_file = shot_time + ".JPG"
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
                
    result_scan = scan.enlarge_circles(fixed_time + ".JPG")
    final_iso = cam.get_camera_setting("iso")
    sleep(1)
    final_shutter = cam.get_camera_setting("shutter")
    sleep(1)
    final_aperture = cam.get_camera_setting("aperture")
    sleep(1)
    
    write_quote = final_shutter+ " " + final_aperture + " " + final_iso + " " + result_scan + " " + fixed_time + ".JPG"
    file = open("colorsResults.txt", "a")
    file.write(write_quote)
    file.write("\n")
    file.close()    
    print(result_scan)    
trigger_and_color()
    

    
    
    
    
    

