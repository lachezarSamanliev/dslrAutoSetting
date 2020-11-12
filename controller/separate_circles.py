#GOOOOOODDDDDDDDD
from multiprocessing import Process,Queue,Pipe
from PIL import Image
import numpy as np
from collections import Counter
class Circle:
    scale = [1,2,3,4,5,6,7,8,9,10]
    global centers_list
    global most_common_red
    centers_list = [(1232, 816), (1232, 2448), (2464, 1632), (3696, 816), (3696, 2448)]
    global circle_spot
    global reds
    global greens
    global blues
    reds = list()
    red = []
    greens = list()
    greens = []
    blues = list()
    blues = []
    def make_circle(img, circle_position, side, scale):
        img_open = Image.open(img)
        current_scale = scale
        current_side = side
        x = circle_position - 1
        circle_spot = circle_position
        #n  are used for the change between rectangle size
        n = 4
        n_opposite = 1
        #for x in range(0, 5):
        for x_two in range(0,4):
            #distinguish coordinates for four rectangles
            if current_side == 0:
            #distinguish coordinates for four rectangles
                rect_one_x_one = centers_list[x][0] - (n * (15 * scale))
                rect_one_y_one = centers_list[x][1]- (n_opposite * (20 * scale))
        
                rect_one_x_two = centers_list[x][0] - ((n-1) * (15 * scale))
                rect_one_y_two = centers_list[x][1] + ((n_opposite) * (20 * scale))
            elif current_side == 1:
                rect_one_x_one = centers_list[x][0] + ((n-1) * (15 * scale))
                rect_one_y_one = centers_list[x][1]- (n_opposite * (20 * scale))
           
                rect_one_x_two = centers_list[x][0] + ((n) * (15 * scale))
                rect_one_y_two = centers_list[x][1] + ((n_opposite) * (20 * scale))               #call cropping def
            crop_box = (rect_one_x_one, rect_one_y_one, rect_one_x_two, rect_one_y_two)
            region_temp = img_open.crop(crop_box)
            #region_temp.show()
            data_segment = np.array(region_temp.getdata())
            end = int(len(data_segment))
            #populates the list with B colors so they can be analyzed
            #min, max, occurences
            for i_temp in range(0, end):
            #blues.append(data_blue_sea[x])
                temp = data_segment[i_temp]
                blues.append(temp[2])
                reds.append(temp[0])
                greens.append(temp[1])
            n -= 1
            n_opposite += 1

            if n == 0:
                n = 4
            if n_opposite == 5:
                n_opposite = 1
    def show_trends():
        cnt_blue = Counter(blues)
        cnt_red = Counter(reds)
        cnt_green = Counter(greens)
        reds[:] = []
        greens[:] = []
        blues[:] = []
        most_common_red = str(cnt_red.most_common(5)[0][0])
        m_c_red = int(most_common_red)
        most_common_green = str(cnt_green.most_common(5)[0][0])
        m_c_green = int(most_common_green)
        most_common_blue = str(cnt_blue.most_common(5)[0][0])
        m_c_blue = int(most_common_blue)
        print(m_c_red)
        print(m_c_green)
        print(m_c_blue)
        return (m_c_red, m_c_green, m_c_blue)
    def find_trends():
        cnt_blue = Counter(blues)
        cnt_red = Counter(reds)
        cnt_green = Counter(greens)
        most_common_red = str(cnt_red.most_common(5)[0][0])
        m_c_red = int(most_common_red)
        most_common_green = str(cnt_green.most_common(5)[0][0])
        m_c_green = int(most_common_green)
        most_common_blue = str(cnt_blue.most_common(5)[0][0])
        m_c_blue = int(most_common_blue)      
        return (m_c_red, m_c_green, m_c_blue)


            
#opit = Circle

#opit.default_scan("grassStef.JPG")
        
        
        
        
        
    
    
    