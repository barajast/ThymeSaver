from Food import Food
from User import User

from kivymd.uix.card import MDCardSwipe

from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDThemePicker

from kivymd.uix.dialog import MDDialog

from kivymd.uix.button import MDRectangleFlatButton

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons

from kivymd.uix.list import IconRightWidget
from kivymd.uix.list import IconLeftWidget

from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

from kivy.core.window import Window

# from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField 

Window.size = (400, 650)


KV = '''

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48) #48


<dialog_content>
    orientation:"vertical"
    spaceing: "12dp"
    size_hint_y: None
    height: "120dp"
    
    MDLabel:
        text: "Does this item expire?"
        valign: "top"
    
    BoxLayout:
        BoxLayout:
            MDLabel:
                text: "Yes"
                halign:"center"
            Check:
                active: True
                halign:"left"

        BoxLayout:
            MDLabel:
                text: "No"
                halign:"center"
            Check:
                halign:"left"

    MDRaisedButton:
        text: "Select an expiration date"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()


# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>: #All of the info in the nav drawer
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image: #User image, not necessary but could be cool. Current Captain Wheeze
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "CaptainWheezeopp.png"

    MDLabel: # This will eventually be the username of the user
        text: "A$AP Sidebar"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel: # and this will be the users email
        text: "SadWill@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView: #This is the nav list in the navbar, probably doesn't need a scrollview
        DrawerList:
            id: md_list

<ListItemWithCheckbox>:
    IconLeftWidget:
        icon: root.icon
    RightCheckbox:

<SwipeItem>:

    size_hint_y: 1
    height: content.height
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": 0.5}
            on_release: app.remove_item(root)

        MDIconButton:
            icon: "database-plus"
            pos_hint: {"center_y": 0.5}
            on_release: app.add_pantry_item(root)
            

    MDCardSwipeFrontBox:
        OneLineListItem: # was OneLineListItem
            id: content
            text: root.text
            icon: root.icon
            _no_ripple_effect: True

        RightCheckBox:
MDScreen: #main screen
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"

    ScrollView:
        scroll_timeout: 100

        MDList:
            id:md_list
            padding: 0

    MDFloatingActionButtonSpeedDial:
        data: app.data
        callback: app.callback #testing here
        root_button_anim: True
        hint_animation: True

    
    NavigationLayout: # This is the top bar for naviagation, currently blue

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Yung Money -- The List"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer: # This is the ||| button on the top left that makes the nav bar work
            id: nav_drawer

            ContentNavigationDrawer: # This is the contents that live inside it
                id: content_drawer
'''

user = User("PeterParker","spidyman@gmail.com","password")



class SwipeItem(MDCardSwipe):
    '''' Card with behavior '''
    text = StringProperty()
    icon = StringProperty('android')

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''' list item '''
    icon = StringProperty('android')

class ContentNavigationDrawer(BoxLayout):
    pass

class RightCheckBox(IRightBodyTouch,MDCheckbox):
    '''' right container '''

class ItemDrawer(OneLineIconListItem): # icons and names in the nav list
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1)) #colors gets set back to black after click?


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class dialog_content(BoxLayout):
    pass


class App(MDApp):
    instance = "database"
    
    data = {
        'emoticon-angry': "WILL, I'LL END YOUR BLOODLINE",
        'database-plus': 'Add all checked to Pantry',
        'delete': 'Delete all checked',
        'plus':'Add item to list',
    }

    def got_date(self, the_date):
        print(the_date)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.got_date)
        date_dialog.open()

    def callback(self,instance): #when you press on one of the items in the circle button it prints the name of the icon being used
        print(instance.icon)

    def show_theme_picker(self):
        theme_dialog = MDThemePicker(callback = self.got_date)
        theme_dialog.open()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def add_pantry_item(self,instance):
        hold = instance.text #this gets the title of the item clicked
        close_button = MDRectangleFlatButton(text = 'Close', on_release=self.close_dialog)
        submit_button = MDRectangleFlatButton(text = 'Submit', on_release =self.close_dialog)
        self.dialog = MDDialog(
            title = "Add item to Pantry?",
            size_hint=(0.8,1),
            type="custom",
            content_cls = dialog_content(),
            buttons=[submit_button,close_button]
        )
        self.dialog.open()
        # open thingy that prompts for more info and then creates a food object which is then sent to the food handler

    def close_dialog(self,instance):
        
        #This probably won't be useful here but might be useful for what Katie is doing
        #takes the user list and adds and item "new thing" to it and then adds it to the list on the screen
        user.localList.append("A new item")
        self.screen.ids.md_list.add_widget(
            SwipeItem(text = user.localList[-1], icon = "pasta")
        )
        #end comments
        App.remove_item(self, instance) #this just doesn't work right now, need to remove item after pushing to Pantry
        self.dialog.dismiss()

    def remove_item(self,instance):
        self.screen.ids.md_list.remove_widget(instance)


    def on_start(self):
        
        icons_item = {
            "food-apple": "Food",
            "pasta": "Recipes",
            "database": "Pantry",
            "brush": "Theme", #completely unesccesary but would be cool to customize colors of the app
            #see MDThemePicker https://kivymd.readthedocs.io/en/latest/components/pickers/index.html
            "logout": "Log out",
        }

        itemsList = [
            "", #empty item because the positioning puts it under the nav bar
            "pizza",
            "Banana",
            "Lamb",
            "Chicky nuggies",
            "Gogurt",
            "Cheeze stick",
            "Cold pasta sauce",
            "Spam",
            "Paimon",
            "Shallot",
            "Carrot",
            "Way too many green onions",
            "Chili",
            "Paprika",
            "Flour",
            "Sugar",
            "Apples",
            "Sour patch kids"
        ]
        
        for i in itemsList:
            user.localList.append(i)

        for i in user.localList: #prints all the items in user local list
            self.screen.ids.md_list.add_widget(
                SwipeItem(text = i, icon = "pasta")
            )

        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

App().run() #changed the name here, make a note in your git push