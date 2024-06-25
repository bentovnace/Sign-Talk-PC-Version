from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
import base64
import json
import requests
import cv2 
import numpy as np
import PIL.Image
from Speechrecognizer import stt
from plyer import filechooser
import time
import random
import urllib
from urllib.request import urlopen
from threading import Thread
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty,ListProperty
from random import  random
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.card import MDCard
from pytube import YouTube
from pytube import YouTube
from pytube.cli import on_progress
from kivy.graphics.texture import Texture
global url_get
import sys
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()



import random


class Chip(ToggleButton):
    dc=ListProperty([0,0,0,1])
    def __init__(self,**k):
        super().__init__(**k)

    def call(self,):
        print("a")

        if self.state=='down':
            self.dc=[1,1,1,1]
            self.color=[0,0,0,1]
        else:
            self.color=[1,1,1,1]
            self.dc=[0,0,0,1]


class Plate(MDCard):
    _image=StringProperty('')
    menu=None
    _video_title=StringProperty("#01 Introduction to Kivymd & Toolbar")
    _channel_name=StringProperty("Sk Sahil - 79K views - 1 day ago" )
    _rimage=StringProperty('')
    _time=StringProperty('0:00')
    def on_kv_post(self,obj):pass
    
    
    
    def open_menu(self,obj):
        if not self.menu:
            _items=["Save to Watch Later",'Save to playlist','Share','Report']
            menu_items = [
            {
                "text": f" {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in _items
        ]
            self.menu = MDDropdownMenu(
                caller=obj,
                items=menu_items,
                width_mult=4,
            )
        self.menu.open()
    def menu_callback(self, text_item):
        print(text_item)
        
        
        
        
class ObjectScreen(MDScreen):
    global local
    name=ObjectProperty(None)
    file_obj = open('label.txt')
    data = file_obj.read()
    file_obj.close()
    local = data
    
    
    
    def youtobe_video_1(self):
        global url_get
        self.ids.main.current = "video_youtobe" 
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate1._video_title
        url =self.ids.Plate1.text
        thumb =self.ids.Plate1._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        #self.ids.load_button.on_press = self.gif_get(url)

       
    def youtobe_video_2(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate2._video_title
        url =self.ids.Plate2.text
        thumb =self.ids.Plate2._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
       
        
    def youtobe_video_3(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate3._video_title
        url =self.ids.Plate3.text
        thumb =self.ids.Plate3._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
       
    def youtobe_video_4(self):
        global url_get
        self.ids.main.current = "video_youtobe" 
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate4._video_title
        url =self.ids.Plate4.text
        thumb =self.ids.Plate4._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_5(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate5._video_title
        url =self.ids.Plate5.text
        thumb =self.ids.Plate5._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_6(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate6._video_title
        url =self.ids.Plate6.text
        thumb =self.ids.Plate6._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_7(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate7._video_title
        url =self.ids.Plate7.text
        thumb =self.ids.Plate7._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_8(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate8._video_title
        url =self.ids.Plate8.text
        thumb =self.ids.Plate8._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_9(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate9._video_title
        url =self.ids.Plate9.text
        thumb =self.ids.Plate9._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_10(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate10._video_title
        url =self.ids.Plate10.text
        thumb =self.ids.Plate10._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_11(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate11._video_title
        url =self.ids.Plate11.text
        thumb =self.ids.Plate11._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
    def youtobe_video_12(self):
        global url_get
        self.ids.main.current = "video_youtobe"
        
        print('click')
        self.ids.youtobe_tiltle.text = self.ids.Plate12._video_title
        url =self.ids.Plate12.text
        thumb =self.ids.Plate12._image
        self.get_thumnail(thumb)
        self.ids.videoplay_2.thumbnail = "Video\\thumbnail.png"
        self.video_youtube_dowload(url)
        url_get=  url
        
        #Thread(target=self.gif_get(url)).start()
        
        
        
        
    def check_internet(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current = 'scr_1'
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
    def setting_app(self,*args):
        self.ids.main.current= 'setting_app'      
    def reload_check(self,*args):
        Clock.schedule_once(self.check_internet)
    def back_setting(self,*args):
        
        self.ids.main.current = 'scr_2'        
    global state_recognition    
    def state_recognition_capture(self,*args):
        global state_recognition, state_stream_recogntion
        state_recognition = 'Capture'
        self.ids.state_recognition_load.text = state_recognition
        self.ids.main.current= 'scr_2'
        state_stream_recogntion = "off"
       
        Clock.unschedule(self.stream_v1_get_data)
    
        Clock.unschedule(self.stream_v2_get_data)
        
        Clock.schedule_once(self.Stop_stream_camera)
        
    def state_recognition_stream(self,*args):
        global state_recognition, local
        state_recognition= 'Stream'
        self.ids.state_recognition_load.text = state_recognition +' '+ str(recognition_state)
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current= 'scr_2'
            Thread(target=self.Run_stream).start()
            if recognition_state =="V1":
                self.check_internet_streamv1()
                Thread(target=self.StreamV1_on).start()
                
                
            if recognition_state =="V2":
                self.check_internet_streamv2()
                Thread(target=self.StreamV2_on).start()
                
                
                
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
    global state_stream_recogntion 
    state_stream_recogntion = "off"
    
    
    
    def play_v1_stream(self):
        global state_recognition, local
        state_recognition= 'Stream'
        self.ids.state_recognition_load.text = state_recognition +' '+ str(recognition_state)
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current= 'scr_2'
 
            Thread(target=self.Run_stream).start()
            self.check_internet_streamv1()
            Thread(target=self.StreamV1_on).start()
 
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
            
            
            
    def play_v2_stream(self):
        global state_recognition, local
        state_recognition= 'Stream'
        self.ids.state_recognition_load.text = state_recognition +' '+ str(recognition_state)
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current= 'scr_2'
    
            Thread(target=self.Run_stream).start()
            self.check_internet_streamv2()
            Thread(target=self.StreamV2_on).start()
 
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'        
    
            
            
    def get_data_from_stream(self):
        global state_recognition,state_stream_recogntion
        if recognition_state =="V1":
            print('StreamV1_start')
            state_stream_recogntion = "start"
            Thread(target=self.check_internet_streamv1).start
            
            
            
        if recognition_state =="V2":
            print('StreamV2_start')
            state_stream_recogntion = "start"  
            Thread(target=self.check_internet_streamv2).start
            
    def StreamV1_on(self):
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current= 'scr_2'
            stream_V1_ip = local +'/streamv1'
            requests.get(stream_V1_ip)
            
            
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
            
    def StreamV2_on(self):
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current= 'scr_2'
            stream_V2_ip = local +'/streamv2'
            
            requests.get(stream_V2_ip)
            
            
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'

        
        
        
        
        
        
        
        
    def check_stream_internet(self,*args):
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            self.ids.main.current= 'scr_2'
        
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
            
            
            
            
            
            
            
    def Run_stream(self):
        if state_recognition =='Stream':
            ip_stream = local[:-4] + '8080'
            try:
                urlopen(ip_stream, timeout=1)
                print("Internet is active")
                self.videocapture = cv2.VideoCapture(0)
                Clock.schedule_interval(self.stream_to_flask,1/30)
                
            
            except urllib.error.URLError as Error:
                print(Error)
                print("Internet disconnected") 
                self.ids.main.current = 'disconnect_network_3'   
                
                
                
                
                
                
                
                
      
                
                
                
    
                      
    def Stop_stream_camera(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            stop_stream = local +'/change_state?state=2'
            requests.get(stop_stream)
           
            
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'      
            
            
    def check_internet_streamv1(self):
        
        Clock.schedule_interval(self.stream_v1_get_data,1/30)
        
    def stream_v1_get_data(self,*args):
        global local
        if state_stream_recogntion == "start":
            data_stream_v1 = local[:-4]+"5000"+'/get_data_stream_v1'
            data_streamv1 = requests.get(data_stream_v1).text
            self.ids.result_stream.text =data_streamv1
    
        print('Ok_stream')
        
    def check_internet_streamv2(self):
        if state_stream_recogntion == "start":
            Clock.schedule_interval(self.stream_v2_get_data,1/30)
        
    def stream_v2_get_data(self,*args):
        global local
        if state_stream_recogntion == "start":
            data_stream_v2 = local[:-4]+"5000"+'/get_data_stream_v2'
            data_streamv2 = requests.get(data_stream_v2).text
            self.ids.result_stream.text =data_streamv2
        
        
            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def check_internet_1(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            downloadUrl = local+'/uploader4'

            req = requests.get(downloadUrl)
            filename =req.url[downloadUrl.rfind('/')+1:]+'.mp4'

            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'    
            
    def check_internet_pro(self,*args):
        global local
        #try:
        #    urlopen(local, timeout=1)
        #    print("Internet is active")
        #    StreamV1 = local+'/streamv1'

        #    Stream_result = requests.get(StreamV1).text
        #    self.ids.result_stream.text = Stream_result

      
#        except urllib.error.URLError as Error:
#            print(Error)
#            print("Internet disconnected") 
#            self.ids.main.current = 'disconnect_network_3'  
          

    
        
    def dowloadvideo(self,*args):
        Clock.schedule_once(self.check_internet_1)
        
    def check_internet_2(self,*args):
        global local,search_data
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            input_search = self.ids.searching.text
            downloadUrl2 = local+'/returnsignimg?input='+input_search
            req = requests.get(downloadUrl2)
            api2 = local +'/signdata?input='+input_search
            bodyresponse = requests.get(api2).text
            search_data = bodyresponse
            with open(str(search_data), 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        
            self.cus2 =Factory.Signbottomsheet()
            self.obj2 = MDCustomBottomSheet(screen = self.cus2)
            self.cus2.ids.signsearch.source = search_data
            self.obj2.open()     
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'  
        
    def choose(self):
        
        filechooser.open_file(on_selection=self.handle_selection)
    def search_result(self, *args): 
        Clock.schedule_once(self.check_internet_2)
    def check_internet_3(self,*args):
        global local,search_data
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            input_search = self.ids.searching.text
            api2 = local +'/signdata?input='+input_search
            bodyresponse = requests.get(api2).text
            search_data = bodyresponse
            print(search_data)
            if search_data != "None":
                Clock.schedule_once(self.search_result)   
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'  
            
            
            
    def choose_pro(self):
        
        filechooser.open_file(on_selection=self.handle_selection_pro_3)   
        
        
    def handle_selection_pro_3(self, selection):
        
        
        self.selection = selection
        if str(selection) == '[]':
            self.pathname = ''
        else: 
            
            self.pathname = selection[0]
        print(self.pathname)
        if self.pathname =='':
            print('None')
        else:
            self.ids.pathname_src.text= self.pathname
            Clock.schedule_once(self.load_video_translate)
    def load_video_translate(self,*args):
        self.ids.videoplay_31.source= self.pathname
        
        self.ids.main.current = "video_translate"
        
    
        
    def searching(self,*args):
        Clock.schedule_once(self.check_internet_3)
       
    def handle_selection(self, selection):
        
        
        self.selection = selection
        if str(selection) == '[]':
            self.pathname = ''
        else: 
            
            self.pathname = selection[0]
        print(self.pathname)
        if self.pathname =='':
            print('None')
        else:
            self.ids.main.current= 'load'
            Thread(target=self.recogntion_1_thread).start()
    
    def recogntion_1_thread(self):
        Clock.schedule_once(self.recognition_image)
        
    def recogntion_2_thread(self):
        Clock.schedule_once(self.recognition_video,5)
    def choose2(self):
        filechooser.open_file(on_selection=self.handle_selection2)
    def handle_selection2(self, selection):
       
        self.selection = selection
        if str(selection) == '[]':
            self.pathname = ''
        else: 
            self.ids.main.current= 'load'
            self.pathname = selection[0]
        print(self.pathname)
        if self.pathname =='':
            print('None')
        else:
            Thread(target=self.recogntion_2_thread).start()
    global imagenumber, filename    ,img
    imagenumber = 1
    
    def check_internet_4(self,*args):
        global local, imagenumber, filename,img
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            api  = local + '/bodyimg2'
            im_b64 = requests.get(api).text
            img_bytes = base64.b64decode(im_b64.encode('utf-8'))
            np_data = np.fromstring(img_bytes,np.uint8)
            img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
            
            filename =str(imagenumber) + ".png"
            cv2.imwrite(filename, img)
    
            imagenumber = imagenumber+ 1
            self.ids.main.current = 'pictureshow'
            self.ids.imagedetect.source=filename
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'  
    
    def base64_to_img_2(self,*args):
        
       Clock.schedule_once(self.check_internet_4)
    def check_internet_5(self,*args):
        global local,filename,img
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            myurl = local + '/uploader2'
            files = {'file': open(self.pathname, 'rb')}
            getdata = requests.post(myurl, files=files)
            Clock.schedule_once(self.base64_to_img_2)
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'  
    def recognition_image(self,*args):
        Clock.schedule_once(self.check_internet_5)
       
   
       
     
    
   
            
    def check_internet_6(self,*args):
        global local,filename,img
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            myurl = local + '/uploader3'
            files = {'file': open(self.pathname, 'rb')}
            getdata = requests.post(myurl, files=files)
        
                
            Clock.schedule_once(self.dowloadvideo)
            self.ids.videoplay.source= 'uploader4.mp4'
            self.ids.main.current = 'video'
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'  
    def recognition_video(self,*args):
 
        Clock.schedule_once(self.check_internet_6)
        
        
    def open_new(self):
        self.ids.main.current='scr_5'
    def back_pro(self):
        self.ids.main.current='scr_1'
    def pro_1(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='vnlanguage.jpg'
    def back_scr(self):
        self.ids.main.current='scr_5'
    

        
    def pro_2(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Basic1.png'
    def pro_3(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Family.png'
    def pro_4(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Question.png'
    def pro_5(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='transport2.png'
    def pro_6(self):
        self.ids.main.current='scr_7'
        self.ids.bodyimgpro.source='Time.png'
        self.ids.bodyimg2.source='Time2.png'
    def pro_7(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Clothes.png'
    def pro_8(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Color.png'
    def pro_9(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Body_1.png'
    def pro_10(self):
        self.ids.main.current='scr_7'
        self.ids.bodyimgpro.source='Emotion.png'
        self.ids.bodyimg2.source='Emotion2.png'
    def pro_11(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='Medical.png'
    def pro_12(self):
        self.ids.main.current='scr_6'
        self.ids.bodyimg.source='House.png'
    #def capture(self):
    
    #    camera = self.ids['camera']
        

    #    pixels_data = camera.texture.get_region(x=camera.x, y=camera.y, width=camera.resolution[0],
    #                                            height=camera.resolution[1]).pixels
    #    image = PIL.Image.frombytes(mode="RGBA", size=(int(camera.resolution[0]), int(camera.resolution[1])),
                                    #data=pixels_data)

    #    pil_image = image.convert('RGB')
    #    open_cv_image = np.array(pil_image)
  
    #    img1 = open_cv_image[:, :, ::-1].copy()

    
    #    ObjectScreen.file_write(img1)



    def file_write(image):
        global save_image_obj
        timestr = time.strftime("%Y%m%d_%H%M%S")
        print(timestr)
        save_image_obj = "img\\" + str(random.randint(1,10000))+ str(random.randint(1,1000))+"Day"+timestr+".png"
        cv2.imwrite(save_image_obj, image)
       

        
    def run_camera(self):
        
        self.ids.main.current='scr_2'
  
    
    #def capture(self):
      
    #    camera = self.ids.camera
    #    camera.export_to_png("photo2.png")
       
    #    self.path_save = "photo2.png"
    
            

                        
        #sp.run(['python','Screens\ObjectScreen\BodyLanguage\detect.py'], shell=True)
        
    
    def image_show(self):
        scr4  = self.ids.scr_4
        layout_2 = MDBoxLayout(orientation= 'vertical')
        scr4.add_widget(layout_2)
    def back(self,*args):
        self.ids.main.current ='scr_1'
     

        
    def open_1(self):
        
        self.cus =Factory.CustomBottomSheet()
        self.cus.ids.Button.bind(on_press=self.input_data_2)
        self.cus.ids.Button_2.bind(on_press= self.bodylanguage_call_2)
        self.cus.ids.Button_3.bind(on_press = self.clear)
        self.cus.ids.Change.bind(on_press = self.change_trans)
        self.cus.ids.Audio.bind(on_press = self.Audio_read)
        self.cus.ids.Picture.bind(on_press = self.show_image)
        self.obj = MDCustomBottomSheet(screen = self.cus)
        self.obj.open()   
    def process_data(self):
        global state_load
        if state_load =='text':
            Clock.schedule_once(self.img_recognition_text)
        if state_load =='body':
            Clock.schedule_once(self.body_recognition)    
    def check_internet_7(self,*args):
        global local,save_image_obj
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            myurl = local + '/uploadfromcamera'
            files = {'file': open(save_image_obj, 'rb')}
            getdata = requests.post(myurl, files=files)
            response = getdata
            save_label_txt = open('label_name.txt', mode= 'a+')
            label_saved = save_label_txt.write(response.text)
            save_label_txt.close
            Clock.schedule_once(self.open_cus)
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
    
    def body_recognition(self,*args):
        
        Clock.schedule_once(self.check_internet_7)
       
        #self.cus =Factory.CustomBottomSheet()
        #self.cus.ids.Button.bind(on_press=self.input_data_2)
        #self.cus.ids.Button_2.bind(on_press= self.bodylanguage_call_2)
        #self.cus.ids.Button_3.bind(on_press = self.clear)
        #self.cus.ids.Change.bind(on_press = self.change_trans)
        #self.cus.ids.Audio.bind(on_press = self.Audio_read)
        #self.cus.ids.Picture.bind(on_press = self.show_image)
        #self.obj = MDCustomBottomSheet(screen = self.cus)
        #self.obj.open()   
        #self.cus.ids.textinput_bdl.text = self.cus.ids.textinput_bdl.text + response.text
    def open_cus(self, *args): 
        global response
        if state_load =='body':
            file_obj = open('label_name.txt')
            data = file_obj.read()
            file_obj.close()
        elif state_load =='text':
            data = response.text
        self.cus =Factory.CustomBottomSheet()
        self.cus.ids.Button.bind(on_press=self.input_data_2)
        self.cus.ids.Button_2.bind(on_press= self.bodylanguage_call_2)
        self.cus.ids.Button_3.bind(on_press = self.clear)
        self.cus.ids.Change.bind(on_press = self.change_trans)
        self.cus.ids.Audio.bind(on_press = self.Audio_read)
        self.cus.ids.Picture.bind(on_press = self.show_image)
        self.obj = MDCustomBottomSheet(screen = self.cus)
        self.obj.open()    
        self.cus.ids.textinput_bdl.text = data
    global state_load
    state_load = 'body'
    def state(self):
        global state_load
        if state_load =='body':
            state_load ='text'
            
        else:
            state_load = 'body'
    global recognition_state
    recognition_state = 'V1'
    def RTRecognition(self):
        global recognition_state
        if recognition_state =='V1':
            recognition_state ='V2'
            
        else:
            recognition_state = 'V1'
        print(recognition_state)
    def check_internet_8(self,*args):
        global api, response, local
        
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            api = local + "/etext"
            image_file = 'photo2.png'

            with open(image_file, "rb") as f:
                im_bytes = f.read()        
            im_b64 = base64.b64encode(im_bytes).decode("utf8")

            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            
            payload = json.dumps({"image": im_b64, "other_key": "value"})
            response = requests.post(api, data=payload, headers=headers)
            Clock.schedule_once(self.open_cus)
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
           
    def img_recognition_text(self,*args):
        Clock.schedule_once(self.check_internet_8)
        
        
    def check_internet_9(self,*args):
        global api, response, local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            print(self.cus.ids.textinput_bdl.text)
            Clock.schedule_once(self.remove_sign_2)
            text_input_bdl =self.cus.ids.textinput_bdl.text
            self.secondspinner_bdl = self.cus.ids.secondvalue_bdl.text 
            self.firstspinner_bdl  = self.cus.ids.firstvalue_bdl.text
                        
            
            
            api  = local + '/etrans'+'?textinput='+text_input_bdl+'&src='+self.firstspinner_bdl+'&dest='+self.secondspinner_bdl
            response = requests.get(api).text 
            b = response
            self.cus.ids.textoutput_bdl.font_name = 'Cucho.otf'
            self.cus.ids.textoutput_bdl.text = b
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
    
    def input_data_2(self,*arg):
    
        Clock.schedule_once(self.check_internet_9)
       

    
    def clear(self,*args):
        self.cus.ids.textinput_bdl.text = ''
        self.cus.ids.textoutput_bdl.text = ''
        
        file_object = open('label_name.txt', mode ='w')
        data_clear = file_object.write('')
        file_object.close()
    global datasign
    datasign=0
    
    def check_internet_10(self,*args):
        global datasign, local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            text_input =self.cus.ids.textinput_bdl.text
            if datasign == 0:
                signimage = Image(source="",size_hint=(1,2))
                self.cus.ids.textoutputbox.add_widget(signimage)
                self.cus.ids["sign2"]=signimage
                datasign = 1  
                
            api2 = local +'/signdata?input='+text_input
            bodyresponse = requests.get(api2).text
            result = bodyresponse
            print(result)
            if result != "None":
                Clock.schedule_once(self.returnimage2)
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
                
    def add_sign2(self,*args):
        Clock.schedule_once(self.check_internet_10)
        
        
            
            
    def remove_sign_2(self,*args):
        global datasign
        if datasign==1:
            self.cus.ids.textoutputbox.remove_widget(self.cus.ids.sign2)
            datasign =0
    def check_internet_11(self,*args):
        global datasign, local
        
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            text_input_bdl =self.cus.ids.textinput_bdl.text
            self.secondspinner_bdl = self.cus.ids.secondvalue_bdl.text 
            self.firstspinner_bdl  = self.cus.ids.firstvalue_bdl.text
                        
            
            api2 = local +'/signdata?input='+text_input_bdl
            bodyresponse = requests.get(api2).text
            result = bodyresponse
            filename =result
            downloadUrl = local+'/returnsignimg?input='+text_input_bdl
            req = requests.get(downloadUrl)
            print(result)
            with open(str(filename), 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            self.cus.ids.sign2.source= filename
            self.cus.ids.textoutputbox.text =''
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'        
            
    def returnimage2(self,*args):
     
        Clock.schedule_once(self.check_internet_11)
       
        
        
    def bodylanguage_call_2(self,*args):
        global local

        print(self.cus.ids.textinput_bdl.text)
        text_input_bdl =self.cus.ids.textinput_bdl.text
        self.secondspinner_bdl = self.cus.ids.secondvalue_bdl.text 
        self.firstspinner_bdl  = self.cus.ids.firstvalue_bdl.text
                   
        Clock.schedule_once(self.add_sign2)
        #self.cus.ids.textoutput_bdl.font_size = '50'
        #self.cus.ids.textoutput_bdl.font_name = 'Bodylanguage-Regular.ttf'
        #self.cus.ids.textoutput_bdl.text = b
        print('b')
        
    def change_trans(self,*args):
        
        self.spiner_1 = self.cus.ids.firstvalue_bdl.text
        self.spiner_2 = self.cus.ids.secondvalue_bdl.text
        
        self.cus.ids.firstvalue_bdl.text = self.spiner_2
        self.cus.ids.secondvalue_bdl.text =  self.spiner_1 
        
    def Audio_read(self,*args):
        if stt.listening:
            self.stop_listening()
            return
        self.cus.ids.Audio.icon = 'record-circle'
        self.cus.ids.textinput_bdl.text = ''
        stt.start()

        Clock.schedule_interval(self.check_state, 1 /5)
    def stop_listening(self):
        self.cus.ids.Audio.icon = 'account-tie-voice'
        stt.stop()
        self.update()
        Clock.unschedule(self.check_state)
    def check_state(self, dt):
        # if the recognizer service stops, change UI
        if not stt.listening:
            self.stop_listening()
    def update(self):
        self.cus.ids.textinput_bdl.text = '\n'.join(stt.results)


    
        
        
        
    def change_state(self):
        statement_change = self.ids.rec.text
       
        if statement_change == '1':
            self.ids.rec.text = '0'
            print(self.ids.rec.text)
            self.ids.rec_image.source = 'icons8-record-100.png'
            self.out.release()
        elif statement_change== '0':
            
            self.ids.rec.text = '1'
            print(self.ids.rec.text)
            
            self.ids.rec_image.source ='icons8-stop-squared-100.png' 
            
            
            
        
        
    def show_image(self,*args):
       
        Clock.schedule_once(self.base64_to_img)
        
        
    def back_record(self):
        self.ids.main.current='scr_2'
    
    def back_2(self):
        global state_recognition, state_stream_recogntion
        state_recognition = 'Capture'
        self.ids.state_recognition_load.text = state_recognition
        self.ids.main.current= 'scr_1'
        state_stream_recogntion = "off"
       
        Clock.unschedule(self.stream_v1_get_data)
    
        Clock.unschedule(self.stream_v2_get_data)
        
        Clock.schedule_once(self.Stop_stream_camera)
        
    global imagenum
    imagenum = 10000
    
    
            
    def check_internet_12(self,*args):
        global local,imagenum
        
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            api  = local + '/bodyimg'
            im_b64 = requests.get(api).text
            img_bytes = base64.b64decode(im_b64.encode('utf-8'))
            np_data = np.fromstring(img_bytes,np.uint8)
            img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
            filename2 = str(imagenum) + ".png"
            cv2.imwrite(filename2, img)
            self.ids.image_base.source = filename2
            self.ids.main.current = 'scr_4'
            imagenum= imagenum + 1
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'       
    def base64_to_img(self,*args):
        Clock.schedule_once(self.check_internet_12)
   
    def youtobe_back_screen(self):
        self.ids.main.current = "scr_1" 
    def youtobe_back_screen_2(self):
        self.ids.main.current = "youtobe"
   
        #for i in range(0,2):
        #    print(videos[1]["url"])
        #    id_video =videos[1]["url"]
        #    thumbnail = (id_video).thumbnail_url
        #    thumbnail_pro=str("Plate"+i)
    
        #    self.ids.thumbnail_pro._image=thumbnail
    
        
    def load_url_2(self):
        global thumbnail_pro
        self.ids.main.current="load"
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            api  = local + '/playlist'
            request= requests.get(api).text
           
            with open("video_url.txt", mode="w+", encoding ="utf-8") as url:
                url.write(request)    
                
                
            with open("video_url.txt", mode="r", encoding ="utf-8") as read:    
                yt_playlist =   read.readlines()
            for k in range(1,12):
                
                print(yt_playlist[k].replace("\n",""))
                id_video =yt_playlist[k].replace("\n","")
            
                thumbnail = YouTube(id_video).thumbnail_url
                title = YouTube(id_video).title
                author=  YouTube(id_video).author
                views = YouTube(id_video).views
                time_video = YouTube(id_video).length
                public_date = YouTube(id_video).publish_date
                name = author +" - "+ str(views)+"-Views"+"                            "+str(public_date)[:-9]
                import datetime
                SecToConvert = time_video
                ConvertedSec = str(datetime.timedelta(seconds = SecToConvert))
                thumbnail_pro="Plate"+str(k)
                self.ids[thumbnail_pro].text=yt_playlist[k].replace("\n","")
                self.ids[thumbnail_pro]._image=thumbnail
                self.ids[thumbnail_pro]._video_title = title
                self.ids[thumbnail_pro]._channel_name = name
                self.ids[thumbnail_pro]._time = ConvertedSec
                self.ids.main.current = "youtobe"
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'
    global num_i,read_gif
    def video_youtube_dowload(self,url):
        global read_gif
        

        yt = YouTube(url, on_progress_callback=on_progress)
        file_name = "Video\\video.mp4"
        try:
            stream = yt.streams.filter(progressive=True, file_extension="mp4").get_by_resolution("360p")
            stream.download(filename=file_name)
            
            self.ids.videoplay_2.source= file_name
            
            #urlopen(local, timeout=1)
            #print("Internet is active")
            #api  = local + '/gifdata?input_url='
            
           # gif_data = requests.get(api+url_get).text
            
            
        
        #           time.sleep(5) 
        
            
        except:
            print('No result')
            
        self.sub(url)
    def search_video(self):
        global local
        try:
            
            urlopen(local, timeout=1)
            print("Internet is active")
            search = self.ids.search_yt.text
            api  = local + '/search_video?input='+search 
            request= requests.get(api).text
            
            with open("search_url.txt", mode="w+", encoding ="utf-8") as url:
                url.write(request)    
                
                
            with open("search_url.txt", mode="r", encoding ="utf-8") as read:    
                result =   read.readlines()
        
            for i in range(1,12):
                print("https://www.youtube.com/watch?v="+result[i].replace("\n",""))
                url_new = "https://www.youtube.com/watch?v="+result[i].replace("\n","")
                thumbnail = YouTube(url_new).thumbnail_url
                title = YouTube(url_new).title
                author=  YouTube(url_new).author
                views = YouTube(url_new).views
                time_video = YouTube(url_new).length
                public_date = YouTube(url_new).publish_date
                name = author +" - "+ str(views)+"-Views"+"                            "+str(public_date)[:-9]
                import datetime
                SecToConvert = time_video
                ConvertedSec = str(datetime.timedelta(seconds = SecToConvert))
                thumbnail_pro="Plate"+str(i)
                self.ids[thumbnail_pro].text=url_new
                self.ids[thumbnail_pro]._image=thumbnail
                self.ids[thumbnail_pro]._video_title = title
                self.ids[thumbnail_pro]._channel_name = name
                self.ids[thumbnail_pro]._time = ConvertedSec       
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'     
        
           
    def get_thumnail(self,url_thumnail):
        thumbnail = requests.get(url_thumnail)
        path = "Video\\thumbnail.png"
        with open(path,"wb") as f:
            f.write(thumbnail.content)        
    def gif_get(self):
        global local,url_get
        print(url_get)
        Clock.schedule_once(self.check_internet_video)
        self.ids.videoplay_3.source= "gifdata.mp4"
        
    global data_get
    data_get= "/vivian"
        
    def check_internet_video(self,*args):
        global local, data_get, url_get
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            downloadUrl = local+data_get+"?input="+url_get

            
         
            filename = "gifdata.mp4"
            
            with open(filename, 'wb') as f:
                req = requests.get(downloadUrl,stream=True)
                total_length = req.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(req.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in req.iter_content(chunk_size=8192):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                        
                        sys.stdout.flush()
                        
            
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'    
            
        self.progress_bar()
           
    def progress_bar(self):
        for bar in range (0,100):
            self.ids.progress_2.value = bar
            
        
    #num_i =0
    #def change_gif(self,*args):
    #    global num_i,read_gif
    #    with open("gif_image.txt", mode="r", encoding="utf-8") as h:
    #        read_gif = h.readlines()
      
    #    self.ids.gif_img.source = read_gif[num_i].replace("\n","")
    #    print(read_gif[num_i])
    #    num_i=num_i+1    
    global sub_num
    def sub(self, url_video_sub):
        global sub_num 
        sub_num = -1
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            downloadUrl = local+'/sub?input='+url_video_sub
            sub = requests.get(downloadUrl).text
            with open("sub.txt", mode="w+", encoding = "utf-8") as w:
                w.write(sub)
            
       
                
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3' 
        
   
    
       
    def sub_next(self):
        global sub_num
        with open("sub.txt", mode="r+", encoding = "utf-8") as w:
            sub = w.readlines()
            if sub_num <= len(sub)-1 and sub_num >= -1:
                sub_num= sub_num+1
                if sub_num < len(sub):
                    self.ids.sub.text = sub[sub_num]
                    print(sub_num)
                
                
            
    def sub_back(self):
        global sub_num
        
        with open("sub.txt", mode="r+", encoding = "utf-8") as w:
            sub = w.readlines()
            if sub_num <= len(sub)+1 and sub_num > 0:
                sub_num= sub_num-1
                self.ids.sub.text = sub[sub_num]
                print(sub_num)
            
    
        
            
    def character(self):
        self.cus3 =Factory.Character()
        self.obj3 = MDCustomBottomSheet(screen = self.cus3)
        self.cus3.ids.human.bind(on_press = self.human)
        self.cus3.ids.vivian.bind(on_press = self.vivian)
        self.obj3.open() 
    
    def character_new(self):
        self.cus3 =Factory.Character()
        self.obj3 = MDCustomBottomSheet(screen = self.cus3)
        self.cus3.ids.human.bind(on_press = self.human)
        self.cus3.ids.vivian.bind(on_press = self.vivian)
        self.obj3.open() 
            
        
    def human(self,*args):
        global data_get 
        data_get = "/gifdata"
        self.ids.name_character.text = "Human"
        self.ids.name_character_new.text = "Human"
        self.ids.character_choose.text = "Human"
        self.obj3.dismiss()
        
    def vivian(self,*args):
        global data_get 
        data_get = "/vivian"
        self.ids.name_character.text = "Vivian"
        self.ids.name_character_new.text = "Vivian"
        self.ids.character_choose.text = "Vivian"
        self.obj3.dismiss()
        
    def video_to_sign(self):
        print("hello world")
    
 
        
        
    def check_internet_video_2(self,*args):
        global local, data_get
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            downloadUrl = local+data_get+"2"

            
         
            filename = "gifdata.mp4"
            
            with open(filename, 'wb') as f:
                req = requests.get(downloadUrl,stream=True)
                total_length = req.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(req.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in req.iter_content(chunk_size=8192):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                        
                        sys.stdout.flush()
                        
                        
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'    
            
            
    def mp3_upload(self,*args):
        global local,filename,img
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            myurl = local + '/uploadermp3'
            files = {'file': open(self.pathname, 'rb')}
            getdata = requests.post(myurl, files=files)
        
                
            Clock.schedule_once(self.check_internet_dowload)
            self.ids.videoplay_32.source= 'gifdata2.mp4'
            Clock.schedule_once(self.progress_bar_2)
        
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3' 
            
    def check_internet_dowload(self,*args):
        global local
        try:
            urlopen(local, timeout=1)
            print("Internet is active")
            downloadUrl = local+'/uploadermp3pro'

            req = requests.get(downloadUrl)
            filename = "gifdata2.mp4"

            with open(filename, 'wb') as f:
                req = requests.get(downloadUrl,stream=True)
                total_length = req.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(req.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in req.iter_content(chunk_size=8192):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                        
                        sys.stdout.flush()
        except urllib.error.URLError as Error:
            print(Error)
            print("Internet disconnected") 
            self.ids.main.current = 'disconnect_network_3'   
            
            
    def progress_bar_2(self,*args):
        for bar in range (0,100):
            self.ids.progress_new.value = bar

    def build_camera(self):
    
        
        self.videocapture = cv2.VideoCapture(0)
        
        Clock.schedule_interval(self.update_camera, 1.0/33.0)
    
        

    def update_camera(self,*args):
       
        ret, frame = self.videocapture.read()
    

        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 

        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
       
        self.ids.img_camera.texture = texture1

    def stream_to_flask(self,*args):
        global local
        if state_recognition =='Stream':
            
            ret,frame = self.videocapture.read()
            #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            _, imdata = cv2.imencode('.JPG', frame)
            ip_stream = local[:-4] + '8080'
            ip= ip_stream+ '/upload'
            requests.put(ip, data=imdata.tobytes())