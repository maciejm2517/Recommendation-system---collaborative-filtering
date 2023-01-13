from tkinter import *
from tkinter import messagebox
import recomender

class Gui():
    def __init__(self,toppings):
        self.root = Tk()
        self.root.title('gui app')
        self.root.geometry("500x700")
        # self.my_label=Label(self.root,text='start typing',font=('Helvetica',14),fg='grey')
        # self.my_label.grid(row=1,column=1,padx=0,pady=10)

        self.default_text = StringVar(self.root, value='search or double click')
        
        self.my_entry=Entry(self.root,font=('Helvetica',14),textvariable=self.default_text)
        self.my_entry.grid(row=1,column=1,padx=(10,10),pady=(10,10))

        self.my_list=Listbox(self.root,width=26)
        self.my_list.grid(row=2,column=1,padx=0,pady=(10,10))

        self.button_like=Button(self.root,text="Like",command=self.like_interaction)
        self.button_like.grid(row=1,column=5,padx=(10,10),pady=(10,10))

        self.button_buy=Button(self.root,text="Buy",command=self.buy_interaction)
        self.button_buy.grid(row=2,column=5,padx=(10,10),pady=(10,10))

        self.label_recommendation=Label(self.root,text='Recommendation',font=('Helvetica',14),fg='grey')
        self.label_recommendation.grid(row=3,column=1,padx=0,pady=10)

        self.list_recommendation=Listbox(self.root,width=26)
        self.list_recommendation.grid(row=4,column=1,padx=0,pady=(10,10))

        self.button_clear=Button(self.root,text="Clear prererences",command=self.clear_preferences)
        self.button_clear.grid(row=3,column=5,padx=(10,10),pady=(10,10))

        self.toppings=toppings

        self.names=recomender.get_names()
        self.user={name:0 for name in self.names}

        self.start=True

        self.loop()
        pass

    def clear_preferences(self):
        self.user={name:0 for name in self.names}
        self.list_recommendation.delete(0,END)
        self.start=True


    def update(self,data):
        self.my_list.delete(0,END) 

        for item in data:
            self.my_list.insert(END,item)

    def update_recommendations(self,data):
        self.list_recommendation.delete(0,END) 

        for item in data:
            self.list_recommendation.insert(END,item)        

    def fillout(self,e):
        if self.start:
            self.start=False
            return
        input=self.my_list.get(ACTIVE)
        self.my_entry.delete(0,END)
        self.my_entry.insert(0,input)
        #TODO
        if self.user[input]<3:
            self.user[input]=3
        self.interaction_recomendation()

        # SEARCHED

    def buy_interaction(self):
        input=self.my_list.get(ACTIVE)
        #TODO
        if self.user[input]<5:
            self.user[input]=5
        self.interaction_recomendation()

    def like_interaction(self):
        input=self.my_list.get(ACTIVE)
        #TODO
        if self.user[input]<4:
            self.user[input]=4
        self.interaction_recomendation()


    def check(self,e):
        typed=self.my_entry.get()
        if typed=="":
            data=self.toppings
        else:
            data=[]
            for item in self.toppings:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)

    def interaction_recomendation(self):
        interactions_dict=dict()
        for key in self.user:
            if self.user[key]>0:
                interactions_dict[key]=self.user[key]

        # print(interactions_dict)
        
        self.recomendation=recomender.prediction(interactions_dict)
        interaction_list=[key for key in self.recomendation]
        
        # print(interaction_list[:5])
        # print(interaction_list)
        self.update_recommendations(interaction_list)

    def loop(self):
        self.update(self.toppings)

        self.my_list.bind("<<ListboxSelect>>",self.fillout)

        self.my_entry.bind("<KeyRelease>",self.check)
        self.root.mainloop()