from sh import gphoto2 as gp
from time import sleep
import signal, os, subprocess
from analyze_sides import *
from subprocess import call
import random
class Camera:
    global iso_list
    iso_list = [100,125,160,200,250,320,400,500,640,800,1000,1250,1600,2000,2500,3200,4000,5000,64000,8000,10000]
    global shutter_list
    global aperture_list
    def get_num(reading):
        temp = reading
        temp_final = 0
        barrier = "\\"
        if temp[0] == barrier:
            t = 0
        else :
            temp_final = temp[0]
        if temp[1] == barrier:
            t = 1
        else :
            temp_final = temp_final + temp[1]
        if temp[2] == barrier or temp[2] == "n" or temp[2] == "B":
            t = 2
        else :
            temp_final = temp_final + temp[2]

        if temp[3] == barrier or temp[3] == "n" or temp[3] == "B":
            t = 2
        else :
            temp_final = temp_final + temp[3]
        if temp[4] == barrier or temp[4] == "n" or temp[4] == "B":
            t = 2
        else :
            temp_final = temp_final + temp[4]
        return temp_final   

    def get_camera_setting(setting_choice):
            
        if setting_choice == "iso":
            list_space = 5
            command = '/main/imgsettings/iso'
        elif setting_choice == "shutter":
            list_space = 6
            command = '/main/capturesettings/shutterspeed2'
        elif setting_choice == "aperture":
            list_space = 6
            command = '/main/capturesettings/f-number'
        elif setting_choice == "lightmeter":
            list_space = 5
            command = '/main/status/lightmeter'
        
        out = subprocess.Popen(['gphoto2', '--get-config', command],
                           stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        stdout,stderr = out.communicate()
        output = str(stdout)
        output = output.split()
        result = Camera.get_num(output[list_space])
        return result
    
    def change_camera_setting(setting_choice, value_in_list):
        value = str(value_in_list)
        if setting_choice == "iso":
            command = '/main/imgsettings/iso=' + value
        elif setting_choice == "shutter":
            list_space = 6
            command = '/main/capturesettings/shutterspeed=' + value
        elif setting_choice == "aperture":
            list_space = 6
            command = '/main/capturesettings/f-number=' + value
            
        out = subprocess.Popen(['gphoto2', '--set-config', command],
                           stdout = subprocess.PIPE)
    
    def get_list_settings(setting_choice):
        temp_setting = setting_choice
        
        path = "/var/www/html/SP_photo/model/"
        if temp_setting == "iso":
            list_space = 5
            path = path + "iso.txt"
        elif temp_setting == "shutter":
            list_space = 6
            path = path + "shutter.txt"
        elif temp_setting == "aperture":
            list_space = 6
            path = path + "aperture.txt"

        f = open(path, "r")
        lines = f.read().splitlines()
        f.close()
        return lines
        temper.config(text=final)     
    def make_random_setting(setting_choice):
        setting = setting_choice
        if setting == "iso":
            position = random.randint(0,19)
        elif setting == "aperture":
            position = random.randint(0,16)
        elif setting == "shutter":
            position = random.randint(0,17)          
        Camera.change_camera_setting(setting, position)      
    def move_iso(value_iso):
        current_value = value_iso
        db_list = cam.get_list_settings("iso")
        current_position = db_list.index(current_value)
        good_position = db_list.index("800") 
        scan = Scanner
        difference = scan.get_difference(current_position, good_position)
        if difference > 3:
            movement = int((difference / 2) + 2)
            if current_position > good_position:
                moved_index = current_position - movement
                Camera.change_camera_setting("iso", moved_index)
            elif current_position < good_position:
                moved_index = current_position + movement
                Camera.change_camera_setting("iso", moved_index)
        else:
            if current_position > good_position:
                moved_index = current_position - 1
                Camera.change_camera_setting("iso", moved_index)
            elif current_position < good_position:
                moved_index = current_position + 1
                Camera.change_camera_setting("iso", moved_index)          
    def random_setting_change():
        setting_chosen = random.randint(0,1)
        return setting_chosen
    
    def move_s_and_a(value_shutter, value_aperture):
        scan = Scanner
        
        path = "/var/www/html/SP_photo/model/shutter.txt"
        path_two = "/var/www/html/SP_photo/model/aperture.txt"
        f = open(path, "r")
        lines_shutter = f.read().splitlines()
        f.close()
        f_two = open(path_two, "r")
        lines_aperture = f_two.read().splitlines()
        f_two.close()
        print("HERE1")
        print(value_shutter)
        print(value_aperture)
        current_position_s = lines_shutter.index(value_shutter)
        min_position_s = lines_shutter.index("1/4000")
        max_position_s = lines_shutter.index("1")
        current_position_a = lines_aperture.index(value_aperture)
        min_position_a = lines_aperture.index("f/5")
        max_position_a = lines_aperture.index("f/32")
        random_setting = cam.random_setting_change()
        point_s = scan.get_difference(current_position_s, min_position_s)
        point_two_s = scan.get_difference(current_position_s, max_position_s)
            
        point_a = scan.get_difference(current_position_a, min_position_a)
        point_two_a = scan.get_difference(current_position_a, max_position_a)
        print(random_setting)
        if random_setting == 0:
            if point_s < point_two_s:
                print(current_position_s)
                current_position_s = current_position_s + 3
                print(current_position_s)
                if point_a < point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a + 1
                    print(current_position_a)
                elif point_a > point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a - 1
                    print(current_position_a)
                else:
                    print("keep1")
            elif point_s > point_two_s:
                print(current_position_s)
                current_position_s =current_position_s- 3
                if point_a < point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a + 1
                    print(current_position_a)
                elif point_a > point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a - 1
                    print(current_position_a)
                else:
                    print("keep2")
                    print(current_position_s)
            else:
                print("keep3")
        elif random_setting == 1:
            if point_s < point_two_s:
                print(current_position_s)
                current_position_s = current_position_s + 1
                print(current_position_s)
                if point_a < point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a + 3
                    print(current_position_a)
                elif point_a > point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a - 3
                    print(current_position_a)
                else:
                    print("keep4")
            elif point_s > point_two_s:
                print(current_position_s)
                current_position_s = current_position_s- 1
                if point_a < point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a + 3
                    print(current_position_a)
                elif point_a > point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a - 3
                    print(current_position_a)
                else:
                    print("keep5")
                    print(current_position_s)
            else:
                print("keep6")
        else:
            if point_s < point_two_s:
                print(current_position_s)
                current_position_s = current_position_s + 1
                print(current_position_s)
                if point_a < point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a + 1
                    print(current_position_a)
                elif point_a > point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a - 1
                    print(current_position_a)
                else:
                    print("keep7")
            elif point_s > point_two_s:
                print(current_position_s)
                current_position_s = current_position_s- 1
                if point_a < point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a + 1
                    print(current_position_a)
                elif point_a > point_two_a:
                    print(current_position_a)
                    current_position_a = current_position_a - 1
                    print(current_position_a)
                else:
                    print("keep8")   
        cam.change_camera_setting("shutter", current_position_s)
        sleep(1)
        cam.change_camera_setting("aperture", current_position_a)
        sleep(1)
    def make_good_settings():
        scan = Scanner
        lightmeter_target = -1
        value_iso = cam.get_camera_setting("iso")
        sleep(0.5)
        value_shutter = cam.get_camera_setting("shutter")
        sleep(0.5)
        value_aperture = cam.get_camera_setting("aperture")
        sleep(0.5)
        Camera.move_iso(value_iso)
        sleep(1)
        value_light_meter = cam.get_camera_setting("lightmeter")  
        good_position_l = -1
        current_position_l = int(value_light_meter)
        result_l = scan.get_difference(good_position_l, current_position_l)
        while result_l > 4:
            #invoke changes
            sleep(3)
            #make change
            cam.move_s_and_a(value_shutter, value_aperture)
            print("changed")
            #getting the lighmeter value again
            sleep(0.5)
            again = cam.get_camera_setting("lightmeter")
            sleep(0.5)
            result_l = scan.get_difference(good_position_l, int(again))
            sleep(1)
            
        
            

        
        
    
#cam = Camera
#cam.make_good_settings()
#value_lightmeter = cam.get_camera_setting("lightmeter")
#print(value_lightmeter)
#cam.get_iso()
#cam.get_shutter()
#print(cam.get_camera_setting("aperture"))
#print(cam.get_camera_setting("iso"))
#print(cam.get_camera_setting("shutter"))
#print(cam.get_camera_setting("lightmeter"))

#sleep between changes because Camera needs to catch up
#cam.change_camera_setting("aperture", 2)
#sleep(1)
#cam.change_camera_setting("shutter", 2)
#sleep(1)
#cam.change_camera_setting("iso", 2)
#sleep(1)
#cam.make_random_setting("iso")
