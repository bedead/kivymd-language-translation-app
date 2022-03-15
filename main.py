import os
from typing import Text
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet, MDListBottomSheet
import json
import webbrowser
from textblob import TextBlob





if os.path.exists('langgo_data.json'):
    with open('langgo_data.json','r') as f:
        data = json.load(f)

else:
    data = {'theme': 'Dark','color':'Brown'}
    with open('langgo_data.json','w') as f:
        json.dump(data, f)

with open('language.json','r') as s:
    language_dict = json.load(s)




if (platform != 'android'):
    # from android.permissions import request_permissions, Permission
    # request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    Window.size = (360, 640)


sm = ScreenManager()
# all screens
class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass
class langtoSelect(MDBoxLayout):
    pass
class profilecard(MDBoxLayout):
    pass



class Homescreen(Screen):
    def translate_text(self, from_text):
        for key, value in language_dict.items():
            if key == Main.to_language:
                text = TextBlob(from_text)
                translated_text = text.translate(to=value)
                break
        self.ids.to_text.text = str(translated_text)


class Settingscreen(Screen):
    color_sheet = None
    profile_sheet = None
    def toggle_bottomcolorsheet(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
        # 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 
        # 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.color_sheet = MDListBottomSheet(radius=12)
        data1 = {
            'Red':"", 'Pink':"", 'Purple':"",
            'DeepPurple':"", 'Indigo':"",
            'Blue':"", 'LightBlue':"",'Cyan':"",
            'Teal':"", 'Green':"", 'LightGreen':"",
            'Lime':"", 'Yellow':"", 'Amber':"",
            'Orange':"", 'DeepOrange':"", 'Brown':"",
            'Gray':"", 'BlueGray':""
        }
        for items in data1.items():
            self.color_sheet.add_item(
                items[0],
                lambda x, y=items[0]: app.change_primary_color(y),
                icon='circle-outline',
            )
        self.color_sheet.open()

    def toggle_profile(self):
        self.profile_sheet = MDCustomBottomSheet(
            screen=Factory.profile_card(),
            radius=12
            )
        self.profile_sheet.open()

sm.add_widget(Homescreen(name="Home"))
sm.add_widget(Settingscreen(name="Settings"))




# main class of app
class Main(MDApp):
    to_dialog = None
    to_language = ""
    def __init__(self, **kwargs):
        self.title = "Langgo"
        super().__init__(**kwargs)

        




    def goto_mail(self):
        webbrowser.open('mailto:satyam.work.only@gmail.com')









    def show_to_option(self):
        
        self.to_dialog = MDDialog(
                radius=[20,7,20,7],
                title="To : ",
                type="custom",
                content_cls=langtoSelect(),
            )
        self.to_dialog.open()
    def close_to(self):
        if self.to_dialog.open:
            self.to_dialog.dismiss(force=True)
        else:
            pass
    def to_select(self, lang):
        Main.to_language = lang






    # dark and light theme changer
    def toggle_theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            data['theme'] = 'Light'
            self.root.ids.nav_icon2.text_color = app.theme_cls.primary_color
            self.root.ids.nav_icon1.text_color = [0,0,0,1]
        else:
            self.theme_cls.theme_style = "Dark"
            data['theme'] = 'Dark'
            self.root.ids.nav_icon2.text_color = app.theme_cls.primary_color
            self.root.ids.nav_icon1.text_color = [1,1,1,1]
        with open('langgo_data.json','w') as f:
            json.dump(data, f)







    def change_primary_color(self, color):
        print(color)
        if color != "":
            self.theme_cls.primary_palette = color
            data['color'] = color
            if self.theme_cls.theme_style == "Dark":
                self.root.ids.nav_icon2.text_color = app.theme_cls.primary_color
                self.root.ids.nav_icon1.text_color = [1,1,1,1]
            else:
                self.root.ids.nav_icon2.text_color = app.theme_cls.primary_color
                self.root.ids.nav_icon1.text_color = [0,0,0,1]
        with open('langgo_data.json','w') as f:
           json.dump(data, f)








    def select_nav(self, instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(2):
                if f"nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = app.theme_cls.primary_color
                else:
                    if app.theme_cls.theme_style == "Light":
                        self.root.ids[f"nav_icon{i+1}"].text_color = [0,0,0,1]
                    else:
                        self.root.ids[f"nav_icon{i+1}"].text_color = [1,1,1,1]







    # donot remove build method
    def build(self):

        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
        # 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 
        # 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        # themes and palette

        self.theme_cls.material_style = "M3"
        
        if data != None:
            self.theme_cls.theme_style = data['theme']
            self.theme_cls.primary_palette = data['color']
        else:
            pass


        Builder.load_file('Homescreen.kv')
        Builder.load_file('Settingscreen.kv')
        Builder.load_file('langto.kv')
        Builder.load_file('profile_card.kv')
        return Builder.load_file('mainapp.kv')

if __name__ == "__main__":
    app = Main()
    app.run()