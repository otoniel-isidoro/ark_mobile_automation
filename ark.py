# -*- encoding=utf8 -*-
__author__ = "toni (otoniel.isidoro@gmail.com)"

from airtest.core.api import *
import time;

start_app('com.studiowildcard.wardrumstudios.ark')


def any_element_exists(elements):
    exist = False
    for element in elements:
        if exists(element):
            exist = True
            break
    return exist

def wait_for_any_element(elements, timeout=60):
    ts = time.time()
    print("wait for elements {} within timeout {} ".format(str(elements), str(timeout)))
    ret = True
    while not any_element_exists(elements):
        print(">> time elapsed:" + str(int(time.time() - ts)) + " seconds")
        if (int(time.time() - ts)) > timeout:
            ret = False
            break
    return ret   

def go_to_bag():
    if wait_for_any_element([Template(r"bag.png", threshold=0.5999999999999999, rgb=True, target_pos=5, record_pos=(-0.422, -0.207), resolution=(1520, 720)), Template(r"bag_open.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.421, -0.21), resolution=(1520, 720)), Template(r"bag_closed.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.423, -0.209), resolution=(1520, 720))], timeout=30):
        if exists(Template(r"bag_open.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.421, -0.21), resolution=(1520, 720))):
            touch(Template(r"bag_open.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.421, -0.21), resolution=(1520, 720)))
        elif exists(Template(r"bag.png", threshold=0.5999999999999999, rgb=True, target_pos=5, record_pos=(-0.422, -0.207), resolution=(1520, 720))):
            touch(Template(r"bag.png", threshold=0.5999999999999999, rgb=True, target_pos=5, record_pos=(-0.422, -0.207), resolution=(1520, 720)))
        elif exists(Template(r"bag_closed.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.423, -0.209), resolution=(1520, 720))):
            touch(Template(r"bag_closed.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.423, -0.209), resolution=(1520, 720)))
    
def watch_ad():
    go_to_bag()
    wait_for_any_element([Template(r"ambar.png", rgb=True, target_pos=5, record_pos=(0.318, -0.209), resolution=(1520, 720))], timeout=5)
    
    touch(Template(r"ambar.png", rgb=True, target_pos=5, record_pos=(0.318, -0.209), resolution=(1520, 720)), times=2)

    if wait_for_any_element([Template(r"watch_ad.png", record_pos=(-0.344, 0.138), resolution=(1520, 720))], timeout=5):
        touch(Template(r"watch_ad.png", record_pos=(-0.344, 0.138), resolution=(1520, 720)))
        wait_for_any_element([Template(r"close_ad.png", threshold=0.75, record_pos=(0.442, -0.917), resolution=(720, 1520)), Template(r"close_ad_2.png", record_pos=(0.397, -0.199), resolution=(1520, 720)), Template(r"googleplay.png", record_pos=(-0.267, -0.164), resolution=(1520, 720))], timeout=60)
        if exists(Template(r"googleplay.png", record_pos=(-0.267, -0.164), resolution=(1520, 720))):
            keyevent("BACK")
            sleep(2)
        if exists(Template(r"close_ad_2.png", record_pos=(0.397, -0.199), resolution=(1520, 720))):
            touch(Template(r"close_ad_2.png", record_pos=(0.397, -0.199), resolution=(1520, 720)))
        elif exists(Template(r"close_ad.png", record_pos=(0.442, -0.917), resolution=(720, 1520))):
            touch(Template(r"close_ad.png", record_pos=(0.442, -0.917), resolution=(720, 1520)))
    
def start_from_main_screen():
    touch(Template(r"play_ark.png", threshold=0.49999999999999983, record_pos=(-0.371, -0.195), resolution=(1520, 720)))
    if wait_for_any_element([Template(r"rejoin_session.png", record_pos=(0.023, -0.084), resolution=(1520, 720))], timeout=10):
        touch(Template(r"rejoin_button.png", record_pos=(-0.107, 0.063), resolution=(1520, 720)))
    else:
        wait_for_any_element([Template(r"play_multiplayer.png", record_pos=(0.194, -0.022), resolution=(1520, 720))], timeout=10)

        touch(Template(r"play_multiplayer.png", record_pos=(0.194, -0.022), resolution=(1520, 720)))

        wait_for_any_element([Template(r"server_settler_rock.png", threshold=0.75, record_pos=(-0.287, -0.093), resolution=(1520, 720))], timeout=10)

        touch(Template(r"server_settler_rock.png", record_pos=(-0.287, -0.093), resolution=(1520, 720)))

        wait_for_any_element([Template(r"server_settler_rock_info.png", record_pos=(-0.231, -0.174), resolution=(1520, 720))], timeout=10)

        wait_for_any_element([Template(r"join_button.png", record_pos=(0.284, 0.178), resolution=(1520, 720))],  timeout=10)

        touch(Template(r"join_button.png", record_pos=(0.284, 0.178), resolution=(1520, 720)))
    
def take_the_gift():
    if exists(Template(r"free_gift.png", threshold=0.6499999999999999, rgb=True, target_pos=5, record_pos=(0.384, -0.209), resolution=(1520, 720))):
        touch(Template(r"free_gift.png", threshold=0.65, rgb=True, target_pos=5, record_pos=(0.384, -0.209), resolution=(1520, 720)))
        touch(Template(r"ok_button.png", record_pos=(0.016, 0.053), resolution=(1520, 720)))

def respawn_at_bed():
    if wait_for_any_element([Template(r"survivor_died.png", record_pos=(0.016, -0.11), resolution=(1520, 720))], timeout=20):
        touch(Template(r"ok_button.png", record_pos=(0.016, 0.053), resolution=(1520, 720)))

    if wait_for_any_element([Template(r"bed.png", record_pos=(-0.28, -0.041), resolution=(1520, 720))]):
        touch(Template(r"bed.png", record_pos=(-0.28, -0.041), resolution=(1520, 720)))
        if wait_for_any_element([Template(r"respawn_bed.png", record_pos=(0.334, 0.184), resolution=(1520, 720))], timeout=20):
            touch(Template(r"respawn_bed.png", record_pos=(0.334, 0.184), resolution=(1520, 720)))
        
        
if exists(Template(r"ok_button.png", record_pos=(0.016, 0.053), resolution=(1520, 720))): #tenta clicar no ok caso de timeout
    touch(Template(r"ok_button.png", record_pos=(0.016, 0.053), resolution=(1520, 720)))
if wait_for_any_element([Template(r"bag.png", threshold=0.5999999999999999, rgb=True, target_pos=5, record_pos=(-0.422, -0.207), resolution=(1520, 720)), Template(r"bag_open.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.421, -0.21), resolution=(1520, 720)), Template(r"bag_closed.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.423, -0.209), resolution=(1520, 720)),Template(r"play_ark.png", threshold=0.49999999999999983, rgb=True, record_pos=(-0.371, -0.195), resolution=(1520, 720)),Template(r"bed.png", record_pos=(-0.28, -0.041), resolution=(1520, 720))]):
    if exists(Template(r"play_ark.png", threshold=0.49999999999999983, rgb=True, record_pos=(-0.371, -0.195), resolution=(1520, 720))):
        start_from_main_screen()
        respawn_at_bed()
    elif exists(Template(r"bed.png", record_pos=(-0.28, -0.041), resolution=(1520, 720))):
        respawn_at_bed()    

    go_to_bag()

try:
    watch_ad()  
except:
    print("ainda não habilitou o botão para assistir anuncio")
finally:    
    take_the_gift()
    touch(Template(r"close_bag.png", threshold=0.5999999999999999, target_pos=5, record_pos=(0.447, -0.206), resolution=(1520, 720)))

auto_setup(__file__)



