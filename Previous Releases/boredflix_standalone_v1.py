from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.label import MDLabel
import threading
import requests
import requests_cache
from kivy.utils import platform
import subprocess
import sys
from kivymd.uix.spinner import MDSpinner
from kivy.metrics import dp
from kivy.uix.modalview import ModalView

if platform == 'android':
    from jnius import autoclass, cast

    def open_url(url):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        browserIntent = Intent()
        browserIntent.setAction(Intent.ACTION_VIEW)
        browserIntent.setData(Uri.parse(url))
        currentActivity = cast('android.app.Activity', activity)
        currentActivity.startActivity(browserIntent)
else:
    import webbrowser


magnets = []
inp = """
MDTextField:
    hint_text: "B O R E D F L I X"
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

class ItemConfirm(OneLineAvatarIconListItem):

    divider = None

    def set_icon(self, instance_check):
        def thrs(magnet_link: str, download: bool):
            thread1 = threading.Thread(target=webtorrent_stream,args=(magnet_link,download))
            thread2= threading.Thread(target=displ)
            thread2.start()
            thread1.start()
        def displ():
            pass
        def webtorrent_stream(magnet_link: str, download: bool):
            try:
                cmd = []
                cmd.append("webtorrent")
                cmd.append(magnet_link)
                if not download:
                    cmd.append('--mpv')

                if sys.platform.startswith('linux'):
                    subprocess.call(cmd)
                elif sys.platform.startswith('win32'):
                    subprocess.call(cmd, shell=True)
            except:
                try:
                    cmd = []
                    cmd.append("webtorrent")
                    cmd.append(magnet_link)
                    if not download:
                        cmd.append('--vlc')

                    if sys.platform.startswith('linux'):
                        subprocess.call(cmd)
                    elif sys.platform.startswith('win32'):
                        subprocess.call(cmd, shell=True)

                except:

                    MDDialog(title="Error...", text="No valid media player found, try again after installing mpv or vlc").open()
                
                        
        num = 0
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            num = num+1
            if check != instance_check:
                check.active = False
            else:
                self.spinner = MDSpinner(size_hint=(0.5, 0.5))
                mod = ModalView(background_color=(0,0,0,0))
                mod.add_widget(self.spinner)
                mod.open()
                num = int(num - int(num/3)*3)
                if num == 1:
                    if platform == 'android':
                        open_url(magnets[-3])
                    else:
                        thrs(magnets[-3],download=False)

                elif num == 2:
                    if platform == 'android':
                        open_url(magnets[-2])
                    else:
                        thrs(magnets[-2],download=False)

                else:
                    if platform == 'android':
                        open_url(magnets[-1])
                    else:
                        thrs(magnets[-1],download=False)

                num = 0


class BoredFlix(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.primary_hue = "800"
        self.theme_cls.theme_style = "Dark"

        screen = Screen()
        btn = MDRectangleFlatButton(text='Search', pos_hint={
                                    'center_x': 0.5, 'center_y': 0.42}, line_width=1.2, on_release=self.fin)
        screen.add_widget(btn)
        # l1 = MDLabel(text='Hello world', halign='center',
        #              theme_text_color='Custom', text_color=(255/255.0, 100/255.0, 103/255.0, 1), font_style='Button')
        # screen.add_widget(l1)
        self.m = Builder.load_string(inp)
        screen.add_widget(self.m)
        self.dic = Builder.load_string(KV)
        screen.add_widget(self.dic)
        self.loading_label = MDLabel(
        text='Loading', halign='center', theme_text_color='Custom', text_color=(1, 1, 1, 1), font_style='Subtitle1', pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.loading_label.opacity = 0
        screen.add_widget(self.loading_label)

        return screen

    def close(self, obj):
        self.dia.dismiss()

    def cut(self,obj):
        self.err.dismiss()

    def shut(self, obj):
        self.cri.dismiss()

    def show_loading(self):
        self.loading_label.opacity = 1

    def hide_loading(self):
        self.loading_label.opacity = 0
    def fin(self, obj): 
        movie = self.m.text.replace(' ', '%20')
        requests_cache.install_cache('demo_cache')
        head ={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36'}
        s = requests.Session()
        Star=False
        def pway(movie,Star,head):
            if Star==True:
                pass
            else:
                Star=True
                requests_cache.clear()
            return (s.get(
                "YOUR SOURCE HERE",headers=head)).text
        try:
            self.show_loading()
            f = pway(movie,Star,head)
            self.hide_loading()

        except:
            self.hide_loading()
            first = MDRectangleFlatButton(
                text="Back", line_width=1.23, on_release=self.cut)
            self.err=MDDialog(title="Error",text="Check your internet connection or spelling",buttons=[
                                    first,
                                ])
            self.err.open()
            return

        titl = f.split('title="Details for ', 3)
        f = f.split('<a href="magnet:', 3)
        titls = []
        for i in range(1, 4):
            try:
                titls.append(str(i)+'. '+titl[i][:titl[i].index('">')])
                magnets.append("magnet:" + f[i][:f[i].index('"')])
            except:
                pass
        emp = []
        if titls == []:
            firstt = MDRectangleFlatButton(
                text="Back", line_width=1.23, on_release=self.shut)
            self.cri = MDDialog(
                title="Sorry...", text="Your search returned no results.\nPlease check for spacing and spelling errors and try again",  buttons=[firstt,])
            self.cri.open()
        else:
            for j in titls:
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
            self.dia.open()


BoredFlix().run()
