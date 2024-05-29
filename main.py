



import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="grey")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Heart Disease Prediction and Prevenion System  ")

# 

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('reg3.png')
image2 = image2.resize((2000, 1000), Image.ANTIALIAS)

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

def log():
    from subprocess import call
    call(["python","login.py"])

def reg():
    from subprocess import call
    call(["python","registration.py"])


  
def window():
  root.destroy()

        

button1 = tk.Button(root, text="Sign In ", command=log, width=15, height=1,font=('times', 20, ' bold '), bg="Blue", fg="white")
button1.place(x=50, y=300)

button2 = tk.Button(root, text="Sign Up", command=reg, width=15, height=1,font=('times', 20, ' bold '), bg="Blue", fg="white")
button2.place(x=330, y=300)



button4 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 20, ' bold '), bg="Red", fg="white")
button4.place(x=170, y=400)

root.mainloop()
