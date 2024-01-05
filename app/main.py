import socket, threading
def connectts(ip):
    global server, port, client
    server=ip
    port=4000
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server, port))
def send(msg):
    try:
        message=msg.encode('utf-8')
        msg_len=len(message)
        send_len=str(msg_len).encode('utf-8')
        send_len += b' ' * (640 - len(send_len))
        client.send(send_len)
        client.send(message)
    except:
        pass
import kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
from kivy.app import App
from kivy import platform
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.lang.parser
#import global_idmap
all_keys=['ctrl', 'shift', 'enter', 'alt', 'winleft', 'escape', 'space', 'backspace', 'tab', 'linefeed', 'clear', 'return', 'pause', 'scroll_lock', 'sys_req', 'delete', 'home', 'left', 'up', 'right', 'down', 'page_Up', 'Page_down', 'end', 'menu', 'help', 'break', 'num_lock', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '\\`', '~', '!', '@', '#', '$', '%', '^', '&', '\\*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', '/', '?', '.', '>', ',', '<', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
data={"connected": False}
def customfile(operation="r", data=[]):
    if operation=="r":
        with open('custom.txt') as file:
            return eval(file.read())
    if operation=="w":
        with open('custom.txt', "w") as file:
            text=eval(file.read())
            text[data[0]]=data.remove(data[0])
            file.write(text)
class Custom(Screen):
    pass
class CustomMade(Screen):
    pass
class more(Screen):
    pass
class MyGrid(Screen):
    pass
class mac(App):
    def build(self):
        return MyGrid()

    def btn(ait):
        if data["connected"]==False:
            threading.Thread(target=connectts(ait.root.ids.hip.text)).start()
            data["connected"]=True
    
    def custom(ait):
        ait.Custom=Custom()
        ait.root.add_widget(ait.Custom)
    
    def more(ait):
        ait.More=more()
        ait.root.add_widget(ait.More)
        
#/mnt/c/Users/itaya/Documents/android_app
    def run_moti(ait2):send("rm")
    def add_custom_python(ait2):
        pass
    def add_custom_giopty(ait2):
        pass
    def run_program(ait2):
        #test123=ait2.root.ids.runp.text
        #print(str(ait2.root.ids.runp.text))
        send(f'rp {ait2.root.ids.runp.text}')
    def keyboard(ait2):
        if ait2.root.ids.KeyboardInput_one.text in all_keys or len(ait2.root.ids.KeyboardInput_one.text)==0:
            if ait2.root.ids.KeyboardInput_two.text in all_keys or len(ait2.root.ids.KeyboardInput_two.text)==0:
                if ait2.root.ids.KeyboardInput_three.text in all_keys or len(ait2.root.ids.KeyboardInput_three.text)==0:
                    if ait2.root.ids.KeyboardInput_four.text in all_keys or len(ait2.root.ids.KeyboardInput_four.text)==0:
                        sts=''
                        if len(ait2.root.ids.KeyboardInput_one.text)==0:
                            pass
                        else:
                            sts+=ait2.root.ids.KeyboardInput_one.text + ";"
                        if len(ait2.root.ids.KeyboardInput_two.text)==0:
                            pass
                        else:
                            sts+=ait2.root.ids.KeyboardInput_two.text + ";"
                        if len(ait2.root.ids.KeyboardInput_three.text)==0:
                            pass
                        else:
                            sts+=ait2.root.ids.KeyboardInput_three.text + ";"
                        if len(ait2.root.ids.KeyboardInput_four.text)==0:
                            pass
                        else:
                            sts+=ait2.root.ids.KeyboardInput_four.text
                        send(f"k {sts}")
    def open_link_on_chrome(ait2):
        send(f"oloc {ait2.root.ids.openl.text}")
    def ktype(ait2):
        send(f't {ait2.root.ids.ktype.text}')
    def click(ait2):
        try:
            x=str(float(ait2.root.ids.click_pos_x.text))
            y=str(float(ait2.root.ids.click_pos_y.text))
            send(f'c {x};{y}')
        except:
            pass
    def disconnect_on_first_screen(ait2):
        data["connected"]=False
        send("disconnect")
    def on_stop(self):
        send("disconnect")
    def send_code(ait2):
        send(f"ec {ait2.Custom.ids.code.text}")
    def send_code_giopty(ait2):
        pass
    def system_command(ait2):
        send(f"sc {ait2.root.ids.command.text}")
    def back_from_custom(ait2):
        ait2.root.remove_widget(ait2.Custom)
    def back_from_more(ait2):
        ait2.root.remove_widget(ait2.More)
    def open_custom_commands(ait2):
        pass
    def rickroll(ait2):
        send(f"rr {ait2.Custom.ids.RickrollTitle.text}")
    def windowsalert(ait2):
        send(f"al {ait2.Custom.ids.WindowsAlertTitle.text};{ait2.Custom.ids.WindowsAlertText.text}")
    def onlymusicrickroll(ait2):
        send("rrm")
    def register_video(ait2):
        send(f"rnv {ait2.Custom.ids.id.text};{ait2.Custom.ids.videourl.text}")
    def play_registered_video(ait2):
        send(f"prv {ait2.Custom.ids.title.text};{ait2.Custom.ids.idtp.text}")
    def blackscreen(ait2):
        send(f"bs {ait2.Custom.ids.bss.text}")
    def enableuac(ait2):
        send("eu ")
    def enabletaskmanager(ait2):
        send("etm ")
    def tts(ait2):
        send(f"tts {ait2.More.ids.ttstext.text}")
    def enablep(ait2):
        send(f"ep {ait2.More.ids.ptdname.text};{ait2.More.ids.ptdindex.text}")
    def disablep(ait2):
        send(f"ep {ait2.More.ids.ptdindex.text}")
    def efd(ait2):
        send("efd ")
    def dfd(ait2):
        send("dfd ")
    def udw(ait2):
        send("udw  ")

if __name__ == "__main__":
    mac().run()