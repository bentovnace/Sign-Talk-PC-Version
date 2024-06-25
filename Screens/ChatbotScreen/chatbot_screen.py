from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.factory import Factory
import requests
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from plyer import tts
import urllib
from urllib.request import urlopen













class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = 'Cucho.otf'
    font_size = 18
    
    
class Response(MDLabel):
    font_name = 'Cucho.otf'
    font_size = 18
    

class ResponseImage(Image):
    source = StringProperty()
    


class ChatbotScreen(MDScreen):
    name=ObjectProperty(None)
    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    global local,state_load, internet_state
    file_obj = open('label.txt')
    data = file_obj.read()
    file_obj.close()
    local = data
    state_load='No'
    internet_state=0
    def check_internet(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.chat_main_scr.current = 'start_chat'
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.chat_main_scr.current = 'disconnect_network'
           
  
            
    
           
    def reload_check(self,*args):
        Clock.schedule_once(self.check_internet)

   
            
        

    
    def speak(self):
        global state_load
        if state_load =='Speak':
            state_load ='No'
            
        else:
            state_load = 'Speak'
        print(state_load)
    def start_scr_chat(self):
        Clock.schedule_once(self.check_internet)
        
        
        
    def text_to_speech(self,*args):
        global pro_response
        speak = pro_response
        try:
            tts.speak(speak)
        except:
            print ('cant talk')   
    
    def response_pro(self, *args):
        response = ""
        response = pro_response
        #if value =="Hello" or value =="hello":
        #    response = f"Hello. My name is Ebot"
        #elif value =="Bye" or value =="How are you":
        #    self.ids.chat_list.add_widget(ResponseImage(source= 'Source\Icon\Back.jpg'))
        if len(response) < 6:
            size_2 = .22
            halign_2 = 'center'
        elif len(response) < 11:
            size_2 = .32
            halign_2 = 'center'
            
        elif len(response) < 16:
            size_2 = .45
            halign_2 = 'center'
            
        elif len(response) < 21:
            size_2 = .58
            halign_2 = 'center'
        elif len(response) < 26:
            size_2 = .71
            halign_2 = 'center'
        else: 
            size_2 = .77
            halign_2 = "right"
        self.ids.chat_list.add_widget(Response(text =response , size_hint_x = size_2, halign= halign_2))    
        
    def start_environment(self,*args):
        global pro_response,sentence, local
        api  = local + '/ebot?input='
        response = requests.get(api+sentence).text
        
        pro_response = str(response)
            
    def start_environment_vn(self,*args):
        global pro_response,sentence, local
        api  = local + '/ebotvn?input2='
        response = requests.get(api+sentence).text
        
        pro_response = str(response)
    def play_text(self):
        self.cus =Factory.CustomBottomSheet_bot()
        self.obj = self.cus.ids.send_button.bind(on_press = self.send)
        self.obj = MDCustomBottomSheet(screen = self.cus)
        self.obj.open()     
    def send(self,*args):
        global size, halign, value ,sentence,state_load
        if self.cus.ids.input_message != "":
            value = self.cus.ids.input_message.text
            sentence =  self.cus.ids.input_message.text
            if len(value) < 6:
                size = .22
                halign = 'center'
            elif len(value) < 11:
                size = .32
                halign = 'center'
                
            elif len(value) < 16:
                size = .45
                halign = 'center'
                
            elif len(value) < 21:
                size = .58
                halign = 'center'
            elif len(value) < 26:
                size = .71
                halign = 'center'
            else: 
                size = .77
                halign = "left"
            self.ids.chat_list.add_widget(Command(text = value, size_hint_x = size, halign =halign))  
            if self.ids.secondvalue.text =='english':
                Clock.schedule_once(self.start_environment,1 )
            elif self.ids.secondvalue.text =='vietnamese':
                Clock.schedule_once(self.start_environment_vn,1 )
            Clock.schedule_once(self.response_pro,1 )
            if state_load=='Speak':
                Clock.schedule_once(self.text_to_speech,1)
            self.cus.ids.input_message.text =""
            self.obj.dismiss()
   
    def chat_back(self):
        self.ids.chat_main_scr.current = 'chatbot_main'