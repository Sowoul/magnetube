from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.clock import mainthread
import threading
import requests
import requests_cache
import subprocess
from kivymd.uix.spinner import MDSpinner
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
import tempfile
import atexit
import shutil
import multiprocessing as mp
from flask import Flask, Response, render_template
from kivy.clock import Clock
from requests import request
from host import strms
from flaskwebgui import FlaskUI
temp_dir = tempfile.TemporaryDirectory()
atexit.register(temp_dir.cleanup)

magnets = []
inp = """
MDTextField:
    hint_text: "M A G N E T U B E"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    icon_right: "movie-outline"
    size_hint_x: 0.4
    width:300
"""

KV = '''
<ItemConfirm>
    on_release: root.set_icon(check)
    CheckboxLeftWidget:
        id: check
        group: "check"
MDFloatLayout:
'''

colors = {
    "Teal": {
        "200": "#212121",
        "500": "#212121",
        "700": "#212121",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#202020",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
}

spnr = '''
MDScreen:
      
    MDSpinner:
        size_hint: None, None
          
        size: dp(46), dp(46)
          
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
          
        active: True
'''

justar = True
try:
    requests_cache.clear()
except:
    pass


class ItemConfirm(OneLineAvatarIconListItem):
    stre = False
    divider = None

    def delete_downloads():
        try:
            shutil.rmtree(temp_dir.name)
        except Exception as e:
            print(f"Failed to delete downloads: {str(e)}")

    def set_icon(self, instance_check):
        def thrs(magnet_link: str, download: bool):
            Clock.schedule_once(
                lambda da: webtorrent_stream(magnet_link, download))

        @mainthread
        def erro():
            MDDialog(
                title="Error...", text="No valid media player found, try again after installing mpv or vlc").open()

        def webtorrent_stream(magnet_link: str, download: bool):
            try:
                app = strms(magnet_link=magnet_link)
                threading.Thread(target=FlaskUI(
                    app=app, server="flask").run).start()
            finally:
                print('Cache cleared')
        num = 0

        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            num = num+1
            if check != instance_check:
                check.active = False
            else:
                self.spinner = MDSpinner(size_hint=(0.5, 0.5))
                self.mod = ModalView(background_color=(0, 0, 0, 0))
                self.mod.add_widget(self.spinner)
                self.mod.open()
                num = int(num - int(num/3)*3)
                if num == 1:
                    thrs(magnets[-3], download=False)

                elif num == 2:
                    thrs(magnets[-2], download=False)

                else:
                    thrs(magnets[-1], download=False)

                num = 0


class Magnetube(MDApp):
    def reset(self):
        self.screen.remove_widget()

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.primary_hue = "800"
        self.theme_cls.theme_style = "Dark"

        self.screen = Screen()
        btn = MDRectangleFlatButton(text='Search', pos_hint={
                                    'center_x': 0.5, 'center_y': 0.42}, line_width=1.2, on_release=self.fin1)
        self.screen.add_widget(btn)
        self.m = Builder.load_string(inp)
        self.screen.add_widget(self.m)
        self.dic = Builder.load_string(KV)
        self.screen.add_widget(self.dic)

        return self.screen

    def close(self, obj):
        self.dia.dismiss()

    def cut(self, obj):
        self.err.dismiss()

    def shut(self, obj):
        self.cri.dismiss()

    @mainthread
    def loading(self, *args):
        self.spinner = MDSpinner(size_hint=(0.5, 0.5))
        self.mod = ModalView(background_color=(0, 0, 0, 0))
        self.mod.add_widget(self.spinner)
        self.mod.open()

    def fin1(self, obj):
        threading.Thread(target=self.fin).start()

    @mainthread
    def disp(self, *args):
        emp = []
        if self.titls == []:
            firstt = MDRectangleFlatButton(
                text="Back", line_width=1.23, on_release=self.shut)
            self.cri = MDDialog(
                title="Sorry...", text="Your search returned no results.\nPlease check for spacing and spelling errors and try again",  buttons=[firstt,])
            self.cri.open()
        else:
            for j in self.titls:
                emp.append(ItemConfirm(text=j))
            first = MDRectangleFlatButton(
                text="Back", line_width=1.23, on_release=self.close)
            self.dia = MDDialog(title=f'Results for "{self.m.text}"',
                                type="confirmation",
                                items=emp,
                                buttons=[
                                    first,
                                ],
                                )
            self.mod.dismiss()
            self.dia.open()

    def fin(self):
        temp_dir.cleanup
        self.loading()
        movie = self.m.text.replace(' ', '+')
        requests_cache.install_cache('demo_cache')
        head = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36'}
        s = requests.Session()

        def pway(movie, head):
            return (s.get(f"http://localhost:5000/search/?keyword={movie}", headers=head)).text
        try:
            f = pway(movie, head)
        except:
            first = MDRectangleFlatButton(
                text="Back", line_width=1.23, on_release=self.cut)
            self.err = MDDialog(title="Error", text="Check your internet connection or spelling", buttons=[
                first,
            ])
            self.err.open()
            return

        titl = f.split('<strong>Title:</strong>', 3)
        f = f.split('<strong>Magnet Link:</strong>', 3)

        self.titls = []
        for i in range(1, 4):
            try:
                self.titls.append(str(i)+'. '+titl[i][:titl[i].index('<')])
                magnets.append("magnet:" + f[i][:f[i].index('\n')])
            except:
                pass
        self.disp()


try:
    Magnetube().run()
finally:
    requests_cache.clear()
