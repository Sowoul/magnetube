from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from urllib.request import Request, urlopen
import webbrowser

magnets = []

from kivy.lang import Builder
inp = """
MDTextField:
    hint_text: "B O R E D F L I X"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    icon_right: "movie-outline"
    size_hint_x: None
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


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        num = 0
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            num = num+1
            if check != instance_check:
                check.active = False
            else:
                num = int(num- int(num/3)*3)
                if num == 1:
                    webbrowser.open(magnets[-3])
                elif num == 2:
                    webbrowser.open(magnets[-2])
                else:
                    webbrowser.open(magnets[-1])
                num=0


class BoredFlix(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue= "500"
        self.theme_cls.primary_hue = "800"
        self.theme_cls.theme_style = "Dark"

        screen = Screen()
        btn = MDRectangleFlatButton(text='Search', pos_hint={
                                    'center_x': 0.5, 'center_y': 0.42},line_width=1.2, on_release=self.fin)
        screen.add_widget(btn)
        # l1 = MDLabel(text='Hello world', halign='center',
        #              theme_text_color='Custom', text_color=(255/255.0, 100/255.0, 103/255.0, 1), font_style='Button')
        # screen.add_widget(l1)
        self.m = Builder.load_string(inp)
        screen.add_widget(self.m)
        self.dic = Builder.load_string(KV)
        screen.add_widget(self.dic)

        return screen

    def close(self, obj):
        self.dia.dismiss()
    def shut(self,obj):
        self.cri.dismiss()


    def fin(self, obj):
        movie = self.m.text.replace(' ', '%20')
        f = Request(f'YOUR SOURCE HERE', headers={'User-Agent': 'Mozilla/5.0'})
        f = urlopen(f).read().decode()
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
        if titls==[]:
            firstt = MDRectangleFlatButton(text="Back", on_release=self.shut)
            self.cri=MDDialog(title="Sorry...",text="Your search returned no results.\nPlease recheck spacings and spellings and try again",line_width=1.2,buttons=[firstt,])
            self.cri.open()
        else:
            for j in titls:
                emp.append(ItemConfirm(text=j))
            first = MDRectangleFlatButton(text="Back", line_width=1.23,on_release=self.close)

            self.dia = MDDialog(title=f'Results for "{self.m.text}"',
                                type="confirmation",
                                items=emp,
                                buttons=[
                                    first,
                                ],
                                )
            self.dia.open()


BoredFlix().run()
