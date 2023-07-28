import tkinter
from tkinter import *
from tkinter import filedialog
import tiktok_bot
import tiktoklogin

root = Tk()
root.title('Tiktok Bot')
root.iconphoto(False, tkinter.PhotoImage(file='robot.png'))
root.geometry("500x200")
root.resizable(width =False, height=False)




''''
def selectprofile():
    global selected_profile_folder
    selected_profile_folder = filedialog.askdirectory()
    print(selected_profile_folder)

    # reset the button text back to Browse
    selectprofile_text.set("Selected")
'''

def createprofile():
    global selected_new_profile_folder
    selected_new_profile_folder = filedialog.askdirectory()
    print(selected_new_profile_folder)
    tiktoklogin.func(selected_new_profile_folder)

def run():
    video = video_link.get()
    c1_status = var1.get()
    c2_status = var2.get()
    c3_status = var3.get()
    tiktok_bot.func(video,c1_status,c2_status,c3_status)



''''
selectprofile_text = StringVar()
selectprofile_btn = Button(root, textvariable=selectprofile_text, command=lambda:selectprofile(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
selectprofile_text.set("Select a profile")
selectprofile_btn.grid(column=0, row=2, sticky=NE, padx=10)
'''


createprofile_text = StringVar()
createprofile_btn = Button(root, textvariable=createprofile_text, command=lambda:createprofile(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
createprofile_text.set("Create new profile")
createprofile_btn.grid(column=0, row=0,rowspan=2, sticky=NE, padx=5)

lable1 = Label(root, text= 'video link')
lable1.grid(column = 0, row=3)

video_link = Entry(root, width=50)
video_link.grid(column=1, row=3,rowspan=4, sticky=NE, padx=10)

var1 = IntVar()
c1 = Checkbutton(root,text= 'like',variable = var1).place(x=200,y=60)
#c1.grid(column=0, row=4,columnspan=2, sticky=NE, padx=10)

var2 = IntVar()
c2 = Checkbutton(root,text= 'comment',variable = var2).place(x=200,y =80)
#c2.grid(column=0, row=9,columnspan=2, sticky=NE, padx=10)
var3 = IntVar()
c3 = Checkbutton(root,text= 'follow',variable = var3).place(x=200, y=100)
#c3.grid(column=0, row=10, columnspan=2,sticky=NE, padx=10)

run_text = StringVar()
run_btn = Button(root, textvariable=run_text, command=lambda:run(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15).place(x =200,y=130)
run_text.set("Run")



root.mainloop()

