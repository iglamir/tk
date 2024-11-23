import tkinter
from tkinter import *
import random
import os
import sys
from tkinter import messagebox
import front3

class Book:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1010x700+0+0")
        self.root.configure(bg="#7eea6b")
        self.root.title("Book Store")
        title=Label(self.root,text="کتاب فروشگاه",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#7eea6b",fg="white").pack(fill=X)
        self.HaryPater=IntVar()
        self.Got=IntVar()
        self.HaryPater2=IntVar()
        self.HaryPater3=IntVar()
        self.Hafez=IntVar()
        self.math=IntVar()
        self.it=IntVar()
        self.hasani=IntVar()
        self.hasani2=IntVar()
        self.baby=IntVar()
        self.angor=IntVar()
        self.ghermzi=IntVar()
        self.boz=IntVar()
        self.eraser=IntVar()
        self.pen=IntVar()
        self.pencil=IntVar()
        self.notebook=IntVar()
        self.llable=IntVar()
        self.glue=IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        self.phone=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))


        details = LabelFrame(self.root, text="کاربر مشخصات", font=("Arial Black", 12), bg="#eae202", fg="white",relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="نام کاربر", font=("Arial Black", 14), bg="#eae202", fg="white").grid(row=0,column=0,padx=15)
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)
        contact_name = Label(details, text="همراه شماره", font=("Arial Black", 14), bg="#eae202", fg="white").grid(row=0, column=2, padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)
        bill_name = Label(details, text="کاربری شماره", font=("Arial Black", 14), bg="#eae202", fg="white").grid(row=0,column=4,padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)



        books = LabelFrame(self.root, text="ها کتاب", font=("Arial Black", 12), bg="#eae202", fg="#6C3483",relief=GROOVE, bd=10)
        books.place(x=677, y=180, height=380, width=325)

        item1 = Label(books, text="پاتر هری کتاب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=0, column=0, pady=11)
        item1_entry = Entry(books, borderwidth=2, width=15, textvariable=self.HaryPater).grid(row=0, column=1, padx=10)

        item2 = Label(books, text="پاتر هری دوم نسخه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry = Entry(books, borderwidth=2, width=15, textvariable=self.HaryPater2).grid(row=1, column=1, padx=10)

        item3 = Label(books, text="پاتر هری سوم نسخه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry = Entry(books, borderwidth=2, width=15, textvariable=self.HaryPater3).grid(row=2, column=1, padx=10)

        item4 = Label(books, text="مهندسی کتاب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry = Entry(books, borderwidth=2, width=15, textvariable=self.math).grid(row=3, column=1, padx=10)

        item5 = Label(books, text="حافظ دیوان", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry = Entry(books, borderwidth=2, width=15, textvariable=self.Hafez).grid(row=4, column=1, padx=10)

        item6 = Label(books, text="گات کتاب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=5, column=0, pady=11)
        item6_entry = Entry(books, borderwidth=2, width=15, textvariable=self.Got).grid(row=5, column=1, padx=10)

        story = LabelFrame(self.root, text="داستان کتاب", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#eae202",fg="#6C3483")
        story.place(x=340, y=180, height=380, width=325)

        item8 = Label(story, text="حسنی قصه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=0, column=0, pady=11)
        item8_entry = Entry(story, borderwidth=2, width=15, textvariable=self.hasani).grid(row=0, column=1, padx=10)

        item9 = Label(story, text="دروغگو چوپان قصه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry = Entry(story, borderwidth=2, width=15, textvariable=self.hasani2).grid(row=1, column=1, padx=10)

        item10 = Label(story, text="منگول شنگول", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=2, column=0, pady=11)
        item10_entry = Entry(story, borderwidth=2, width=15, textvariable=self.angor).grid(row=2, column=1, padx=10)

        item11 = Label(story, text="قرمزی شنل", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=3, column=0, pady=11)
        item11_entry = Entry(story, borderwidth=2, width=15, textvariable=self.ghermzi).grid(row=3, column=1, padx=10)

        item12 = Label(story, text="قندی بز بز", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=4, column=0, pady=11)
        item12_entry = Entry(story, borderwidth=2, width=15, textvariable=self.boz).grid(row=4, column=1, padx=10)

        item13 = Label(story, text="زن قلقله کدو", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry = Entry(story, borderwidth=2, width=15, textvariable=self.baby).grid(row=5, column=1, padx=10)

        # stati = LabelFrame(self.root, text="تحریر لوازم", font=("Arial Black", 12), relief=GROOVE, bd=10,bg="#eae202", fg="#6C3483")
        # stati.place(x=677, y=180, height=380, width=325)
        #
        # item15 = Label(stati, text="نویس روان", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=0,column=0,pady=11)
        # item15_entry = Entry(stati, borderwidth=2, width=15, textvariable=self.pencil).grid(row=0, column=1, padx=10)
        #
        # item16 = Label(stati, text="عروسکی مداد", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=1,column=0,pady=11)
        # item16_entry = Entry(stati, borderwidth=2, width=15, textvariable=self.pencil).grid(row=1, column=1, padx=10)
        #
        # item17 = Label(stati, text="خمیری پاک کن", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=2, column=0, pady=11)
        # item17_entry = Entry(stati, borderwidth=2, width=15, textvariable=self.eraser).grid(row=2, column=1, padx=10)
        #
        # item18 = Label(stati, text="بزرگ دفترچه", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=3,column=0,pady=11)
        # item18_entry = Entry(stati, borderwidth=2, width=15, textvariable=self.notebook).grid(row=3, column=1, padx=10)
        #
        # item19 = Label(stati, text="ماتیکی چسب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=4,column=0,pady=11)
        # item19_entry = Entry(stati, borderwidth=2, width=15, textvariable=self.glue).grid(row=4, column=1, padx=10)
        #
        # item20 = Label(stati, text="اسمی برچسب", font=("Arial Black", 11), bg="#eae202", fg="#6C3483").grid(row=5, column=0, pady=11)
        # item20_entry = Entry(stati, borderwidth=2, width=15, textvariable=self.llable).grid(row=5, column=1, padx=10)

        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#eae202")
        billarea.place(x=5, y=180, width=325, height=380)

        bill_title = Label(billarea, text="حساب صورت", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#eae202",fg="#6C3483").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        billing_menu = LabelFrame(self.root, text="حساب صورت خلاصه", font=("Arial Black", 12), relief=GROOVE, bd=10,bg="#eae202", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_books = Label(billing_menu, text="ها کتاب کل قیمت", font=("Arial Black", 11), bg="#eae202",fg="white").grid(row=0, column=0)
        total_books_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_story = Label(billing_menu, text="ها داستان کل قیمت", font=("Arial Black", 11), bg="#eae202",fg="white").grid(row=1, column=0)
        total_story_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)

        total_stati = Label(billing_menu, text="تحریر لوازم کل قیمت", font=("Arial Black", 11), bg="#eae202",fg="white").grid(row=2, column=0)
        total_stati_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#868602")
        button_frame.place(x=350, width=620, height=95)

        button_stati = Button(button_frame, text="تحریر لوازم", font=("Arial Black", 15), pady=10, bg="#fdfd3f",fg="#6C3483", command=lambda: self.stati()).grid(row=0, column=0, padx=12)
        button_total = Button(button_frame, text="حساب صورت کل", font=("Arial Black", 15), pady=10, bg="#fdfd3f",fg="#6C3483", command=lambda: self.total()).grid(row=0, column=1, padx=10)
        button_clear = Button(button_frame, text="خرید سبد کردن پاک", font=("Arial Black", 15), pady=10, bg="#fdfd3f",fg="#6C3483", command=lambda: self.clear()).grid(row=0, column=2, padx=8, pady=6)
        button_exit = Button(button_frame, text="خروج", font=("Arial Black", 15), pady=10, bg="#fdfd3f", fg="#6C3483",width=8, command=lambda: self.exit1()).grid(row=0, column=3, padx=10, pady=6)
        self.intro()

    def total(self):
        if (self.c_name.get == "" or self.phone.get() == ""):
            messagebox.showerror("Error", "فیلد هارا پر کنید")
        self.hr = self.HaryPater.get() * 120
        self.hr2 = self.HaryPater2.get() * 40
        self.hr3 = self.HaryPater3.get() * 10
        self.mt = self.math.get() * 20
        self.hf = self.Hafez.get() * 30
        self.gt = self.Got.get() * 60
        total_books_price = (
                self.hr +
                self.hr2 +
                self.hr3 +
                self.mt +
                self.hf +
                self.gt )
        self.total_sna.set(str(total_books_price) + " Toman")
        self.a.set(str(round(total_books_price * 0.05, 3)) + "Toman")

        self.hs = self.hasani.get() * 42
        self.hs2= self.hasani2.get() * 120
        self.bz = self.boz.get() * 113
        self.ar = self.angor.get() * 160
        self.gi = self.ghermzi.get() * 55
        self.by = self.baby.get() * 480
        total_story_price = (
                self.hs +
                self.hs2 +
                self.bz +
                self.ar +
                self.gi +
                self.by )

        self.total_gro.set(str(total_story_price) + " Toman")
        self.b.set(str(round(total_story_price * 0.01, 3)) + " Toman")

        self.pe = self.pen.get() * 30
        self.pi = self.pencil.get() * 180
        self.er = self.eraser.get() * 130
        self.nb = self.notebook.get() * 500
        self.gl = self.glue.get() * 85
        self.la = self.llable.get() * 100

        total_stati_price = (
                self.pe +
                self.pi +
                self.er +
                self.nb +
                self.gl +
                self.la )

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
        self.txtarea.insert(END, "\tخوش امدید به فروشگاه کتاب\n\tارتباط با ما : 442232129")
        self.txtarea.insert(END, f"\n\nشماره کاربری : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nنام کاربر : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nشماره تلفن همراه : {self.phone.get()}")
        self.txtarea.insert(END, "\n===================================\n")
        self.txtarea.insert(END, "\nمحصول\t\tتعداد\tقیمت\n")
        self.txtarea.insert(END, "\n===================================\n")

    def billarea(self):
        self.intro()
        if self.HaryPater.get() != 0:
            self.txtarea.insert(END, f"هری پاتر\t\t {self.HaryPater.get()}\t{self.hr}\n")
        if self.HaryPater2.get() != 0:
            self.txtarea.insert(END, f"هری پاتر2\t\t {self.HaryPater2.get()}\t{self.hr2}\n")
        if self.HaryPater3.get() != 0:
            self.txtarea.insert(END, f"کتاب مهندسی\t\t {self.math.get()}\t{self.mt}\n")
        if self.Hafez.get() != 0:
            self.txtarea.insert(END, f"دیوان حافظ\t\t {self.Hafez.get()}\t{self.hf}\n")
        if self.Got.get() != 0:
            self.txtarea.insert(END, f"گات\t\t {self.Got.get()}\t{self.gt}\n")
        if self.hasani.get() != 0:
            self.txtarea.insert(END, f"حسنی\t\t {self.hasani.get()}\t{self.hs}\n")
        if self.hasani2.get() != 0:
            self.txtarea.insert(END, f" چوپان دروغگو\t\t {self.hasani2.get()}\t{self.hs2}\n")
        if self.angor.get() != 0:
            self.txtarea.insert(END, f"شنگول منگول\t\t {self.angor.get()}\t{self.ar}\n")
        if self.boz.get() != 0:
            self.txtarea.insert(END, f"بز بز قندی\t\t {self.boz.get()}\t{self.bz}\n")
        if self.baby.get() != 0:
            self.txtarea.insert(END, f"کدو قلقله زن\t\t {self.baby.get()}\t{self.by}\n")
        if self.ghermzi.get() != 0:
            self.txtarea.insert(END, f"شنل قرمزی\t\t {self.ghermzi.get()}\t{self.gi}\n")
        if self.pen.get() != 0:
            self.txtarea.insert(END, f"روان نویس\t\t {self.pen.get()}\t{self.pe}\n")
        if self.eraser.get() != 0:
            self.txtarea.insert(END, f"مداد عروسکی\t\t {self.eraser.get()}\t{self.er}\n")
        if self.pencil.get() != 0:
            self.txtarea.insert(END, f"پاک کن بزرگ\t\t {self.pencil.get()}\t{self.pi}\n")
        if self.glue.get() != 0:
            self.txtarea.insert(END, f"چسب\t\t {self.glue.get()}\t{self.gl}\n")
        if self.notebook.get() != 0:
            self.txtarea.insert(END, f"دفترچه\t\t {self.notebook.get()}\t{self.nb}\n")
        if self.llable.get() != 0:
            self.txtarea.insert(END, f"برچسب\t\t {self.llable.get()}\t{self.la}\n")

    def clear(self):
        self.txtarea.delete(1.0, END)
        self.HaryPater.set(0)
        self.HaryPater2.set(0)
        self.HaryPater3.set(0)
        self.pen.set(0)
        self.pencil.set(0)
        self.eraser.set(0)
        self.notebook.set(0)
        self.llable.set(0)
        self.glue.set(0)
        self.Hafez.set(0)
        self.ghermzi.set(0)
        self.hasani.set(0)
        self.hasani2.set(0)
        self.boz.set(0)
        self.angor.set(0)
        self.baby.set(0)
        self.math.set(0)
        self.Got.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)

    def stati(self):
        self.root.destroy()
        second = tkinter.Tk()
        example = front3.statii(second)


    def exit1(self):
        self.root.destroy()



if __name__ =='__main__':
    window = tkinter.Tk()
    app = Book(root=window)
    window.mainloop()