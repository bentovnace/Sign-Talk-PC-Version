from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty

from kivy.clock import Clock
import random
from kivy.core.audio import SoundLoader
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
import requests

from Screens.GameScreen.Chao_hoi import quiz1
from Screens.GameScreen.Gioi_thieu import quiz2
from Screens.GameScreen.Gia_dinh import quiz3
from Screens.GameScreen.Xa_hoi import quiz4
from Screens.GameScreen.Mua_sam import quiz5
from Screens.GameScreen.Nha_hang import quiz6
from Screens.GameScreen.Hoc_tap import quiz7
from Screens.GameScreen.The_thao import quiz8
from Screens.GameScreen.Du_lich import quiz9
from Screens.GameScreen.Nghe_nghiep import quiz10
from Screens.GameScreen.Mau_sac import quiz11
from Screens.GameScreen.Phuong_tien import quiz12
from Screens.GameScreen.Abc import quiz13
import urllib
from urllib.request import urlopen
class GameScreen(MDScreen):
    name=ObjectProperty(None)
    textinput  = ObjectProperty(None)

    textoutput = ObjectProperty(None)
    global local
    name=ObjectProperty(None)
    file_obj = open('label.txt')
    data = file_obj.read()
    file_obj.close()
    local = data
    global k , h , w
    k=0  
    h= 0
    w = 1 #Thay doi trang thai nut back
    def check_internet(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            Clock.schedule_once(self.download1)
            Clock.schedule_once(self.download2)
            Clock.schedule_once(self.download3)
            Clock.schedule_once(self.download4)
            Clock.schedule_once(self.download5)
            Clock.schedule_once(self.download6)
            Clock.schedule_once(self.download7)
            Clock.schedule_once(self.download8)
            Clock.schedule_once(self.download9)
            Clock.schedule_once(self.download10)
            Clock.schedule_once(self.download11)
            Clock.schedule_once(self.download12)
            Clock.schedule_once(self.download13)
            
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
           
            
    def reload_check(self,*args):
        Clock.schedule_once(self.check_internet)
    def download1(self,*args):
        global local
        url = local +'/Chao_hoi'
        file_name='Screens\\GameScreen\\Chao_hoi.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download2(self,*args):
        global local
        url = local+'/Gioi_thieu'
        file_name='Screens\\GameScreen\\Gioi_thieu.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download3(self,*args):
        global local
        url = local + '/Gia_dinh'
        file_name='Screens\\GameScreen\\Gia_dinh.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download4(self,*args):
        global local
        url = local + '/Xa_hoi'
        file_name='Screens\\GameScreen\\Xa_hoi.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download5(self,*args):
        global local
        url = local + '/Mua_sam'
        file_name='Screens\\GameScreen\\Mua_sam.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download6(self,*args):
        global local
        url = local + '/Nha_hang'
        file_name='Screens\\GameScreen\\Nha_hang.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download7(self,*args):
        global local
        url = local + '/Hoc_tap'
        file_name='Screens\\GameScreen\\Hoc_tap.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download8(self,*args):
        global local
        url = local + '/The_thao'
        file_name='Screens\\GameScreen\\The_thao.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download9(self,*args):
        global local
        url = local+ '/Du_lich'
        file_name='Screens\\GameScreen\\Du_lich.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download10(self,*args):
        global local
        url = local + '/Nghe_nghiep'
        file_name='Screens\\GameScreen\\Nghe_nghiep.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download11(self,*args):
        global local
        url = local + '/Mau_sac'
        file_name='Screens\\GameScreen\\Mau_sac.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download12(self,*args):
        global local
        url = local  + '/Phuong_tien'
        file_name='Screens\\GameScreen\\Phuong_tien.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def download13(self,*args):
        global local
        url = local + '/Abc'
        file_name='Screens\\GameScreen\\Abc.py'
        with open(file_name, "wb") as file:
            
            response = requests.get(url)
            
            file.write(response.content)

    def change_E_screen(self):
        Clock.schedule_once(self.check_internet)
        self.ids.answer_a.font_name = "iCiel Brush Up.otf" 
        self.ids.answer_b.font_name = "iCiel Brush Up.otf" 
        self.ids.answer_c.font_name = "iCiel Brush Up.otf"
        self.ids.answer_d.font_name = "iCiel Brush Up.otf"  
        self.ids.answer_a.font_size ="20sp" 
        self.ids.answer_b.font_size ="20sp"
        self.ids.answer_c.font_size ="20sp"
        self.ids.answer_d.font_size ="20sp"
        self.ids.ques_1.font_size = "32sp"
        
        
        
        if w == 1:
            self.ids.main_scr.current='game_screen_2'
        elif w ==0:
            self.ids.main_scr.current = 'game_screen_3'
    def change_bdl_screen(self):
        global w
        Clock.schedule_once(self.check_internet)
        self.ids.answer_a.font_name = "Bodylanguage-Regular.ttf" 
        self.ids.answer_b.font_name = "Bodylanguage-Regular.ttf" 
        self.ids.answer_c.font_name = "Bodylanguage-Regular.ttf"
        self.ids.answer_d.font_name = "Bodylanguage-Regular.ttf"  
        self.ids.answer_a.font_size ="40sp" 
        self.ids.answer_b.font_size ="40sp"
        self.ids.answer_c.font_size ="40sp"
        self.ids.answer_d.font_size ="40sp"
        self.ids.main_scr.current = 'game_screen_3'
       
    
    def game_back_1(self):
        global w
        self.ids.main_scr.current = 'game_screen_1'
        w =1
        
    
    def change_question(self):
        global h,k
        self.ids.main_scr.current = 'question_1'
        h = 0
        self.ids.progress_bar.value = 0
        k = 0
        self.ids.per_cent.text= "0%"
        
    def answer_A(self):
        
        self.answer = 'A'
        print(self.answer)
        Clock.schedule_once(self.check_ans,0.2)
        
        
    def answer_B(self):
        
       
        self.answer = 'B'
        print(self.answer)
        
        Clock.schedule_once(self.check_ans,0.2)
        
        
    def answer_C(self):
       
        self.answer = 'C'
        print(self.answer)
        Clock.schedule_once(self.check_ans,0.2)
        
    def answer_D(self):
        
        self.answer = 'D'
        print(self.answer)
        Clock.schedule_once(self.check_ans,0.2)
    
    
    def open_bottom_Sheet(self,*args):
        
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
        
    def close_bottom(self,*args):
        self.obj_bottom.dismiss()        
        
        
        
        
    def open_bottom_Sheet_2(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_2, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
        
   
         
    def open_bottom_Sheet_3(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_3, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
    def open_bottom_Sheet_4(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_4, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
    def open_bottom_Sheet_5(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_5, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
      
    def open_bottom_Sheet_6(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_6, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
           
    def open_bottom_Sheet_7(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_7, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
    
    def open_bottom_Sheet_8(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_8, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
    def open_bottom_Sheet_9(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_9, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
    
    def open_bottom_Sheet_10(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_10, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
    def open_bottom_Sheet_11(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_11, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
    def open_bottom_Sheet_12(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_12, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        
            
    def open_bottom_Sheet_13(self,*args):
            
        self.cus_bottom =Factory.CustomBottomSheet_pro()
        self.cus_bottom.ids.continue_button.bind(on_press = self.chao_hoi_13, on_release = self.close_bottom)
        self.obj_bottom = MDCustomBottomSheet(screen = self.cus_bottom)
        
        self.obj_bottom.open()  
        

    def chao_hoi(self,*args):
    
        global ques_number,h,w
        h +=1
    
        w=1
        ques_number = random.randint(1,10)
        if h <= 10:
            Clock.schedule_once(self.ques_up,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz1[question]["question"]
        self.ids.answer_a.text = quiz1[question]["answerW1"]
        self.ids.answer_b.text = quiz1[question]["answerW2"]
        self.ids.answer_c.text = quiz1[question]["answerW3"]
        self.ids.answer_d.text = quiz1[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]

    def chao_hoi_2(self,*args):
        
        global ques_number,h,w
        h +=1
        w = 1
        
        ques_number = random.randint(21,30)
        if h <= 10:
            Clock.schedule_once(self.ques_up_2,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_2(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz2[question]["question"]
        self.ids.answer_a.text = quiz2[question]["answerW1"]
        self.ids.answer_b.text = quiz2[question]["answerW2"]
        self.ids.answer_c.text = quiz2[question]["answerW3"]
        self.ids.answer_d.text = quiz2[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
        
        
    def chao_hoi_3(self,*args):
        
        global ques_number,h,w
        h +=1
        w  = 1
        
        ques_number = random.randint(31,40)
        if h <= 10:
            Clock.schedule_once(self.ques_up_3,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_3(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz3[question]["question"]
        self.ids.answer_a.text = quiz3[question]["answerW1"]
        self.ids.answer_b.text = quiz3[question]["answerW2"]
        self.ids.answer_c.text = quiz3[question]["answerW3"]
        self.ids.answer_d.text = quiz3[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
    
    def chao_hoi_4(self,*args):
        
        global ques_number,h,w
        
        w=1
        h +=1
    
        
        ques_number = random.randint(41,50)
        if h <= 10:
            Clock.schedule_once(self.ques_up_4,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_4(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz4[question]["question"]
        self.ids.answer_a.text = quiz4[question]["answerW1"]
        self.ids.answer_b.text = quiz4[question]["answerW2"]
        self.ids.answer_c.text = quiz4[question]["answerW3"]
        self.ids.answer_d.text = quiz4[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
    def chao_hoi_5(self,*args):
        
        global ques_number,h,w
        w=1
        h +=1
    
        
        ques_number = random.randint(51,60)
        if h <= 10:
            Clock.schedule_once(self.ques_up_5,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_5(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz5[question]["question"]
        self.ids.answer_a.text = quiz5[question]["answerW1"]
        self.ids.answer_b.text = quiz5[question]["answerW2"]
        self.ids.answer_c.text = quiz5[question]["answerW3"]
        self.ids.answer_d.text = quiz5[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
    def chao_hoi_6(self,*args):
        
        global ques_number,h,w
        w =1
        h +=1
    
        
        ques_number = random.randint(61,70)
        if h <= 10:
            Clock.schedule_once(self.ques_up_6,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_6(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz6[question]["question"]
        self.ids.answer_a.text = quiz6[question]["answerW1"]
        self.ids.answer_b.text = quiz6[question]["answerW2"]
        self.ids.answer_c.text = quiz6[question]["answerW3"]
        self.ids.answer_d.text = quiz6[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
            
    def chao_hoi_7(self,*args):
        
        global ques_number,h,w
        w= 1
        h +=1
    
        
        ques_number = random.randint(71,80)
        if h <= 10:
            Clock.schedule_once(self.ques_up_7,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

        
    def ques_up_7(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz7[question]["question"]
        self.ids.answer_a.text = quiz7[question]["answerW1"]
        self.ids.answer_b.text = quiz7[question]["answerW2"]
        self.ids.answer_c.text = quiz7[question]["answerW3"]
        self.ids.answer_d.text = quiz7[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
            
    def chao_hoi_8(self,*args):
            
        global ques_number,h, w
        
        w=1
        h +=1
    
        
        ques_number = random.randint(81,90)
        if h <= 10:
            Clock.schedule_once(self.ques_up_8,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_8(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz8[question]["question"]
        self.ids.answer_a.text = quiz8[question]["answerW1"]
        self.ids.answer_b.text = quiz8[question]["answerW2"]
        self.ids.answer_c.text = quiz8[question]["answerW3"]
        self.ids.answer_d.text = quiz8[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
            
                           
    def chao_hoi_9(self,*args):
            
        global ques_number,h,w
        
        w=1
        h +=1
    
        
        ques_number = random.randint(91,100)
        if h <= 10:
            Clock.schedule_once(self.ques_up_9,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()
    def ques_up_9(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz9[question]["question"]
        self.ids.answer_a.text = quiz9[question]["answerW1"]
        self.ids.answer_b.text = quiz9[question]["answerW2"]
        self.ids.answer_c.text = quiz9[question]["answerW3"]
        self.ids.answer_d.text = quiz9[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
            
    def chao_hoi_10(self,*args):
        
        global ques_number,h, w
        
        w=1
        h +=1
    
        
        ques_number = random.randint(101,110)
        if h <= 10:
            Clock.schedule_once(self.ques_up_10,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

    def ques_up_10(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz10[question]["question"]
        self.ids.answer_a.text = quiz10[question]["answerW1"]
        self.ids.answer_b.text = quiz10[question]["answerW2"]
        self.ids.answer_c.text = quiz10[question]["answerW3"]
        self.ids.answer_d.text = quiz10[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
           
            
    def chao_hoi_11(self,*args):
            
        global ques_number,h, w
        
        w=1
        h +=1
    
        
        ques_number = random.randint(111,120)
        if h <= 10:
            Clock.schedule_once(self.ques_up_11,0.2)
            
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

        
    def ques_up_11(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz11[question]["question"]
        self.ids.answer_a.text = quiz11[question]["answerW1"]
        self.ids.answer_b.text = quiz11[question]["answerW2"]
        self.ids.answer_c.text = quiz11[question]["answerW3"]
        self.ids.answer_d.text = quiz11[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
       
        
    def chao_hoi_12(self,*args):
            
        global ques_number,h, w
        
        w =1 
        h +=1
    
        
        ques_number = random.randint(121,130)
        if h <= 10:
            Clock.schedule_once(self.ques_up_12,0.2)
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

        
    def ques_up_12(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz12[question]["question"]
        self.ids.answer_a.text = quiz12[question]["answerW1"]
        self.ids.answer_b.text = quiz12[question]["answerW2"]
        self.ids.answer_c.text = quiz12[question]["answerW3"]
        self.ids.answer_d.text = quiz12[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
        
        
    def chao_hoi_13(self,*args):
            
        global ques_number,h, w
        
        w =0 
        h +=1
    
        
        ques_number = random.randint(131,156)
        if h <= 10:
            Clock.schedule_once(self.ques_up_13,0.2)
            self.ids.answer_a.font_size ="64sp" 
            self.ids.answer_b.font_size ="64sp"
            self.ids.answer_c.font_size ="64sp"
            self.ids.answer_d.font_size ="64sp"
        else:
            self.ids.main_scr.current = 'final_score'
        
        
        #check_ans()

        
    def ques_up_13(self,*args):
        global question 
        
        question = ques_number
        print(question)
        
        self.ids.ques_1.text = quiz13[question]["question"]
        self.ids.answer_a.text = quiz13[question]["answerW1"]
        self.ids.answer_b.text = quiz13[question]["answerW2"]
        self.ids.answer_c.text = quiz13[question]["answerW3"]
        self.ids.answer_d.text = quiz13[question]["answerW4"]
        self.ids.card_a.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_b.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_c.md_bg_color =  [255/255, 255/255, 255/255,1]
        self.ids.card_d.md_bg_color =  [255/255, 255/255, 255/255,1]
        
    def chao_hoi_14(self,*args):
            
        global ques_number,h, w
        
        w =0 
        h +=1
    
        
        ques_number = random.randint(131,156)
        if h <= 10:
            
            self.ids.answer_a.font_name = "iCiel Brush Up.otf" 
            self.ids.answer_b.font_name = "iCiel Brush Up.otf" 
            self.ids.answer_c.font_name = "iCiel Brush Up.otf"
            self.ids.answer_d.font_name = "iCiel Brush Up.otf"  
            self.ids.ques_1.font_name = "Bodylanguage-Regular.otf"
            self.ids.answer_a.font_size ="64sp" 
            self.ids.answer_b.font_size ="64sp"
            self.ids.answer_c.font_size ="64sp"
            self.ids.answer_d.font_size ="64sp"
            self.ids.ques_1.font_size = "64sp"
            Clock.schedule_once(self.ques_up_13,0.2)
            
        else:
            self.ids.main_scr.current = 'final_score'
        
        
    def check_ans(self, *args):
        global k
        question = ques_number
        
        answer_pro  = self.answer
        if question <=10 and question >=1:
            if quiz1[question]['answercorrect1'].lower() == answer_pro.lower():
        
                self.ids.progress_bar.value += 10
                k=k+10
            
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                Clock.schedule_once(self.open_bottom_Sheet,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
                    
        if question <=30 and question >=21:        
            if quiz2[question]['answercorrect2'].lower() == answer_pro.lower():
            
                self.ids.progress_bar.value += 10
                k=k+10
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_2,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
                    
        if question <= 40 and question >= 31:        
            if quiz3[question]['answercorrect3'].lower() == answer_pro.lower():
            
                
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_3,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question <= 50 and question >=41:       
            if quiz4[question]['answercorrect4'].lower() == answer_pro.lower():
            
                
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_4,1)
            else:
                
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question <=60 and question >=51:       
            if quiz5[question]['answercorrect5'].lower() == answer_pro.lower():
            
                
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_5,1)
            else:
                
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question >=61 and question <=70:           
            if quiz6[question]['answercorrect6'].lower() == answer_pro.lower():
            
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_6,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question >=71 and question <=80:             
            if quiz7[question]['answercorrect7'].lower() == answer_pro.lower():

                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_7,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question >=81 and question <=90:         
            if quiz8[question]['answercorrect8'].lower() == answer_pro.lower():
            
                
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_8,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question >=91 and question <=100:         
            if quiz9[question]['answercorrect9'].lower() == answer_pro.lower():
            
                
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_9,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question >=101 and question <=110:         
            if quiz10[question]['answercorrect10'].lower() == answer_pro.lower():
        
                
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"
                
                SoundLoader.load("Correct.wav").play()
                
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                
                Clock.schedule_once(self.open_bottom_Sheet_10,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        if question >=111 and question <=120: 
            if quiz11[question]['answercorrect11'].lower() == answer_pro.lower():
            
                
                self.ids.progress_bar.value += 10
                k=k+10
                
                print(k)
                self.ids.per_cent.text = str(k)+"%"          
                SoundLoader.load("Correct.wav").play()          
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                Clock.schedule_once(self.open_bottom_Sheet_11,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":                
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]       
                    
        if question >=121 and question <=130:      
            if quiz12[question]['answercorrect12'].lower() == answer_pro.lower():
                        
                self.ids.progress_bar.value += 10
                k=k+10            
                print(k)
                self.ids.per_cent.text = str(k)+"%"            
                SoundLoader.load("Correct.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                Clock.schedule_once(self.open_bottom_Sheet_12,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
                    
                    
        if question >=131 and question <=156:      
            if quiz13[question]['answercorrect1'].lower() == answer_pro.lower():
                        
                self.ids.progress_bar.value += 10
                k=k+10            
                print(k)
                self.ids.per_cent.text = str(k)+"%"            
                SoundLoader.load("Correct.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro =="B":
                    self.ids.card_b.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [71/255, 227/255, 44/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [71/255, 227/255, 44/255,1]
                Clock.schedule_once(self.open_bottom_Sheet_13,1)
            else:
            
                SoundLoader.load("Buzzer.wav").play()
                if answer_pro == "A":
                    self.ids.card_a.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro =="B":
                    self.ids.card_b.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "C":
                    self.ids.card_c.md_bg_color =  [225/255, 59/255, 45/255,1]
                elif answer_pro == "D":
                    self.ids.card_d.md_bg_color =  [225/255, 59/255, 45/255,1]
        
        
    
    
    
    
    
    
    
    
    
    