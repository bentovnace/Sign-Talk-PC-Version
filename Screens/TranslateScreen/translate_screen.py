from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivymd.uix.filemanager import MDFileManager
import numpy as np 
from kivymd.uix.screen import MDScreen
import base64
import json                    
import requests
from plyer import filechooser,tts
from kivy.properties import ListProperty
from kivy.uix.image import Image
from Speechrecognizer import stt
import urllib
from urllib.request import urlopen
 
ScreenManager = ObjectProperty(None)

class TranslateScreen(MDScreen):
    name=ObjectProperty(None)
    
    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    
    manager = ObjectProperty(None)
    global local, datasign
    selection = ListProperty([])
    file_obj = open('label.txt')
    data = file_obj.read()
    file_obj.close()
    local = data
    datasign=0
   
    
        
    def speech_recognition(self):
        if stt.listening:
            self.stop_listening()
            return
        self.ids.speech.icon = 'record-circle'
        self.textinput.text =''
        stt.start()

        Clock.schedule_interval(self.check_state, 1 /5)
    def stop_listening(self):
        self.ids.speech.icon = 'account-tie-voice'
        stt.stop()
        self.update()
        Clock.unschedule(self.check_state)
    def check_state(self, dt):
        # if the recognizer service stops, change UI
        if not stt.listening:
            self.stop_listening()
    def update(self):
        self.textinput.text = '\n'.join(stt.results)
   
       
    def choose(self):
        
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
       
        self.selection = selection
        if str(selection) == '[]':
            self.path_name = ''
        else: 
            self.path_name = selection[0]
        print(self.path_name)
    def check_internet(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current = 'scr_1'
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'
    def reload_check(self,*args):
        Clock.schedule_once(self.check_internet)
    def check_internet_2(self,*args):
        global local
        
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            
            text_input =self.textinput.text
        
            self.secondspinner = self.ids.secondvalue.text 
            self.firstspinner  = self.ids.firstvalue.text

            #a = t.translate(text_input,src = self.firstspinner ,  dest = self.secondspinner)        
            #b= a.text
            
            api  = local + '/etrans'+'?textinput='+text_input+'&src='+self.firstspinner+'&dest='+self.secondspinner
        
            response = requests.get(api).text 
            b = response
            self.ids.textoutput.font_name = 'Cucho.otf'
            self.ids.textoutput.font_size = '24sp'
            self.textoutput.text = b
            print('b')
        
            
        except urllib.error.URLError as Error:
            print(Error)
            print(local)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'
        
    def input_data(self):
        global textinput, firstspinner, secondspinner, b,local
        print(self.textinput.text)
        Clock.schedule_once(self.remove_sign)
        Clock.schedule_once(self.check_internet_2)
        
    def translate(self):
        trans = self.firstspinner       
        print(trans)  
        
    def text_to_speech(self):
       
        speak = self.ids.textoutput.text
        try:
            tts.speak(speak)
        except:
            print ('cant talk')

#    def text_to_speech(self):
#        text_input =self.textinput.text
#        t = Translator()
#        a = t.translate(text_input,src = self.firstspinner ,  dest = self.secondspinner)        
#        b= a.text 
#        self.firstspinner  = self.ids.firstvalue.text
#        engine = gTTS(b, lang = 'en')
#        engine.save('speechtotext.mp3')
#        playsound('speechtotext.mp3')
    
#    def speech_recognition(MDApp, Widget):
#        Button = MDRectangleFlatButton(text = 'ADD Audio', pos_hint= {'center_x':.5,'center_y':.5})
#        TranslateScreen.add_widget(Button)


    #def speech_recognition(self):
    #    stt.start()
    #    assert stt.listening
    #    print(stt.partial_results)
    #    stt.stop()   
    #    print(stt.results)
    


            
    def file_open(self):
        self.file_manager_obj = MDFileManager(
            select_path = self.select_path,
            exit_manager = self.exit_manager,        
        )
        self.file_manager_obj.show("/")
       
    def select_path(self, path):

        global path_name
        #print(path.replace('/','',1))
        self.path_name = path.replace('/',"",1)
        print(self.path_name) #''
        self.exit_manager()

    
    
    

    def text_recognition(self):
       
        self.path = self.path_name
        Clock.schedule_once(self.img_recognition_text)
    def check_internet_3(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
           
            self.path_pro_audio =  self.path_name 
            
            import requests
            myurl = local + '/uploader'
            files = {'file': open(self.path_name, 'rb')}
            getdata = requests.post(myurl, files=files)
            print(getdata.text)  
            val = getdata.text
            self.textinput.text = val
                
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'    

    def audio_recogniton_file(self):
        Clock.schedule_once(self.check_internet_3)

    def open_file_manager(self):      
        self.file_manager_obj.show("/")
    
    def exit_manager(self):       
        self.file_manager_obj.close()

    
    
    def open_new_screen(self):
        print('Button Press')



    def camera_recognition(self):
      
       
        self.ids.main.current='scr_2'
    def remove_sign(self,*args):
        global datasign
        if datasign==1:
            self.ids.output_box.remove_widget(self.ids.sign)
            datasign =0
    
    def check_internet_4(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            api = local + "/etext"
            image_file = self.path

            with open(image_file, "rb") as f:
                im_bytes = f.read()        
            im_b64 = base64.b64encode(im_bytes).decode("utf8")

            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            
            payload = json.dumps({"image": im_b64, "other_key": "value"})
            response = requests.post(api, data=payload, headers=headers)
            self.textinput.text = response.text
                
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'    

    def img_recognition_text(self,*args):
        Clock.schedule_once(self.check_internet_4)
        
    def check_internet_5(self,*args):
        global local,datasign
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
           
            text_input =self.textinput.text
            if datasign == 0:
                signimage = Image(source="",size_hint=(1,2))
                self.ids.output_box.add_widget(signimage)
                self.ids["sign"]=signimage
                datasign = 1  
                
            api2 = local +'/signdata?input='+text_input
            bodyresponse = requests.get(api2).text
            result = bodyresponse
            print(result)
            if result != "None":
                Clock.schedule_once(self.returnimage)
                
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'    
            
    def add_sign(self,*args):
        Clock.schedule_once(self.check_internet_5)
        
        
    def check_internet_6(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
           
       
            text_input =self.textinput.text
            self.secondspinner = self.ids.secondvalue.text 
            self.firstspinner  = self.ids.firstvalue.text
            self.secondspinner = self.ids.secondvalue.text 
            self.firstspinner  = self.ids.firstvalue.text
            
            api2 = local +'/signdata?input='+text_input
            bodyresponse = requests.get(api2).text
            result = bodyresponse
            filename =result
            downloadUrl = local+'/returnsignimg?input='+text_input
            req = requests.get(downloadUrl)
            print(result)
            with open(str(filename), 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            self.ids.sign.source= filename
                
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'          
    def returnimage(self,*args):
        Clock.schedule_once(self.check_internet_6)
    def check_internet_7(self,*args):
        global textinput, firstspinner, secondspinner, b, local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            


            text_input =self.textinput.text
            self.secondspinner = self.ids.secondvalue.text 
            self.firstspinner  = self.ids.firstvalue.text
                        
            
            api  = local + '/etrans'+'?textinput='+text_input+'&src='+self.firstspinner+'&dest='+self.secondspinner
            response = requests.get(api).text 
            b = response
            Clock.schedule_once(self.add_sign)
            
            self.ids.textoutput.font_size = '50sp'
            self.ids.textoutput.font_name ='Bodylanguage-Regular.otf'
            self.textoutput.text = b
                    
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_2'                  
    def bodylanguage_call(self):
        Clock.schedule_once(self.check_internet_7)
    
        
    def back_pro(self):
        self.ids.main.current='scr_1'   

    def screen_call(self,*args):
	    self.ids.main.current='scr_1'
     
        
    

