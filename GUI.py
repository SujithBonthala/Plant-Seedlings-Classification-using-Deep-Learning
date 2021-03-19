from tkinter import *
import PIL as p
import tensorflow as tf
import numpy as np
root=Tk()
root.title("Image Classification using Deep Learning")
root.geometry("1360x1000")
Heading_text=Label(root,text="Plant Seedlings Classification using Deep Learning",font="arial 20 italic",fg="gold",bg="black").place(x=350,y=20)
line_1=Label(root,text='We classify plant seedlings by taking an image and displaying the top 3 predictions.',font='times 11').place(x=10,y=100)
line_2=Label(root,text='The 12 plant seedlings that we have chosen for our model is as follows :',font='times 11').place(x=10,y=125)
line_3=Label(root,text='1)    Black-grass',font='times 11').place(x=40,y=150)
line_4=Label(root,text='2)    Charlock',font='times 11').place(x=40,y=175)
line_5=Label(root,text='3)    Cleavers',font='times 11').place(x=40,y=200)
line_6=Label(root,text='4)    Common Chickweed',font='times 11').place(x=40,y=225)
line_7=Label(root,text='5)    Common Wheat',font='times 11').place(x=40,y=250)
line_8=Label(root,text='6)    Fat Hen',font='times 11').place(x=40,y=275)
line_9=Label(root,text='7)    Loose Silky-bent',font='times 11').place(x=40,y=300)
line_10=Label(root,text='8)    Maize',font='times 11').place(x=40,y=325)
line_11=Label(root,text='9)    Scentless Mayweed',font='times 11').place(x=40,y=350)
line_12=Label(root,text='10)  Shepherds Purse',font='times 11').place(x=40,y=375)
line_13=Label(root,text='11)  Small-flowered Cranesbill',font='times 11').place(x=40,y=400)
line_14=Label(root,text='12)  Sugar Beet',font='times 11').place(x=40,y=425)
enter_label=Label(root,text='Enter path of image here:',font='arial 15 bold').place(x=25,y=490)
enter_entry=Entry(root,width=50,bd=3,relief='sunken')
enter_entry.place(x=280,y=495)
def Classify():
    img_path=enter_entry.get()
    #img=ptk.PhotoImage(p.Image.open(img_path))    #Sample image to test - PlantSeedlings\plant-seedlings-final\test\00c47e980.png
    #img=tf.keras.preprocessing.image.load_img(img_path)
    model_import=tf.keras.models.load_model('Saved_Model_Backup')
classify_button=Button(root,text='Classify Image',bd=3,bg='cadet blue',fg='white',command=Classify).place(x=600,y=491)
root.mainloop()
