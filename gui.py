import main
import tkinter as tk


def vp_start_gui():
    global root
    root = tk.Tk()
    TopLevel(root)
    root.mainloop()


class TopLevel:

    def on_button_click(self):
        main.calculate(self.MiddlestNum.get(), self.NumofDice.get())

    def __init__(self, top):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("306x385+650+150")
        top.minsize(120, 1)
        top.maxsize(3604, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.261, rely=0.597, height=24, width=137)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Calulate outcome''')
        self.Button1.configure(command=self.on_button_click)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.033, rely=0.13, height=18, width=159)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Number of dice you will roll''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.065, rely=0.208, height=18, width=98)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Highest number''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.065, rely=0.286, height=18, width=98)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Middlest number''')

        self.MiddlestNum = tk.Entry(top)
        self.MiddlestNum.place(relx=0.784, rely=0.286, height=20, relwidth=0.111)
        self.MiddlestNum.configure(background="white")
        self.MiddlestNum.configure(disabledforeground="#a3a3a3")
        self.MiddlestNum.configure(font="TkFixedFont")
        self.MiddlestNum.configure(foreground="#000000")
        self.MiddlestNum.configure(insertbackground="black")

        self.NumofDice = tk.Entry(top)
        self.NumofDice.place(relx=0.784, rely=0.13, height=20, relwidth=0.111)
        self.NumofDice.configure(background="white")
        self.NumofDice.configure(disabledforeground="#a3a3a3")
        self.NumofDice.configure(font="TkFixedFont")
        self.NumofDice.configure(foreground="#000000")
        self.NumofDice.configure(highlightbackground="#d9d9d9")
        self.NumofDice.configure(highlightcolor="black")
        self.NumofDice.configure(insertbackground="black")
        self.NumofDice.configure(selectbackground="blue")
        self.NumofDice.configure(selectforeground="white")

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(relx=0.784, rely=0.364, height=20, relwidth=0.111)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.Label3_3 = tk.Label(top)
        self.Label3_3.place(relx=0.033, rely=0.364, height=18, width=98)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(cursor="fleur")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Lowest number''')

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(relx=0.784, rely=0.208, height=20, relwidth=0.111)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.065, rely=0.753, height=21, width=99)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(cursor="fleur")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Your troops killed''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.523, rely=0.753, height=21, width=110)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(cursor="fleur")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Enemy troops killed''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.196, rely=0.805, height=21, width=34)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(cursor="fleur")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''0''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.621, rely=0.805, height=21, width=34)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''0''')


vp_start_gui()
