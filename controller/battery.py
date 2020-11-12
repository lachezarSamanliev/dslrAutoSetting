from sh import gphoto2 as gp
import signal, os, subprocess
from subprocess import call  
def get_num(battery_output):
    temp = battery_output
    temp_final = 0
    if temp[0] == "%":
        t = 0
    else :
        temp_final = temp[0]
    if temp[1] == "%":
        t = 1
    else :
        temp_final = temp_final + temp[1]
    if temp[2] == "%":
        t = 2
    else :
        temp_final = temp_final + temp[2]
    return temp_final
def get_battery():
    out = subprocess.Popen(['gphoto2', '--get-config', '/main/status/batterylevel'],
                           stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    stdout,stderr = out.communicate()
    topa = str(stdout)
    topa = topa.split()
    final_num = get_num(topa[5])

    print(final_num)
    return final_num  
get_battery()