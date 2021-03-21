from tkinter import *
from PIL import Image
import tensorflow as tf
import numpy as np
import cv2
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
    img=cv2.imread(img_path)
    model_import=tf.keras.models.load_model('Saved_Model')
    img.resize((224,224,3))
    img=np.array(img).astype('float32')/255
    img=np.expand_dims(img,axis=0)
    prediction=model_import.predict(img)
    prediction_list=prediction[0].tolist()
    for i in range(len(prediction_list)):
        prediction_list[i]=float(prediction_list[i])*100
    names_list=['Black-grass','Charlock','Cleavers','Common Chickweed','Common Wheat','Fat Hen','Loose Silky-bent','Maize','Scentless Mayweed','Shepherds Purse','Small-flowered Cranesbill','Sugar Beet']
    join_list=zip(names_list,prediction_list)
    sorted_list=sorted(join_list,reverse=True,key=lambda x:x[1])
    str_1="1) "+sorted_list[0][0]+" - "+str(sorted_list[0][1])+"%"
    str_2="2) "+sorted_list[1][0]+" - "+str(sorted_list[1][1])+"%"
    str_3="3) "+sorted_list[2][0]+" - "+str(sorted_list[2][1])+"%"
    top_label=Label(root,text='The top 3 predictions are:',font='arial 12 bold').place(x=25,y=550)
    top1_label=Label(root,text=str_1,font='arial 12').place(x=40,y=580)
    top2_label=Label(root,text=str_2,font='arial 12').place(x=40,y=605)
    top3_label=Label(root,text=str_3,font='arial 12').place(x=40,y=630)
classify_button=Button(root,text='Classify Image',bd=3,bg='cadet blue',fg='white',command=Classify).place(x=600,y=491)
root.mainloop()
