from kivymd.uix.screen import MDScreen

from kivy.properties import ObjectProperty
class RootScreen(MDScreen):
    name=ObjectProperty(None) 

    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    
    def change_screen(self,*args):
            self.ids.main_scr.current = 'root_screen_pro'
    
    
   
    def current_slide(self,index):
        for i in range(3):
            if index == i:
                self.ids[f"slide{index}"].color ="#FD8C5F"
            else:
                self.ids[f"slide{i}"].color = "#6F6F6F"
    def next(self):
        self.ids.carousel.load_next(mode="next")
        
    
    def change_open(self):

        self.ids.main_scr.current = 'test_scr'
              
    def close(self):
    
        self.ids.main_scr.current = 'close'