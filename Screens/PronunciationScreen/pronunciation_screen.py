from kivymd.uix.screen import MDScreen

from kivy.clock import Clock
from kivy.properties import ObjectProperty
import random
from kivy.core.audio import SoundLoader
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from plyer import tts
from Speechrecognizer import stt
import requests
import urllib
from urllib.request import urlopen


from Screens.PronunciationScreen.Animal  import quizz1
from Screens.PronunciationScreen.Food import quizz2
from Screens.PronunciationScreen.Color import quizz3
from Screens.PronunciationScreen.Weather import quizz4
from Screens.PronunciationScreen.Sport import quizz5
class PronunciationScreen(MDScreen):
    name=ObjectProperty(None)
    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    global local
    name=ObjectProperty(None)
    file_obj = open('label.txt')
    data = file_obj.read()
    file_obj.close()
    local = data
    
    def check_internet(self,*args):
        global local, q, k 
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            Clock.schedule_once(self.download1)
            Clock.schedule_once(self.download2)
            Clock.schedule_once(self.download3)
            Clock.schedule_once(self.download4)
            Clock.schedule_once(self.download5)
           
           
            
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
    def download1(self,*args):
        global local
        url = local + '/Animal'
        file_name='Screens\\PronunciationScreen\\Animal.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download2(self,*args):
        global local
        url = local + '/Color'
        file_name='Screens\\PronunciationScreen\\Color.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download3(self,*args):
        global local
        url = local + '/Food'
        file_name='Screens\\PronunciationScreen\\Food.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download4(self,*args):
        global local
        url = local + '/Sport'
        file_name='Screens\\PronunciationScreen\\Sport.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download5(self,*args):
        global local
        url = local + '/Weather'
        file_name='Screens\\PronunciationScreen\\Weather.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)
    def change_speak_ques(self):
        global local, q, k 
        Clock.schedule_once(self.check_internet)
        self.ids.speak_scr.current = "speak_ques"
        q = 0
        k = 0
        self.ids.per_cent_speak.text = str(k)+"%"
        self.ids.progress_bar_speak.value = 0
        self.ids.result.text = ""
    def change_menu_speak_screen(self):
        self.ids.speak_scr.current = "home_speak"
    
 
        
        
    def Animal(self,*args):
        
        global ques_number_pro,q
        q +=1
    
        
        ques_number_pro = random.randint(1,10)
        if q <= 10:
            Clock.schedule_once(self.up_data,0.2)
        else:
            self.ids.main_scr.current = 'profinal'
        
           
        
    def up_data(self,*args):
        ran_question = ques_number_pro
        self.ids.ques_image.source = quizz1[ran_question]["image"]
        self.ids.ques_speak.text = quizz1[ran_question]["question"]
        self.ids.meaning.text = quizz1[ran_question]["meaning"]
        self.ids.pronun.text=quizz1[ran_question]["pronun"]
        
    def Food(self,*args):
        
        global ques_number_pro,q
        q +=1
    
        
        ques_number_pro = random.randint(21,30)
        if q <= 10:
            Clock.schedule_once(self.up_data_2,0.2)
        else:
            self.ids.main_scr.current = 'profinal'
        
           
        
    def up_data_2(self,*args):
        ran_question = ques_number_pro
        self.ids.ques_image.source = quizz2[ran_question]["image"]
        self.ids.ques_speak.text = quizz2[ran_question]["question"]
        self.ids.meaning.text = quizz2[ran_question]["meaning"] 
        self.ids.pronun.text=quizz2[ran_question]["pronun"]   

        
        
    def Color(self,*args):
        
        global ques_number_pro,q
        q +=1
    
        
        ques_number_pro = random.randint(41,50)
        if q <= 10:
            Clock.schedule_once(self.up_data_3,0.2)
        else:
            self.ids.main_scr.current = 'profinal'
        
           
        
    def up_data_3(self,*args):
        ran_question = ques_number_pro
        self.ids.ques_image.source = quizz3[ran_question]["image"]
        self.ids.ques_speak.text = quizz3[ran_question]["question"]
        self.ids.meaning.text = quizz3[ran_question]["meaning"]
        self.ids.pronun.text=quizz3[ran_question]["pronun"]

        
    def Weather(self,*args):
        
        global ques_number_pro,q
        q +=1
    
        
        ques_number_pro = random.randint(61,70)
        if q <= 10:
            Clock.schedule_once(self.up_data_4,0.2)
        else:
            self.ids.main_scr.current = 'profinal'
        
           
        
    def up_data_4(self,*args):
        ran_question = ques_number_pro
        self.ids.ques_image.source = quizz4[ran_question]["image"]
        self.ids.ques_speak.text = quizz4[ran_question]["question"]
        self.ids.meaning.text = quizz4[ran_question]["meaning"]
        self.ids.pronun.text=quizz4[ran_question]["pronun"]

        
    def Sport(self,*args):
        
        global ques_number_pro,q
        q +=1
    
        
        ques_number_pro = random.randint(81,90)
        if q <= 10:
            Clock.schedule_once(self.up_data_5,0.2)
        else:
            self.ids.main_scr.current = 'profinal'
    global k    
    k=0        
        
    def up_data_5(self,*args):
        ran_question = ques_number_pro
        self.ids.ques_image.source = quizz5[ran_question]["image"]
        self.ids.ques_speak.text = quizz5[ran_question]["question"]
        self.ids.meaning.text = quizz5[ran_question]["meaning"]
        self.ids.pronun.text=quizz5[ran_question]["pronun"]
    def record_audio(self):
        
        if stt.listening:
            self.stop_listening()
            return
        
        self.ids.record_mic_pro.source = 'record.png'
        stt.start()
        Clock.schedule_interval(self.check_state, 1 /5)
    def stop_listening(self):
        self.ids.record_mic_pro.source = 'icons8-mic-65.png'
        stt.stop()
        self.update()
        Clock.unschedule(self.check_state)
    def check_state(self, dt):
        # if the recognizer service stops, change UI
        if not stt.listening:
            self.stop_listening()
    def update(self):
        global answer_pro_speak, ques_number_pro, ques_pro
        answer = '\n'.join(stt.results)
        ques_pro = ques_number_pro
        if answer =='':
            answer_pro_speak = '\n'.join(stt.partial_results)
        else:
            answer_pro_speak ='\n'.join(stt.results)
        self.ids.result.text = answer_pro_speak
        Clock.schedule_once(self.check_answer_pro,0.2)
    
                
    def check_answer_pro(self,*args):
        global ques_pro,k
        if ques_pro >=1 and ques_pro <=20:       
            if quizz1[ques_pro]['answer'].lower() == answer_pro_speak:
                self.ids.progress_bar_speak.value += 10
                k=k+10
            
                print(k)
                self.ids.per_cent_speak.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
            else:
                SoundLoader.load("Buzzer.wav").play()  
            Clock.schedule_once(self.open_bottom_Sheet_pro_1,1)
    
    
        if ques_pro >=21 and ques_pro <=40:       
            if quizz2[ques_pro]['answer'].lower() == answer_pro_speak:
                self.ids.progress_bar_speak.value += 10
                k=k+10
            
                print(k)
                self.ids.per_cent_speak.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
            else:
                SoundLoader.load("Buzzer.wav").play()
            Clock.schedule_once(self.open_bottom_Sheet_pro_2,1)       
        if ques_pro >=41 and ques_pro <=60:       
            if quizz3[ques_pro]['answer'].lower() == answer_pro_speak:
                self.ids.progress_bar_speak.value += 10
                k=k+10
            
                print(k)
                self.ids.per_cent_speak.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
            else:
                SoundLoader.load("Buzzer.wav").play()    
    
            Clock.schedule_once(self.open_bottom_Sheet_pro_3,1)
        if ques_pro >=61 and ques_pro <=80:       
            if quizz4[ques_pro]['answer'].lower() == answer_pro_speak:
                self.ids.progress_bar_speak.value += 10
                k=k+10
            
                print(k)
                self.ids.per_cent_speak.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
            else:
                SoundLoader.load("Buzzer.wav").play()  
            Clock.schedule_once(self.open_bottom_Sheet_pro_4,1)
        if ques_pro >=81 and ques_pro <=100:       
            if quizz5[ques_pro]['answer'].lower() == answer_pro_speak:
                self.ids.progress_bar_speak.value += 10
                k=k+10
            
                print(k)
                self.ids.per_cent_speak.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
            else:
                SoundLoader.load("Buzzer.wav").play()  

            Clock.schedule_once(self.open_bottom_Sheet_pro_5,1)
            
    
    
    def play_audio_pro(self):

        speak = self.ids.ques_speak.text
        try:
            tts.speak(speak)
        except:
            print ('cant talk')
        
    def open_bottom_Sheet_pro_1(self,*args):
            
        self.cus_bottom_pro =Factory.CustomBottomSheet_pro_02()
        self.cus_bottom_pro.ids.continue_button.bind(on_press = self.Animal, on_release = self.close_bottom_pro)
        self.obj_bottom_pro = MDCustomBottomSheet(screen = self.cus_bottom_pro)
        self.obj_bottom_pro.open()  
    
    def open_bottom_Sheet_pro_2(self,*args):
            
        self.cus_bottom_pro =Factory.CustomBottomSheet_pro_02()
        self.cus_bottom_pro.ids.continue_button.bind(on_press = self.Food, on_release = self.close_bottom_pro)
        self.obj_bottom_pro = MDCustomBottomSheet(screen = self.cus_bottom_pro)
        self.obj_bottom_pro.open()  
        
    def open_bottom_Sheet_pro_3(self,*args):
            
        self.cus_bottom_pro =Factory.CustomBottomSheet_pro_02()
        self.cus_bottom_pro.ids.continue_button.bind(on_press = self.Color, on_release = self.close_bottom_pro)
        self.obj_bottom_pro = MDCustomBottomSheet(screen = self.cus_bottom_pro)
        self.obj_bottom_pro.open()  
        
        
    def open_bottom_Sheet_pro_4(self,*args):
            
        self.cus_bottom_pro =Factory.CustomBottomSheet_pro_02()
        self.cus_bottom_pro.ids.continue_button.bind(on_press = self.Weather, on_release = self.close_bottom_pro)
        self.obj_bottom_pro = MDCustomBottomSheet(screen = self.cus_bottom_pro)
        self.obj_bottom_pro.open() 
        
    def open_bottom_Sheet_pro_5(self,*args):
            
        self.cus_bottom_pro =Factory.CustomBottomSheet_pro_02()
        self.cus_bottom_pro.ids.continue_button.bind(on_press = self.Sport, on_release = self.close_bottom_pro)
        self.obj_bottom_pro = MDCustomBottomSheet(screen = self.cus_bottom_pro)
        self.obj_bottom_pro.open()  
         
        
        
        
    def close_bottom_pro(self,*args):
        self.obj_bottom_pro.dismiss()        

    