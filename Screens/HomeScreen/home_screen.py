from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class HomeScreen(MDScreen):
    name=ObjectProperty(None)
    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    def current_slide(self,index):
        global k
        k = index
        for i in range(3):
            if index == i:
                self.ids[f"slide{index}"].color ="#FD8C5F"
            else:
                self.ids[f"slide{i}"].color = "#6F6F6F"
        Clock.schedule_once(self.next,2)
                
    def next(self,*args):
        global k 
        print(k)
        if k == 0 or k == 1 :
            self.ids.carousel.load_next(mode="next")
        elif k == 2:
            k == 0