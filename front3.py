import front4
import tkinter
from tkinter import *
import random
import os
import sys
from tkinter import messagebox

class statii:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1010x700+0+0")
        self.root.configure(bg="#7eea6b")
        self.root.title("فروشگاه لوازم تحریر")
        title = Label(self.root, text="تحریر لوازم انواع", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#7eea6b",fg="white").pack(fill=X)
        self.eraser = IntVar()
        self.pen = IntVar()
        self.pen2 = IntVar()
        self.pen3 = IntVar()
        self.pen4 = IntVar()
        self.pen5 = IntVar()
        self.pen6 = IntVar()
        self.pencil = IntVar()
        self.pencil2 = IntVar()
        self.pencil3 = IntVar()
        self.pencil4 = IntVar()
        self.pencil5 = IntVar()
        self.pencil6 = IntVar()
        self.eraser = IntVar()
        self.eraser2 = IntVar()
        self.notebook = IntVar()
        self.notebook2 = IntVar()
        self.glue = IntVar()
        self.glue2 = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()

        peens = LabelFrame(self.root, text="نویس زیبا", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        peens.place(x=30, y=80, height=125, width=250)

        peens2 = LabelFrame(self.root, text="فانتزی خودکار", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        peens2.place(x=280, y=80, height=125, width=250)

        peens3 = LabelFrame(self.root, text="ساده خودکار", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        peens3.place(x=530, y=80, height=125, width=250)



        item1 = Label(peens, text="نویس خود", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=0, column=0, pady=11)
        item1_entry = Entry(peens, borderwidth=2, width=15, textvariable=self.pen).grid(row=0, column=1, padx=10)

        item2 = Label(peens, text="نویس روان", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=1, column=0, pady=11)
        item2_entry = Entry(peens, borderwidth=2, width=15, textvariable=self.pen2).grid(row=1, column=1, padx=10)

        item3 = Label(peens2, text="عروسکی خودکار", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=2, column=0, pady=11)
        item3_entry = Entry(peens2, borderwidth=2, width=15, textvariable=self.pen3).grid(row=2, column=1, padx=10)

        item4 = Label(peens2, text="فیجتی خودکار", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=3, column=0, pady=11)
        item4_entry = Entry(peens2, borderwidth=2, width=15, textvariable=self.pen4).grid(row=3, column=1, padx=10)

        item5 = Label(peens3, text="آبی خودکار", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=4, column=0, pady=11)
        item5_entry = Entry(peens3, borderwidth=2, width=15, textvariable=self.pen5).grid(row=4, column=1, padx=10)

        item6 = Label(peens3, text="قرمز خودکار", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=5, column=0, pady=11)
        item6_entry = Entry(peens3, borderwidth=2, width=15, textvariable=self.pen6).grid(row=5, column=1, padx=10)

        penciil = LabelFrame(self.root, text="ساده مداد", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        penciil.place(x=30, y=230, height=125, width=250)

        penciil2 = LabelFrame(self.root, text="فانتزی مداد", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        penciil2.place(x=280, y=230, height=125, width=250)

        penciil3 = LabelFrame(self.root, text="طراحی مداد", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        penciil3.place(x=530, y=230, height=125, width=250)

        item1 = Label(penciil, text="سیاه مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry = Entry(penciil, borderwidth=2, width=15, textvariable=self.pencil).grid(row=0, column=1, padx=10)

        item2 = Label(penciil, text="قرمز مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry = Entry(penciil, borderwidth=2, width=15, textvariable=self.pencil2).grid(row=1, column=1, padx=10)

        item3 = Label(penciil2, text="چندرنگ مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry = Entry(penciil2, borderwidth=2, width=15, textvariable=self.pencil3).grid(row=2, column=1, padx=10)

        item4 = Label(penciil2, text="عروسکی مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry = Entry(penciil2, borderwidth=2, width=15, textvariable=self.pencil4).grid(row=3, column=1, padx=10)

        item5 = Label(penciil3, text="رنگی مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry = Entry(penciil3, borderwidth=2, width=15, textvariable=self.pencil5).grid(row=4, column=1, padx=10)

        item6 = Label(penciil3, text="نرم مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry = Entry(penciil3, borderwidth=2, width=15, textvariable=self.pencil6).grid(row=5, column=1, padx=10)


        eraseer = LabelFrame(self.root, text="کن پاک", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        eraseer.place(x=30, y=380, height=125, width=250)

        notebookk = LabelFrame(self.root, text="دفترچه", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        notebookk.place(x=280, y=380, height=125, width=250)

        gluee = LabelFrame(self.root, text="چسب", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        gluee.place(x=530, y=380, height=125, width=250)

        item1 = Label(eraseer, text="بزرگ کن پاک", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry = Entry(eraseer, borderwidth=2, width=15, textvariable=self.eraser).grid(row=0, column=1, padx=10)

        item2 = Label(eraseer, text="خمیری کن پاک", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry = Entry(eraseer, borderwidth=2, width=15, textvariable=self.eraser2).grid(row=1, column=1, padx=10)

        item3 = Label(notebookk, text="سیمی دفترچه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry = Entry(notebookk, borderwidth=2, width=15, textvariable=self.notebook).grid(row=2, column=1, padx=10)

        item4 = Label(notebookk, text="ساده دفترچه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry = Entry(notebookk, borderwidth=2, width=15, textvariable=self.notebook2).grid(row=3, column=1, padx=10)

        item5 = Label(gluee, text="نواری چسب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry = Entry(gluee, borderwidth=2, width=15, textvariable=self.glue).grid(row=4, column=1, padx=10)

        item6 = Label(gluee, text="ماتیکی چسب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry = Entry(gluee, borderwidth=2, width=15, textvariable=self.glue2).grid(row=5, column=1, padx=10)

        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#eae202")
        billarea.place(x=12, y=510, width=500, height=180)

        bill_title = Label(billarea, text="حساب صورت", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#eae202",fg="#6C3483").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # billing_menu = LabelFrame(self.root, text="", font=("Arial Black", 12), relief=GROOVE, bd=10,bg="#eae202", fg="white")
        # billing_menu.place(x=520, y=555, relwidth=1, height=120)

        button_frame2 = Frame(self.root, bd=0, relief=GROOVE, bg="#868602")
        button_frame2.place(x=20, y=15)

        button_frame = Frame(self.root, bd=7, relief=GROOVE, bg="#868602")
        button_frame.place(x=520,y=590, width=555, height=95)


        button_stati = Button(button_frame2,text="قبلی صفحه", font=("Arial Black", 10), bg="#fdfd3f",fg="#6C3483", command=lambda: self.statti()).grid(row=0, column=0, padx=0)
        button_total = Button(button_frame, text="حساب صورت کل", font=("Arial Black", 15), pady=10, bg="#fdfd3f",fg="#6C3483", command=lambda: self.total()).grid(row=0, column=1, padx=10)
        button_clear = Button(button_frame, text="خرید سبد کردن پاک", font=("Arial Black", 15), pady=10, bg="#fdfd3f",fg="#6C3483", command=lambda: self.clear()).grid(row=0, column=2, padx=8, pady=6)
        button_exit = Button(button_frame, text="خروج", font=("Arial Black", 15), pady=10, bg="#fdfd3f", fg="#6C3483",width=8, command=lambda: self.exit11()).grid(row=0, column=3, padx=10, pady=6)
        self.intro()

    def total(self):
        self.hr = self.pen.get() * 120
        self.hr2 = self.pen2.get() * 40
        self.hr3 = self.pen3.get() * 10
        self.mt = self.pen4.get() * 20
        self.hf = self.pen5.get() * 30
        self.gt = self.pen6.get() * 60
        total_books_price =(
                self.hr +
                self.hr2 +
                self.hr3 +
                self.mt +
                self.hf +
                self.gt)
        self.total_sna.set(str(total_books_price) + " Toman")
        self.a.set(str(round(total_books_price * 0.05, 3)) + "Toman")

        self.hs = self.pencil.get() * 42
        self.hs2 = self.pencil2.get() * 120
        self.bz = self.pencil3.get() * 113
        self.ar = self.pencil4.get() * 160
        self.gi = self.pencil5.get() * 55
        self.by = self.pencil6.get() * 480
        total_story_price =(
                self.hs +
                self.hs2 +
                self.bz +
                self.ar +
                self.gi +
                self.by)

        self.total_gro.set(str(total_story_price) + " Toman")
        self.b.set(str(round(total_story_price * 0.01, 3)) + " Toman")

        self.pe = self.eraser.get() * 30
        self.pi = self.eraser2.get() * 180
        self.er = self.notebook.get() * 130
        self.nb = self.notebook2.get() * 500
        self.gl = self.glue.get() * 85
        self.la = self.glue2.get() * 100

        total_stati_price =(
                self.pe +
                self.pi +
                self.er +
                self.nb +
                self.gl +
                self.la)
        self.total_hyg.set(str(total_stati_price) + " Toman")
        self.c.set(str(round(total_stati_price * 0.10, 3)) + "Toman")
        self.total_all_bill = (total_books_price +
                               total_story_price +
                               total_stati_price +
                               (round(total_story_price * 0.01, 3)) +
                               (round(total_stati_price * 0.10, 3)) +
                               (round(total_books_price * 0.05, 3)))
        self.total_all_bil = str(self.total_all_bill) + " Rs"
        self.billarea()

    def intro(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\t     خوش امدید به فروشگاه کتاب\n\t    ارتباط با ما : 442232129")
        self.txtarea.insert(END, "\n======================================================\n")
        self.txtarea.insert(END, "\n  محصول  \t\t تعداد \t قیمت \n")
        self.txtarea.insert(END, "\n=======================================================\n")

    def billarea(self):
        self.intro()
        if self.pen.get() != 0:
            self.txtarea.insert(END, f"خود نویس\t\t {self.pen.get()}\t{self.hr}\n")
        if self.pen2.get() != 0:
            self.txtarea.insert(END, f"روان نویس\t\t {self.pen2.get()}\t{self.hr2}\n")
        if self.pen3.get() != 0:
            self.txtarea.insert(END, f"خودکار عروسکی\t\t {self.pen3.get()}\t{self.hr3}\n")
        if self.pen4.get() != 0:
            self.txtarea.insert(END, f"خودکار فیجتی\t\t {self.pen4.get()}\t{self.mt}\n")
        if self.pen5.get() != 0:
            self.txtarea.insert(END, f"خودکار آبی\t\t {self.pen5.get()}\t{self.hf}\n")
        if self.pen6.get() != 0:
            self.txtarea.insert(END, f"خودکار قرمز\t\t {self.pen6.get()}\t{self.gt}\n")
        if self.pencil.get() != 0:
            self.txtarea.insert(END, f" مداد سیاه\t\t {self.pencil.get()}\t{self.hs}\n")
        if self.pencil2.get() != 0:
            self.txtarea.insert(END, f"مداد قرمز\t\t {self.pencil2.get()}\t{self.hs2}\n")
        if self.pencil3.get() != 0:
            self.txtarea.insert(END, f"مداد چند رنگ\t\t {self.pencil3.get()}\t{self.bz}\n")
        if self.pencil4.get() != 0:
            self.txtarea.insert(END, f"مداد عروسکی\t\t {self.pencil4.get()}\t{self.ar}\n")
        if self.pencil5.get() != 0:
            self.txtarea.insert(END, f"مداد رنگی\t\t {self.pencil5.get()}\t{self.gi}\n")
        if self.pencil6.get() != 0:
            self.txtarea.insert(END, f"مداد نرم\t\t {self.pencil6.get()}\t{self.by}\n")
        if self.eraser.get() != 0:
            self.txtarea.insert(END, f"پاک کن بزرگ\t\t {self.eraser.get()}\t{self.pe}\n")
        if self.eraser2.get() != 0:
            self.txtarea.insert(END, f"پاک کن خمیری\t\t {self.eraser2.get()}\t{self.pi}\n")
        if self.notebook.get() != 0:
            self.txtarea.insert(END, f"دفترچه سیمی\t\t {self.notebook.get()}\t{self.er}\n")
        if self.notebook2.get() != 0:
            self.txtarea.insert(END, f"دفترچه ساده\t\t {self.notebook2.get()}\t{self.nb}\n")
        if self.glue.get() != 0:
            self.txtarea.insert(END, f"چسب نواری\t\t {self.glue.get()}\t{self.gl}\n")
        if self.glue2.get() != 0:
            self.txtarea.insert(END, f"چسب ماتیکی\t\t {self.glue2.get()}\t{self.la}\n")

    def clear(self):
        self.txtarea.delete(1.0, END)
        self.pen.set(0)
        self.pen2.set(0)
        self.pen3.set(0)
        self.pen4.set(0)
        self.pen5.set(0)
        self.pen6.set(0)
        self.pencil.set(0)
        self.pencil2.set(0)
        self.pencil3.set(0)
        self.pencil4.set(0)
        self.pencil5.set(0)
        self.pencil6.set(0)
        self.eraser.set(0)
        self.eraser2.set(0)
        self.notebook.set(0)
        self.notebook2.set(0)
        self.glue.set(0)
        self.glue2.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)


    def statti(self):
        self.root.destroy()
        second = tkinter.Tk()
        example = front4.Book(second)


    def exit11(self):
        self.root.destroy()




if __name__ =='__main__':
    window = tkinter.Tk()
    app = statii(root=window)
    window.mainloop()