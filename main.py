# https://pythondevelopers14.blogspot.com/2020/07/sign-up-page-projects.html
# Bottom bar, Home,
from kivymd.app import MDApp
from kivy.lang.builder import Builder

built = '''
ScreenManager:
    id: screen_manager        
    Screen:
        name: 'home'
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            elevation: 15
                            title: 'Lex Specialis'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]    
                        
                        MDBottomNavigation:
                            id: panel
                    
                            MDBottomNavigationItem:
                                name: "homie"
                                text: "Home"
                                icon: "home"
                                    
                                Image:
                                    source: 'logo.png'
                                    elevation_normal: 30
                                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    
                            MDBottomNavigationItem:
                                name: "people"
                                text: "People"
                                icon: "account-group"
                    
                                MDLabel:
                                    font_style: "Body1"
                                    theme_text_color: "Primary"
                                    text: "Peoples Section"
                                    halign: "center"
                    
                            MDBottomNavigationItem:
                                name: "blogs"
                                text: "Blogs"
                                icon: "blogger"
                    
                                MDLabel:
                                    font_style: "Body1"
                                    theme_text_color: "Primary"
                                    text: "Blogs section"
                                    halign: "center"
                            
                            MDBottomNavigationItem:
                                name: "carrier"
                                text: "Carrier"
                                icon: "help-network"
                    
                                MDLabel:
                                    font_style: "Body1"
                                    theme_text_color: "Primary"
                                    text: "How to Apply at Lex Specialis ?"
                                    halign: "center"
                                    
    
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        size_hint: None, None
                        size: "100dp", "100dp"
                        source: 'logo.png'
    
                    MDLabel:
                        text: "Yogesh Ojha"
                        icon_left: 'account'
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: 'ojha.yogesh@gmail.com'
                        font_styles: 'Captions'
                        size_hint_y: None
                        height: self.texture_size[1]
    
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    screen_manager.current = "home"
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    screen_manager.current = "scr2"
                                text: 'Login'
                                IconLeftWidget:
                                    icon: 'login'
                            OneLineIconListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    screen_manager.current = "scr3"
                                text: 'Sign Up'
                                IconLeftWidget:
                                    icon: 'account-box'
                            OneLineIconListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    screen_manager.current = "scr4"
                                text: 'About'
                                IconLeftWidget:
                                    icon: 'information-variant'
                            OneLineIconListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    screen_manager.current = "scr5"
                                text: 'Settings'
                                IconLeftWidget:
                                    icon: 'account-settings'
                                

    Screen:
        name: "home1"
        in_class: text
            
        
    Screen:
        name: "scr2"
        in_class: text
        MDLabel:
            text: "Login"
            font_style: 'H2'
            pos_hint: {'center_x': 0.6, 'center_y': 0.8}
        MDFlatButton:
            text: 'home'
            on_press:
                screen_manager.current = 'home'
        MDTextField:
            id: text
            hint_text: "Enter the Password"
            helper_text: "Forgot the Password?"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint_x: None
            width: 300
            icon_right: "account-search"
            required: True
        MDRectangleFlatButton:
            text: 'Submit'
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}

        MDLabel:
            text: ''
            id: show
            pos_hint: {'center_x': 1.0, 'center_y': 0.2}

    Screen:
        name: "scr3"
        MDLabel:
            text: "Sign Up"
            font_style: 'H2'
            pos_hint: {'center_x': 0.6, 'center_y': 0.8}
        MDTextField:
            id: text
            hint_text: "Enter the USERNAME"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300
            icon_right: "account"
            required: True
        MDTextField:
            id: text
            hint_text: "Enter the EMAIL"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300
            icon_right: "email"
            required: True
        MDTextField:
            id: text
            hint_text: "Enter the Password"
            helper_text: "Forgot the Password?"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint_x: None
            width: 300
            icon_right: "account-search"
            required: True
        MDRectangleFlatButton:
            text: 'Submit'
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}

        MDLabel:
            text: ''
            id: show
            pos_hint: {'center_x': 1.0, 'center_y': 0.2}
            
        MDFlatButton:
            text: 'home'
            on_press:
                screen_manager.current = 'home'

    Screen:
        name: "scr4"
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "280dp", "180dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    
            MDLabel:
                text: "Lex Specialis"
                theme_text_color: "Secondary"
                size_hint: (0.0, 1)
    
            MDSeparator:
                height: "1dp"
    
            MDLabel:
                text: "Law firm is in its very first decade of practice and open to deal with variety of cases through the team of our young & dynamic lawyers."  
        
        MDFlatButton:
            text: 'Home'
            on_press:
                screen_manager.current = "home"
            
    Screen:
        name: "scr5"
        
        ScrollView:
            MDList:
                OneLineAvatarIconListItem:
                    text: 'Account'
                    IconLeftWidget:
                        icon: 'account-details'
                    IconRightWidget:
                        icon: 'arrow-right-drop-circle-outline'
                OneLineAvatarIconListItem:
                    text: 'Privacy'
                    IconLeftWidget:
                        icon: 'shield-account-outline'
                    IconRightWidget:
                        icon: 'arrow-right-drop-circle-outline'
                OneLineAvatarIconListItem:
                    text: 'Email & Notification'
                    IconLeftWidget:
                        icon: 'email-alert-outline'
                    IconRightWidget:
                        icon: 'arrow-right-drop-circle-outline'
                OneLineAvatarIconListItem:
                    text: 'Language'
                    IconLeftWidget:
                        icon: 'alphabetical'
                    IconRightWidget:
                        icon: 'arrow-right-drop-circle-outline'
                OneLineAvatarIconListItem:
                    text: 'Dark Mode'
                    IconLeftWidget:
                        icon: 'theme-light-dark'
                    IconRightWidget:
                        icon: 'arrow-right-drop-circle-outline'
                        
        MDFlatButton:
            text: 'Home'
            on_press:
                screen_manager.current = "home"
                    
'''


class Main(MDApp):
    data = {
        'Raise a Query': 'account-question',
    }

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(built)
        return screen


Main().run()
