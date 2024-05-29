


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="grey")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Heart Disease Prediction and Prevention System  ")

# 

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('a1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
# label_l1 = tk.Label(root, text="Railway Track Fault Detection",font=("Times New Roman", 30, 'bold'),
#                     background="#9932CC", fg="white", width=75, height=1)
# label_l1.place(x=0, y=10)

# frame_alpr = tk.LabelFrame(root, text=" --Display-- ", width=400, height=400, bd=5, font=('times', 15, ' bold '),bg="#CD00CD")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=100, y=250)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# image2 = Image.open('log1.jpg')
# image2 = image2.resize((500, 300), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=10, y=120) 
# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])



def reg():
    from subprocess import call
    call(["python","GUI_Master_old.py"])


  
def window():
  root.destroy()

        



button2 = tk.Button(root, text="Heart Disease Detection", command=reg, width=18, height=1,font=('times', 18, ' bold '), bg="black", fg="white")
button2.place(x=150, y=100)



button4 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 20, ' bold '), bg="Red", fg="white")
button4.place(x=150, y=200)

root.mainloop()
