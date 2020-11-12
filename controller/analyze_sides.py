#GOOOOOODDDDDDDDD
from multiprocessing import Process,Queue,Pipe
import numpy as np
#from right_side import half_circle
from separate_circles import *
from collections import Counter
class Scanner:
    global scale_default
    scale_default = 4
    global location_pic
    location_pic = "/var/www/html/gallery/"
    global initial_result
    initial_result = []
    global color_scanned
    color_scanned = []
    def bright_or_dark(sum):
        current_sum = sum
        if current_sum > 560:
            return "Bright"
        elif current_sum < 210:
            return "Dark"
        else:
            return "Neither"
    def initial_scan(path):
        circle = Circle
        scan = Scanner
        temp_location = location_pic + path 
        for i in range (0,5):
            circle.make_circle(temp_location, i, 1, scale_default)
            circle.make_circle(temp_location, i, 0, scale_default)
            commons = circle.show_trends()
            red_result = commons[0]
            green_result = commons[1]
            blue_result = commons[2]
            #getting sum and evaluation
            sum_commons = red_result + green_result + blue_result
            sum_result = scan.bright_or_dark(sum_commons) 
            if sum_result == "Neither":
                initial_result.append(None)
            elif sum_result == "Dark":
                initial_result.append(0)
            else:
                initial_result.append(1)
        return initial_result
    def get_difference(expected, received):
        exp = expected
        rec = received
        result = 0
        if exp < rec:
            result = rec - exp
            return result
        elif exp > rec:
            result = exp - rec
            return result
        else:
            result = 1
            return result
    def is_there_color(red, green, blue):
        
        received_red = red
        received_green = green
        received_blue = blue
        
        red = [216, 36, 42]
        green = [115, 182, 60]
        blue = [117, 170, 225]
        
        diff_red = Scanner.get_difference(red[0], received_red)
        diff_green = Scanner.get_difference(green[1], received_green)
        diff_blue = Scanner.get_difference(blue[2], received_blue)
        
        diff_for_red = Scanner.get_difference(received_green ,received_red)
        diff_for_green = Scanner.get_difference(received_blue, received_green)
        diff_for_blue = Scanner.get_difference(received_red, received_blue) 
        if diff_red < 90 and diff_for_red > 42 :
            if received_green < 91:
                return "RED"
            elif received_green > 70:
                return "InconclusiveRED"
            else:
                return "NotClose"
        elif diff_green < 70 and diff_for_green > 40:
            if received_blue < 91:
                return "GREEN"
            elif received_blue > 70:
                return "InconclusiveGREEN"
            else:
                return "NotClose"
        elif diff_blue < 110 and diff_for_blue > 30:
            if received_red < 150:
                return "BLUE"
            elif received_blue > 70:
                return "InconclusiveBLUE"
            else:
                return "NotClose"
        else:
            return "Dem colors are unknown"
    def enlarge_circles(path):
        previous_path = path
        result = Scanner.initial_scan(previous_path)
        bigger_scale = 9
        circle = Circle
        scan = Scanner
        temp_location = location_pic + previous_path
        for i in range(0,5):
            if result[i] == None:
                circle.make_circle(temp_location, i, 1, bigger_scale)
                circle.make_circle(temp_location, i, 0, bigger_scale)
                commons = circle.find_trends()
            
                red_result = commons[0]
                green_result = commons[1]
                blue_result = commons[2]      
        color_estimate = scan.is_there_color(red_result, green_result, blue_result)
        return color_estimate
            
           