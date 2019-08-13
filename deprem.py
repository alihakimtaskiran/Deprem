import requests
import time as t
import notify2 as not2

url="http://www.koeri.boun.edu.tr/scripts/lst2.asp"

def get_earthquake():  
    
    #get latest earthquakes from http://www.koeri.boun.edu.tr/scripts/lst2.asp
    url="http://www.koeri.boun.edu.tr/scripts/lst2.asp"
    html=["No internet connection"]
    ok=0
    
    try:
        requests.get(url)
    except:
        print("Internet Connection Error")
        ok=1
        
    #if there is no error ok variable is equal to 0 and the program works correctly
    if ok==0: 
        html=requests.get(url).text
        #clear the text from unnecessary parts. Such as header, banner etc...
        x=(html.index("--------------"),html.index('</pre>'))
        html=html[x[0]:x[1]].splitlines()[1:500]
        
        #split the data into date, location and magnitude 
        html_=[]
        for i in html:
            html_.append(i.split(" "))
            
        html=[]
        
        for data in html_:
            scl=[]#scarp list
            for i in range(len(data)):
                if data[i]=="":
                    scl.append(i)
            scl.reverse()
            for i in scl:
                data.pop(i)
            html.append(data)
        html_=[]     
    else:
        print("Connect internet") 
    
    return html
        

'''Main loop'''

while True:
    html=get_earthquake()
    if html[0]=="No internet connection":
        not2.init("Deprem")
        n=not2.Notification("Deprem","Deprem bilgilerini almak için internete bağlanın.")
        n.show()
    else:
        try:
            if not latest_earthquake==html[0]:
                not2.init("Deprem")
                output=html[0][8]+html[0][9]+" bölgesinde "+html[0][6]+" şiddetinde deprem."
                n=not2.Notification("Deprem",output)
                n.show()
        except:
            not2.init("Deprem")
            output=html[0][8]+html[0][9]+" bölgesinde "+html[0][6]+" şiddetinde deprem."
            n=not2.Notification("Deprem",output)
            n.show()               
    t.sleep(300)
    latest_earthquake=html[0]

    


            
