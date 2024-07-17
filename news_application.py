import requests
import webbrowser
from tkinter import*
from urllib.request import urlopen
from PIL import ImageTk,Image
import io
#class for news app
class newsapp:
#constructor to fetch data
    def __init__(self):
 #fetching data by get method where we have to provide url 
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=c1fbed1a49324107b4b78fefca6737a0').json()
    
 #call gui function
        self.load_gui()
        self.news_load(0)

#make a gui function to load a gui
    def load_gui(self):
        self.root=Tk(className="News_Application")
        self.root.geometry('600x550')
        self.root.resizable(0,0)
        self.root.config(background="black")


# function to clear is something on gui
    def clear_gui(self):
        for i in self.root.pack_slaves():
             i.destroy()

#make a function to get new on gui
    def news_load(self,index):
        self.clear_gui()


        try:
         img_url=self.data['articles'][index]['urlToImage']
         bt=urlopen(img_url).read()
         im=Image.open(io.BytesIO(bt))
         re_img=im.resize((600,300))
         img_2=ImageTk.PhotoImage(re_img)
         img_label=Label(self.root,image=img_2)
         img_label.pack()

        except:
         img_url='data:image/png;base64,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'
         bt=urlopen(img_url).read()
         im=Image.open(io.BytesIO(bt))
         re_img=im.resize((600,300))
         img_2=ImageTk.PhotoImage(re_img)
         img_label=Label(self.root,image=img_2)
         img_label.pack()

#title code

        heading=Label(self.root,text=self.data['articles'][index]['title'],background="black",fg="white",wraplength=550,justify="center")
        heading.pack(pady=(20,20))
        heading.config(font=('verdana',15))

#description code
        dta=Label(self.root,text=self.data['articles'][index]['description'],background="black",fg="white",wraplength=600,justify="center")
        dta.pack(pady=(10,10))
        dta.config(font=('verdana',12))

#frame to make buttos
        frame=Frame(self.root,bg="black")
        frame.pack(expand=True,fill=BOTH)
#buttons code
        if index!=0:
         pre=Button(frame,text="Previous",width=30,height=3,command=lambda:self.news_load(index-1))
         pre.pack(side=LEFT)

        read=Button(frame,text="Read More",width=27,height=3,command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)


        if index!=len(self.data['articles'])-1:
         next=Button(frame,text="Next",width=30,height=3,command=lambda:self.news_load(index+1))
         next.pack(side=LEFT)


        self.root.mainloop()

#red more detalies function
    def open_link(self,url):
        webbrowser.open(url)
        
obj=newsapp()
