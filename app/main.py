#!/usr/bin/python3

#TODO: Add the flash and require a login! And maybe add groups for multiple devices!

# Importing everything:
import re
import threading
import time
import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from plyer import flash
from plyer import notification
from plyer import vibrator

notification.notify(title="Started!", message="The application successfully started!", app_name="test")    #Let the user know that the application is now running (Optional)

global SERVER_ADDR                                                      #Global and define server adress
with open("server.txt", "r") as f:
    SERVER_ADDR = f.read()

class MyGrid(GridLayout):    #The gridlayout for the kivy app
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__()

        self.cols = 1

        #self.image = Image(source="easynotify.png")
        #self.add_widget(self.image)

        self.token = Label(text="* "*16, font_name="Mada-Bold.ttf", font_size="25dp")
        self.add_widget(Label(text=""))
        self.add_widget(self.token)
        #self.add_widget(Label(text=""))

        self.image = Image(source="img1.png", keep_ratio=False, allow_stretch=True, size_hint=(0.1, 0.7), pos=(400, -500))#pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.image)

        self.token_button = Button(text="Show Token", font_name="Mada-Bold.ttf", font_size="25dp", background_color=[255, 255, 255, 1], color=[0, 0, 0, 1])
        self.token_button.bind(on_press=self.show_token)
        self.add_widget(self.token_button)
    class check_new_request(threading.Thread):           #A thread which will check if there are any incomming messages
        def run(self):
            could_read = False
            while could_read == False:
                try:
                    with open("token.txt", "r") as f:
                        used_token = f.read()
                        could_read = True
                    while used_token == "none":
                        with open("token.txt", "r") as f:
                            used_token = f.read()
                        time.sleep(.3)
                except:
                    could_read = False
                time.sleep(1)
            while True:
                title = "error"
                while title == "error":           #If an error occurs the program will try it every 10 seconds again
                    try:
                        title = requests.post(SERVER_ADDR + "/readtitle/" + used_token).json() #Get the title
                    except:
                        print("error")
                        title = "error"
                        time.sleep(10)
                if title == "":
                    print("nothing")
                elif title == "invalid":
                    print("invalid:(")
                else:
                    info = requests.post(SERVER_ADDR + "/readinfo/" + used_token).json()    #Get additional info like vibration pattern
                    current_line = 0
                    boolean_do_vibrate = False
                    for line in info.splitlines():
                        current_line += 1
                        if current_line == 1:
                            regexp = re.compile("VIBRATE=(.*)$")       #Parsing the output from "info"
                            do_vibrate = regexp.search(line).group(1)
                            print(do_vibrate)
                            if do_vibrate == "True":
                                boolean_do_vibrate = True
                        if current_line == 2:
                            regexp = re.compile("PATTERN=(.*)$")
                            pattern = regexp.search(line).group(1)
                            if boolean_do_vibrate == True:
                                for letter in pattern:
                                    if letter == "a":
                                        try:
                                            vibrator.vibrate(.1)
                                        except:
                                            pass
                                        time.sleep(.07)
                                    if letter == "b":
                                        time.sleep(.1)
                        if current_line == 3:
                            regexp = re.compile("FLASH=(.*)$")              #Flash currently not working!
                            do_flash = regexp.search(line).group(1)
                            if do_flash == "True":
                                flash.on()
                                time.sleep(.2)
                                flash.off()

                    body = requests.post(SERVER_ADDR + "/readtext/" + used_token).json()    #Gets the content
                    notification.notify(body, title)
                    notification.notify(title=title, message=body, app_name="test")         #Finally - send message
                time.sleep(2)
    check_new_request().start()
    def show_token(self, instance):                                                         # show the token to the user
        global new_token
        if self.token.text == "* "*16:
            with open("token.txt", "r") as f:
                have_token = f.read()
            if have_token == "none":                                                        #if the user has no token, it will request one from the server
                with open("token.txt", "w") as f:
                    print("NEW TOKEN")
                    new_token = requests.post(SERVER_ADDR + "/gettoken").json()
                    have_token = new_token
                    print(str(new_token))
                    f.write(new_token)
                requests.post(SERVER_ADDR + "/addonecount/" + new_token)

            else:
                print("OLD TOKEN")
                with open("token.txt", "r") as f:
                    new_token = f.read()
            current_token = self.token
            print(current_token)
            self.token_button.text = "Hide Token"
            self.token.text = new_token
        else:
            self.token_button.text = "Show Token"
            self.token.text = "* "*16


class test(App):
    def build(self):
        return MyGrid()

test().run()

#Jonathan357611 on Github.
#Got any errors, ideas etc? Just message me!
#I know, my code is a mess, im still learning:)!