import os 
import importlib
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivymd.uix.screen import MDScreen
from kivy import platform
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

if platform=='android':
    from android.permissions import Permission,request_permissions
    request_permissions([Permission.INTERNET,Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE,Permission.RECORD_AUDIO])
class RootScreen(MDScreen):
    pass 


    







Window.size = (480,853)

class EngLishApp(App,  MDApp):
    
    KV_FILES = {
        os.path.join(os.getcwd(),
            "Screens",
            "RootScreen",
            "root_screen.kv",


        ),

        os.path.join(os.getcwd(),
            "Screens",
            "HomeScreen",
            "home_screen.kv",


        ),


        os.path.join(os.getcwd(),
            "Screens",
            "TranslateScreen",
            "translate_screen.kv",


        ),

        os.path.join(os.getcwd(),
            "Screens",
            "ObjectScreen",
            "object_screen.kv",


        ),

        os.path.join(os.getcwd(),
            "Screens",
            "GameScreen",
            "game_screen.kv",


        ),

        os.path.join(os.getcwd(),
            "Screens",
            "PronunciationScreen",
            "pronunciation_screen.kv",


        ),

        os.path.join(os.getcwd(),
            "Screens",
            "ChatbotScreen",
            "chatbot_screen.kv",


        ),


        os.path.join(os.getcwd(),
            "Screens",
            "ProfileScreen",
            "profile_screen.kv",


        ),



       
    }

    
    CLASSES = {
        "RootScreen":"root_screen",
        "HomeScreen":"Screens.HomeScreen.home_screen",
        "TranslateScreen":"Screens.TranslateScreen.translate_screen",
        "ObjectScreen":"Screens.ObjectScreen.object_screen",
        "GameScreen":"Screens.GameScreen.game_screen",
        "PronunciationScreen":"Screens.PronunciationScreen.pronunciation_screen",
        "ChatbotScreen":"Screens.ChatbotScreen.chatbot_screen",
        "ProfileScreen":"Screens.ProfileScreen.profile_screen",
       



    }
    AUTORELOADER_PATHS = [
        (".",{"recursive":True}),

    ]

    def build_app(self):
        self.theme_cls.primary_palette ="Orange"
        import Screens.RootScreen.root_screen

       
        importlib.reload(Screens.RootScreen.root_screen)
  
        n = RootScreen()
        self.BottomNavigation=n.ids.main
      

            
        return Screens.RootScreen.root_screen.RootScreen()

  

    def on_leave(self):
        print('leave')
        
    def on_pause(self):
        return True
    

    
         
if __name__ == "__main__":
    EngLishApp().run()
