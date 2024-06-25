from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
class ProfileScreen(MDScreen):
    name=ObjectProperty(None)
    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    
    def send_key(self,*args):
        text = self.cus_pro.ids.input_message_pro.text 
        print(text)
        save_label_txt = open('label.txt', mode= 'w+')
        label_saved = save_label_txt.write(text)
        self.obj_pro.dismiss() 
    def key(self):
       
        self.cus_pro =Factory.CustomBottomSheet_key()
        self.obj_pro = self.cus_pro.ids.send_button_pro.bind(on_press = self.send_key)
        self.obj_pro = MDCustomBottomSheet(screen = self.cus_pro)
        self.obj_pro.open() 
        
    global M
    M = SoundLoader.load('background.wav')
    
    def music(self):
        
        if M.state == 'stop':
            M.play()
            print(M.state)
        else:
            M.stop()
            print(M.state)
            
    
    def notify(self):
        print('ok')
