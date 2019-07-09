#Licensed under GPLv3.0
#built by 0x0J

from tkinter import *
from tkinter import filedialog as filedialog
from tkinter import messagebox as messb
from PIL import ImageTk, Image


# The Main class
class application:
    def __init__(self, master):
        self.master = master
        self.c_size = (800, 600)
        self.setup_ui(self.c_size)
        self.img = None

# GUI and title
    def setup_ui(self, s):
        Label(self.master, text='P  o  i  n  t  V  i  e  w', fg='white', pady=5, bg='grey',
              font=('Courier', 30)).pack()

        self.canvas = Canvas(self.master, height=s[1], width=s[0],
                             bg='black', bd=10, relief='sunken')

        self.canvas.pack()



        f = Frame(self.master, bg='grey', padx=10, pady=10)
        Button(f, text='Open image', bd=2, fg='white', bg='black', font=('Courier', 15)
               , command=self.make_img).pack(side=LEFT)
        f.pack()

        self.status = Label(self.master, text='No image loaded', bg='grey',
                            font=('Helvetica', 15), bd=2, fg='white', relief='sunken', anchor=W)

        self.status.pack(side=BOTTOM, fill=X)

#Function to display image using filedialog

    def make_img(self):
        try:
            File = filedialog.askopenfilename()
            self.pilImage = Image.open(File)
            resp = self.pilImage.resize((800, 600), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(resp)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0] / 2 + 10, self.c_size[1] / 2 + 10,
                                     anchor=CENTER, image=self.img)
            self.status['text'] = 'Current Image:' + File
        except:
            messb.showerror('File type is unsupported')


#Building window/object/icon/window title

root = Tk()
root.configure(bg='grey')
root.title('PointView')
icon = PhotoImage(file='pointview.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
application(root)
root.resizable(0, 0)
root.mainloop()