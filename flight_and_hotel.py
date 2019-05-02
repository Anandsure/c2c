from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
import math
'''import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()'''

pl=[]
dates=[]
def talkToMe(audio):

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)




def myCommand():
   

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')


    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    

 
            
    if 'bye' in command:
        talkToMe('See ya soon! bye    bye byebyebyee')
        exit()

    elif 'trip' in command:
        talkToMe('let\'s start with the flight plan')
        talkToMe('where are you from?')
        loc= myCommand()
        talkToMe('noted1 %s'%loc)
        pl.append(loc)
        talkToMe('where do you want to fly to?')
        dest= myCommand()
        talkToMe('Okay!, So you want to fly to %s'%dest)
        pl.append(dest)
        talkToMe('when are you flying?(date, month, year')
        date= myCommand()
        if 'january' in date:
            month='01'
        elif 'february' in date:
            month='02'
        elif 'march' in date:
            month='03'
        elif 'april' in date:
            month='04'
        elif 'may' in date:
            month='05'
        elif 'june' in date:
            month='06'
        elif 'july' in date:
            month='07'
        elif 'august' in date:
            month='08'
        elif 'september' in date:
            month='09'
        elif 'october' in date:
            month=10
        elif 'november' in date:
            month=11
        elif 'december' in date:
            month=12
        year=date[-1:-5:-1]
        year=year[::-1]
        day=date[0:2]
        #print(month,"\n",day,"\n",year)
        talkToMe('how many adults?')
        adu= myCommand()
        talkToMe('children?')
        chi= myCommand()
        talkToMe('infants?')
        inf= myCommand()
        if(adu=='zero'):
            adu==0
        if(chi=='zero'):
            chi=0
        if(inf=='zero'):
            inf=0

        talkToMe('are you flying back?')
        c= myCommand()
        airports={'chennai':'MAA','delhi':'DEL','bangalore':'BLR','kolkata':'CCU','mumbai':'BOM','pune':'PNQ','hyderabad':'HYD','guwahati':'GAU','goa':'GOI','chandigarh':'IXC','shimla':'SLV','patna':'PAT','bhubhaneshwar':'BBI','ahmedabad':'AMD','trivandrum':'TRV','jaipur':'JAI','vizag':'VTZ','raipur':'RPR','diu':'DIU','jamshedpur':'IXW','ranchi':'IXR','mangalore':'IXE'}

        if(c=='no'):
            c='no'
            talkToMe('lets get your hotel preferences in now..')
            talkToMe('provide your hotel check-out dates')
            date1= myCommand()
            if 'january' in date1:
                month1='01'
            elif 'february' in date1:
                month1='02'
            elif 'march' in date1:
                month1='03'
            elif 'april' in date1:
                month1='04'
            elif 'may' in date1:
                month1='05'
            elif 'june' in date1:
                month1='06'
            elif 'july' in date1:
                month1='07'
            elif 'august' in date1:
                month1='08'
            elif 'september' in date1:
                month1='09'
            elif 'october' in date1:
                month1=10
            elif 'november' in date1:
                month1=11
            elif 'december' in date1:
                month1=12
            year1=date1[-1:-5:-1]
            year1=year1[::-1]
            day1=date1[0:2]
            talkToMe('what is your budget? (2000-40000+)')
            bud= int(myCommand())
            bud= math.ceil(1.27 * bud)
            bud = str(bud)
            print(bud)
            cpt={'pune': '84040' , 'goa' : '64932','delhi':'64967','chennai':'64991','mumbai':'64981','guwahati':'344953','hyderabad':'64958','kolkata':'64995','bangalore':'5177556'}
            
            if(adu=='2'):
                url = 'https://www.trivago.in/?aDateRange%5Barr%5D='+year+'-'+month+'-'+day+'&aDateRange%5Bdep%5D='+year1+'-'+month1+'-'+day1+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D='+bud+'&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2='+cpt[dest]+'%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'
                
                webbrowser.open(url)
            elif(adu=='1'):
                url = 'https://www.trivago.in/?aDateRange%5Barr%5D='+year+'-'+month+'-'+day+'&aDateRange%5Bdep%5D='+year1+'-'+month1+'-'+day1+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D='+bud+'&iRoomType=1&aRooms%5B0%5D%5Badults%5D=2&cpt2='+cpt[dest]+'%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'
                webbrowser.open(url)
            elif(adu=='3' or adu=='4'):
                url = 'https://www.trivago.in/?aDateRange%5Barr%5D='+year+'-'+month+'-'+day+'&aDateRange%5Bdep%5D='+year1+'-'+month1+'-'+day1+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D='+bud+'&iRoomType=9&aRooms%5B0%5D%5Badults%5D='+adu+'&aRooms%5B0%5D%5Bchildren%5D%5B0%5D='+chi+'&aRooms%5B0%5D%5Bchildren%5D%5B1%5D=7&aRooms%5B0%5D%5Bchildren%5D%5B2%5D=13&aRooms%5B0%5D%5Bchildren%5D%5B3%5D=15&cpt2='+cpt[dest]+'%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'
                webbrowser.open(url)
            webbrowser.open('https://www.goibibo.com/flights/air-%s-%s-%s%s%s--%s-%s-%s-E-D/'%(airports[loc],airports[dest],year,month,day,adu,chi,inf))
        else:
            talkToMe('when are you flying back?date, month, year')
            date1= myCommand()
            if 'january' in date1:
                month1='01'
            elif 'february' in date1:
                month1='02'
            elif 'march' in date1:
                month1='03'
            elif 'april' in date1:
                month1='04'
            elif 'may' in date1:
                month1='05'
            elif 'june' in date1:
                month1='06'
            elif 'july' in date1:
                month1='07'
            elif 'august' in date1:
                month1='08'
            elif 'september' in date1:
                month1='09'
            elif 'october' in date1:
                month1=10
            elif 'november' in date1:
                month1=11
            elif 'december' in date1:
                month1=12
            year1=date1[-1:-5:-1]
            year1=year1[::-1]
            day1=date1[0:2]

            talkToMe('lets get your hotel preferences in now..')
            talkToMe('what is your budget? (2000-40000+)')
            bud= int(myCommand())
            bud= math.ceil(1.27 * bud)
            bud = str(bud)
            print(bud)
            cpt={'pune': '84040' , 'goa' : '64932','delhi':'64967','chennai':'64991','mumbai':'64981','guwahati':'344953','hyderabad':'64958','kolkata':'64995','bangalore':'5177556','chandigarh':'64988','shimla':'64971','patna':'64961','ahmedabad':'85528','trivandrum':'3234826','jaipur':'64989','vizag':'101236','raipur':'64963','diu':'64965','jamshedpur':'344983','ranchi':'64974','mangalore':'85357'}
            
            if(adu=='2'):
                url = 'https://www.trivago.in/?aDateRange%5Barr%5D='+year+'-'+month+'-'+day+'&aDateRange%5Bdep%5D='+year1+'-'+month1+'-'+day1+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D='+bud+'&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2='+cpt[dest]+'%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'
                #webbrowser.open('https://www.trivago.in/?aDateRange%5\Barr%5\D=%s-%s-%s&aDateRange%5\Bdep%5\D=%s-%s-%s&aPriceRange%5\Bfrom%5\D=0&aPriceRange%5\Bto%5\D=%d&iRoomType=7&aRooms%5\B0%5\D%5\Badults%5\D=2&cpt2=%s%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'%(year,month,day,year1,month1,day1,bud,cpt[dest]))
                webbrowser.open(url)
            elif(adu=='1'):
                url = 'https://www.trivago.in/?aDateRange%5Barr%5D='+year+'-'+month+'-'+day+'&aDateRange%5Bdep%5D='+year1+'-'+month1+'-'+day1+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D='+bud+'&iRoomType=1&aRooms%5B0%5D%5Badults%5D=2&cpt2='+cpt[dest]+'%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'
                webbrowser.open(url)
            elif(adu=='3' or adu=='4'):
                url = 'https://www.trivago.in/?aDateRange%5Barr%5D='+year+'-'+month+'-'+day+'&aDateRange%5Bdep%5D='+year1+'-'+month1+'-'+day1+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D='+bud+'&iRoomType=9&aRooms%5B0%5D%5Badults%5D='+adu+'&aRooms%5B0%5D%5Bchildren%5D%5B0%5D='+chi+'&aRooms%5B0%5D%5Bchildren%5D%5B1%5D=7&aRooms%5B0%5D%5Bchildren%5D%5B2%5D=13&aRooms%5B0%5D%5Bchildren%5D%5B3%5D=15&cpt2='+cpt[dest]+'%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0'
                webbrowser.open(url)
            
            webbrowser.open('https://www.goibibo.com/flights/air-%s-%s-%s%s%s-%s%s%s-%s-%s-%s-E-D/'%(airports[loc],airports[dest],year,month,day,year1,month1,day1,adu,chi,inf))
            
            
        
        
        
        
        
                
        
        
        
        
        


talkToMe('I am ready for your command')


while True:
    assistant(myCommand())
