import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import pymysql
from functools import partial
from pandastable import Table, TableModel
import time
from datetime import datetime
from fpdf import FPDF
from tkinter.messagebox import showerror
import tkinter.messagebox


class Welcome():
    def __init__(self,master, root, cur, con):
        self.root = root
        self.cur = cur
        self.con = con
        self.master = master
        self.master.geometry('500x150+100+200')
        self.master.title('Информационная система для обслуживания клиентов видеокассетами')
        self.label1=Label(self.master,text='Главное меню',fg='blue').grid(row=0,column=1)
        self.button2=Button(self.master,text="Показать все таблицы в базе данных",fg='blue',command=self.gotorecords).grid(row=2,column=1)
        self.button3=Button(self.master,text="Выход",fg='red',command=self.exit).grid(row=4,column=1)
        self.button4=Button(self.master,text="Справки",fg='blue',command=self.gotoreport).grid(row=3,column=1)

    def exit(self):
        self.master.destroy()
        self.root.destroy()

    def gotodataentry(self):    
        root2=Toplevel(self.master)
        myGUI=DataEntry(root2)

    def gotorecords(self):
        root2=Toplevel(self.master)
        mygui=Records(root2, self.cur,self.con)
        
    def gotoreport(self):
        root3=Toplevel(self.master)
        mygui2=Report(root3, self.cur)        

class Records:
    def __init__(self, master, cur, con):
        self.cur = cur
        self.con = con
        self.master = master
        self.master.geometry('700x150+100+200')
        self.master.title('Таблицы в базе данных')
        self.textLabel = Label(self.master, text="№ таблицы", width=10)
        self.textLabel.grid(row=0, column=0)
        self.intLabel = Label(self.master, text="Имена таблиц:", width=15)
        self.intLabel.grid(row=0, column=1)
        self.showallrecords()

    def showallrecords(self):
        Data = self.readfromdatabase()
        for index, dat in enumerate(Data):
            Label(self.master, text=index+1).grid(row=index+1, column=0)
            Label(self.master, text=dat[0]).grid(row=index+1, column=1)
            print(dat[0])
            ttk.Button(self.master, text="Показать таблицу", command=partial(self.show_table,dat[0])).grid(row=index+1,column=2)
            ttk.Button(self.master, text="Добавить данные", command=partial(self.insert_row,dat[0])).grid(row=index+1,column=3)
            ttk.Button(self.master, text="Удалить данные", command=partial(self.delete_row,dat[0])).grid(row=index+1,column=4)
            ttk.Button(self.master, text="Обновить данные", command=partial(self.update_row,dat[0])).grid(row=index+1,column=5)

    def readfromdatabase(self):
        self.cur.execute("show full tables where table_type= 'BASE TABLE';")
        return self.cur.fetchall()

    # показать содержание таблиц
    def show_table(self,dat):
        root8=tk.Toplevel()
        root8.title(dat)
        
        if dat == 'данные о выдачах':
            zaprosy="SELECT `Название фильма`, `ФИО клиента`,`Адрес клиента`,`Дата выдачи`,`Дата возвращения`,`Залог`,`Оплата` FROM `данные о выдачах`, `сведения о фильме` where `данные о выдачах`.`Номер фильма` = `сведения о фильме`.`Номер фильма`;"      

        if dat == 'компания производитель':
            zaprosy="SELECT `Название компании`,`Страна`,`Город`,`Год основания` FROM `компания производитель`;"

        if dat == 'сведения о фильме':
            zaprosy="SELECT `Название фильма`,`Название компании`,`Год выпуска`,`Основные исполнители`,`Характер фильма` FROM videokassety2.`сведения о фильме`, videokassety2.`компания производитель` where `сведения о фильме`.`ID Компании` = `компания производитель`.`ID Компании`;"      

        
        # zaprosy = "SELECT * FROM videokassety2.`" + dat + "`;"
        self.cur.execute(zaprosy)
        zapros = pd.DataFrame(self.cur.fetchall())
        zapros.columns= [x[0] for x in self.cur.description]
        app_mine=Table(root8, dataframe=zapros, showtoolbar=True,showstatusbar=True)
        app_mine.show()

    # вставить строку
    def insert_row(self,dat):
        root9=tk.Toplevel()
        root9.geometry("700x200")
        root9.title('Добавить данные')
        print(dat)
        
        column_names="SELECT column_name FROM information_schema.columns where table_name = '" + dat + "' and table_schema = 'videokassety2' ORDER BY ordinal_position;"
        self.cur.execute(column_names)
        column_names=self.cur.fetchall()
        print(column_names)
        entries=[]
        for index, dat_2 in enumerate(column_names):
            print(index, dat_2)
            if index > 0:
                # print('dat_2[0]: '  , dat_2[0])
                if dat_2[0] == 'ID Компании':
                    ttk.Label(root9, text=index, anchor='w', justify = "left").grid(row=index+1, column=0, sticky='W')
                    ttk.Label(root9, text='Название компании', anchor='w', justify = "left").grid(row=index+1, column=1, sticky='W')
                    entries.append(tk.StringVar())
                    table_chosen_3 = ttk.Combobox(root9, width=40, textvariable=entries[index-1], justify = "left", state="readonly")
                    get_companies_v2="SELECT `Название компании` FROM videokassety2.`компания производитель`;"
                    self.cur.execute(get_companies_v2)
                    values_to_choose_3 = self.cur.fetchall()
                    list_to_choose_3=[]
                    for value in values_to_choose_3:
                        #print(value)
                        #print(type(value))
                        list_to_choose_3.append(value[0])
                    table_chosen_3['values'] = (list_to_choose_3)
                    table_chosen_3.grid(column=2, row=index+1, sticky='W')          
                    
                elif dat_2[0] == 'Номер фильма':
                    ttk.Label(root9, text=index, anchor='w', justify = "left").grid(row=index+1, column=0, sticky='W')
                    ttk.Label(root9, text='Название фильма', anchor='w', justify = "left").grid(row=index+1, column=1, sticky='W')
                    entries.append(tk.StringVar())
                    table_chosen_4 = ttk.Combobox(root9, width=40, textvariable=entries[index-1], justify = "left", state="readonly")
                    get_companies_v3="SELECT `Название фильма` FROM videokassety2.`сведения о фильме`;"
                    self.cur.execute(get_companies_v3)
                    values_to_choose_4 = self.cur.fetchall()
                    # print('myyyyyy: ', values_to_choose_4)
                    list_to_choose_4=[]
                    for value in values_to_choose_4:
                        # print(value[0])
                        # print(type(value))
                        list_to_choose_4.append(value[0])
                    # print('myyyyyy2: ', list_to_choose_4)
                    table_chosen_4['values'] = (list_to_choose_4)
                    table_chosen_4.grid(column=2, row=index+1, sticky='W')        
                    
                else:
                    ttk.Label(root9, text=index, anchor='w', justify = "left").grid(row=index+1, column=0, sticky='W')
                    ttk.Label(root9, text=dat_2[0], anchor='w', justify = "left").grid(row=index+1, column=1, sticky='W')
                    entries.append(tk.StringVar())
                    ttk.Entry(root9, textvariable=entries[index-1], width=110).grid(column=2, row=index+1)
        ttk.Button(root9, text="сохранить", command=partial(self.save, entries,column_names,dat)).grid(row=index+2,column=0)
        
    # Вставка данных кнопка
    def save(self, entries,column_names,dat):
        to_insert = []
        list_year = ['Год основания','Год выпуска']
        list_dates = ['Дата выдачи','Дата возвращения']
        list_numbers = ['Залог','Оплата']
        list_chars = ['ФИО клиента','Адрес клиента','Название компании','Страна','Город','Основные исполнители','Характер фильма','Название фильма']
        print("dat_2:", dat)
        command="insert into `" + str(dat) + "` ("
        for j,cols in enumerate(column_names):
            if j == (len(column_names) -1):
                command += "`" + str(cols[0]) + "`) VALUES("
            elif j > 0:
                command += "`" + str(cols[0]) + "`, "


    # проверка года
            if cols[0] in list_year:
                year = j-1
                # print(f'cols: {cols[0]}')
                
                if (entries[j-1].get() == ""):
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как содержимым этого поля не может быть пустым")
                    raise Exception()  
                
                try:
                    int(entries[j-1].get())
                except:
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как содержимым этого поля не могут быть нецифровые символы")
                            
                if (int(entries[j-1].get()) > 2100):
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как год не может быть больше 2100. Впишите год заново")
                    raise Exception()            

                if (int(entries[j-1].get()) < 1900):
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как год не может быть меньше 1900. Впишите год заново")
                    raise Exception()  
                    
                    

    # проверка dates
            if cols[0] in list_dates:
                try:
                    datetime.strptime(entries[j-1].get(), '%Y-%m-%d')
                except ValueError:
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как дата должна быть в формате ГГГГ-MM-ДД и не может быть пустым значением")

    # проверка чисел
            if cols[0] in list_numbers:
                
                if (entries[j-1].get() == ""):
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как содержимое этого поля не может быть пустым")
                    raise Exception()                  
                
                try:
                    int(entries[j-1].get())
                except ValueError:
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как содержимое этого поля не могут быть нецифровые символы")

                if (int(entries[j-1].get()) < 0):
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как число меньше 0")
                    raise Exception()      

                if (int(entries[j-1].get()) > 10000):
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как число больше 10000")
                    raise Exception()    


    # проверка строковых данных
            if cols[0] in list_chars:
                if len(entries[j-1].get()) > 100:
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как строковая переменная длиной более 100 символов")
                    raise Exception()            
                if len(entries[j-1].get()) == 0 :
                    tkinter.messagebox.showerror('Error', "Неправильное значение не будет введено, так как содержимым этого поля не может быть пустым значением")
                    raise Exception()                              

                 
                    
        for k in to_insert:
            command += k
            
        for i, entr in enumerate(entries):
            s=entr.get()
            print("I need: ",s)
            print("I need2: ",s.split(' ')[0])
            
            
            if dat == 'данные о выдачах' and i == 0:
                print(i)
                get_A100="SELECT `Номер фильма` FROM videokassety2.`сведения о фильме` where `Название фильма` = '" + s + "';"
                print(get_A100)
                self.cur.execute(get_A100)
                s = str(self.cur.fetchall()[0][0])
                # print(value_A100)
                # print(value_A100[0][0])

            if dat == 'сведения о фильме' and i == 1:
                print(i)
                get_A100="SELECT `ID Компании` FROM videokassety2.`компания производитель` where `Название компании` = '" + s + "';"
                print(get_A100)
                self.cur.execute(get_A100)
                s = str(self.cur.fetchall()[0][0])                
            
            if len(s) > 1:
                # s.split(' ')
                if i == (len(entries) -1):
                    command += "'" + s.split(' ')[0] +"');"
                else:
                    command += "'" + s.split(' ')[0] +"',"                
            else:
                if i == (len(entries) -1):
                    command += "'" + s +"');"
                else:
                    command += "'" + s +"',"
                
        print(f'command: {command}')
            
        self.cur.execute(command)
        self.con.commit()
    
    ###################################### Все что необходимо для кнопки "Удалить данные" ####################################
    # Удалить данные
    def delete_row(self,dat):
        print(dat)
        root5=tk.Toplevel()
        root5.geometry("700x200")
        root5.title('Удалить данные')
        column_names="SELECT column_name FROM information_schema.columns where table_name = '" + dat + "' and table_schema = 'videokassety2' ORDER BY ordinal_position;"
        self.cur.execute(column_names)
        column_names=self.cur.fetchall()
        text_100 = "Впишите номер " + column_names[0][0] + " для удаления"
        ttk.Label(root5, text=text_100, wraplength=700, anchor='w', justify = "left").grid(row=0, column=0, sticky='W')
        var=tk.StringVar()
        ttk.Entry(root5, textvariable=var, width=110).grid(column=0, row=1)
        ttk.Button(root5, text="удалить", command=partial(self.delete, var, dat, column_names[0][0])).grid(row=2,column=0)
    
    # Удалить данные кнопка
    def delete(self,var, dat, column):
        s=var.get()
        command="delete from `" + dat + "` where `" + str(column) + "` = '" + s + "';"
        print(command)
        self.cur.execute(command)
        self.con.commit()
    
    ###################################### Все что необходимо для кнопки "Обновить данные" ####################################    
    # Обновить данные
    def update_row(self,dat):
        # print(dat)
        root6=tk.Toplevel()
        root6.geometry("700x200")
        root6.title('Обновить данные')
        column_names="SELECT column_name FROM information_schema.columns where table_name = '" + dat + "' and table_schema = 'videokassety2' ORDER BY ordinal_position;"
        self.cur.execute(column_names)
        column_names=self.cur.fetchall()
        text_101 = "Впишите номер " + column_names[0][0] + " для обновления данных"
        ttk.Label(root6, text=text_101, wraplength=700, anchor='w', justify = "left").grid(row=0, column=0, sticky='W')
        var=tk.StringVar()
        ttk.Label(root6, text="Выберите название колонки которую необходимо обновить", wraplength=700, anchor='w', justify = "left").grid(row=2, column=0, sticky='W')
        ttk.Label(root6, text="Впишите новые данные для этой колонки и строки", wraplength=700, anchor='w', justify = "left").grid(row=4, column=0, sticky='W')
        var3=tk.StringVar()
        
        var2=tk.StringVar()
        table_chosen_2 = ttk.Combobox(root6, width=40, textvariable=var2, justify = "left", state="readonly")
        get_companies="SELECT column_name FROM information_schema.columns where table_name = '" + dat + "' and table_schema = 'videokassety2' ORDER BY ordinal_position;"
        self.cur.execute(get_companies)
        values_to_choose_2 = self.cur.fetchall()
        list_to_choose_2=[]
        for value in values_to_choose_2:
            list_to_choose_2.append(value[0])
        table_chosen_2['values'] = (list_to_choose_2)
        table_chosen_2.grid(column=0, row=3, sticky='W')    
        
        ttk.Entry(root6, textvariable=var, width=110).grid(column=0, row=1)
        ttk.Entry(root6, textvariable=var3, width=110).grid(column=0, row=5)
        ttk.Button(root6, text="Обновить", command=partial(self.update, var, var2, var3, dat, column_names[0][0])).grid(row=6,column=0)
    
    # Обновить данные кнопка
    def update(self,var, var2, var3, dat, column):
        s=var.get()
        s2=var2.get()
        s3=var3.get()
        command="Update `" + dat + "` set `" + str(s2) + "` = '" + s3 + "' where `" + str(column) + "` = '" + s + "';"
        print(command)
        self.cur.execute(command)
        self.con.commit()

    
class Report:
    def __init__(self, master, cur):
        self.master = master
        self.master.geometry('500x250+100+200')
        self.master.title('Виды отчетов')
        self.cur = cur
        self.button7=Button(self.master,text="Частота выдачи фильма и прибыль, получаемая от проката фильма",fg='blue',command=self.gotoreport1).grid(row=1,column=1)
        self.button8=Button(self.master,text="Справка о выдаче за день на дату (названия фильмов и срок проката)",fg='blue',command=self.insertdate).grid(row=2,column=1)
        self.button9=Button(self.master,text="Справка по компании-производителю с названиями фильмов за заданный срок",fg='blue',command=self.insertdate2).grid(row=3,column=1)
        self.button10=Button(self.master,text="Список фильмов по жанру",fg='blue',command=self.insertdate3).grid(row=4,column=1)
        self.button10=Button(self.master,text="Рейтинг самых популярных фильмов",fg='blue',command=self.gotoreport5).grid(row=5,column=1)
                
    def showallrecords(self):
        Data = self.readfromdatabase()
        for index, dat in enumerate(Data):
            Label(self.master, text=index+1).grid(row=index+1, column=0)
            Label(self.master, text=dat[0]).grid(row=index+1, column=1)

    def readfromdatabase(self):
        self.cur.execute("show full tables where table_type= 'BASE TABLE';")
        return self.cur.fetchall()

    def gotoreport1(self):    
        var6 = "SELECT `сведения о фильме`.`Название фильма`, count(`данные о выдачах`.`Номер фильма`) as 'Частота выдачи фильма', sum(`данные о выдачах`.`Оплата`) as 'Прибыль' FROM videokassety2.`сведения о фильме`, videokassety2.`данные о выдачах` where `сведения о фильме`.`Номер фильма` = `данные о выдачах`.`Номер фильма` group by `данные о выдачах`.`Номер фильма` order by count(`данные о выдачах`.`Номер фильма`) DESC;"
        title1 = "Справка о частоте выдачи фильма и прибыли, получаемой от проката фильма"
        self.Report_generate(var6, title1)

    def insertdate(self):    
        root5=tk.Toplevel()
        root5.title('Справка о выдаче за день на дату (названия фильмов и срок проката)')
        ttk.Label(root5, text="Внесите дату в формате yyyy-mm-dd", wraplength=700, anchor='w', justify = "left").grid(row=1, column=1, sticky='W')
        var10=tk.StringVar()
        ttk.Entry(root5, textvariable=var10, width=50).grid(column=1, row=2)
        ttk.Button(root5, text="создать отчет", command=partial(self.gotoreport2, var10)).grid(row=3,column=1)

    def gotoreport2(self, var10): 
        s6=var10.get()
        var13 = "SELECT `сведения о фильме`.`Название фильма`, `данные о выдачах`.`Дата возвращения` - `данные о выдачах`.`Дата выдачи` as 'Срок проката'  FROM videokassety2.`сведения о фильме`, videokassety2.`данные о выдачах` where `сведения о фильме`.`Номер фильма` = `данные о выдачах`.`Номер фильма` and `данные о выдачах`.`Дата выдачи` = '" + s6 + "' order by (`данные о выдачах`.`Дата возвращения` - `данные о выдачах`.`Дата выдачи`) DESC;"
        title2 = "Справка о выдаче за день на дату (названия фильмов и срок проката) на дату:" + s6
        self.Report_generate(var13, title2)    
        
    def Report_generate(self,var, title):
        root8=tk.Toplevel()
        root8.title("Справка о частоте выдачи фильма и прибыли, получаемой от проката фильма")
        root8.title(title)
        self.cur.execute(var)
        zapros = pd.DataFrame(self.cur.fetchall())
        zapros.columns= [x[0] for x in self.cur.description]
        app_mine=Table(root8, dataframe=zapros, showtoolbar=True,showstatusbar=True)
        app_mine.show()

    def insertdate2(self):    
        root6=tk.Toplevel()
        root6.title('Справка по компании-производителю с названиями фильмов за заданный срок')
        ttk.Label(root6, text="Выберите компанию", wraplength=700, anchor='w', justify = "left").grid(row=1, column=1, sticky='W')
        var11=tk.StringVar()
        table_chosen_2 = ttk.Combobox(root6, width=40, textvariable=var11, justify = "left", state="readonly")
        get_companies="SELECT `Название компании` FROM videokassety2.`компания производитель`;"
        self.cur.execute(get_companies)
        values_to_choose_2 = self.cur.fetchall()
        list_to_choose_2=[]
        for value in values_to_choose_2:
            list_to_choose_2.append(value[0])
        table_chosen_2['values'] = (list_to_choose_2)
        table_chosen_2.grid(column=1, row=2, sticky='W')  
        
        ttk.Label(root6, text="Внесите год начала и год конца через запятую", wraplength=700, anchor='w', justify = "left").grid(row=3, column=1, sticky='W')
        var12=tk.StringVar()
        ttk.Entry(root6, textvariable=var12, width=50).grid(column=1, row=4)        
        ttk.Button(root6, text="создать отчет", command=partial(self.gotoreport3, var11, var12)).grid(row=5,column=1)

    def gotoreport3(self, var11, var12): 
        s7=var11.get()
        s8=var12.get().split(",")
        var13 = "SELECT `сведения о фильме`.`Название фильма` FROM videokassety2.`сведения о фильме`, videokassety2.`компания производитель` where `сведения о фильме`.`ID Компании` = `компания производитель`.`ID Компании` and `компания производитель`.`Название компании` = '" + s7 + "' and (`сведения о фильме`.`Год выпуска` between " + s8[0] + " and " + s8[1] + ");"
        title3 = "Справка по компании-производителю с названиями фильмов за заданный срок на компанию: " + s7 + " за период между " + s8[0] + " и " + s8[1]
        self.Report_generate(var13, title3)    

    def insertdate3(self):    
        root7=tk.Toplevel()
        root7.title('Список фильмов по жанру')
        ttk.Label(root7, text="Выберите компанию", wraplength=700, anchor='w', justify = "left").grid(row=1, column=1, sticky='W')
        var15=tk.StringVar()
        table_chosen_2 = ttk.Combobox(root7, width=40, textvariable=var15, justify = "left", state="readonly")
        table_chosen_2['values'] = ["фантастика", "мультфильм","драма", "криминал","детектив", "комедия","триллер"]
        table_chosen_2.grid(column=1, row=2, sticky='W')    
        ttk.Button(root7, text="создать отчет", command=partial(self.gotoreport4, var15)).grid(row=5,column=1)
        
    def gotoreport4(self, var15): 
        s7=var15.get()
        var13 = "SELECT `сведения о фильме`.`Название фильма`, `сведения о фильме`.`Характер фильма` FROM videokassety2.`сведения о фильме` where `сведения о фильме`.`Характер фильма` like '%" + s7 + "%';"
        title4 = "Список фильмов по жанру: " + s7
        self.Report_generate(var13, title4)    

    def gotoreport5(self):    
        var14 = "SELECT `сведения о фильме`.`Название фильма`, RANK() OVER (order by count(`данные о выдачах`.`Номер фильма`) desc) as 'Рейтинг' FROM videokassety2.`сведения о фильме`, videokassety2.`данные о выдачах` where `сведения о фильме`.`Номер фильма` = `данные о выдачах`.`Номер фильма` group by `данные о выдачах`.`Номер фильма`;"
        
        title5 = "Рейтинг самых популярных фильмов"
        self.Report_generate(var14, title5)

        
#  login window
def validateLogin(username, password,root, Host, Port):
    User = username.get()
    Password = password.get()
    Host = Host.get()
    Port = Port.get()    

    # Port number
    if Port < 0 or Port > 65535:
        tkinter.messagebox.showerror('Error', "Значение порта должно быть > 0 и < 65535")
        raise Exception()  
    
    
    
    try:
        con = pymysql.connect(database = 'videokassety2', user=str(User), password = str(Password), host=str(Host), port=Port)
        # print(Connection.messages)
        # print(con)
        cur = con.cursor()
        root111=tk.Toplevel()
        myGUIWelcome = Welcome(root111,root, cur, con)
        root.withdraw()
    except:
        tkinter.messagebox.showerror('Error', "Вы указали неверный логин, пароль, Host или Port. Либо данная база данных не существует.")
           
# main window
def main():
    root=Tk()
    root.title('Login')
    #user name
    usernameLabel = Label(root, text="User Name").grid(row=0, column=0)
    username = StringVar(value='root')
    usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)  
    #password label and password entry box
    passwordLabel = Label(root,text="Password").grid(row=1, column=0)  
    password = StringVar(value='***')
    passwordEntry = Entry(root, textvariable=password).grid(row=1, column=1)  
    #Host
    HostLabel = Label(root,text="Host для MySQL").grid(row=2, column=0)  
    Host = StringVar(value='localhost')
    HostEntry = Entry(root, textvariable=Host).grid(row=2, column=1)  
    #Port
    PortLabel = Label(root,text="Port для MySQL").grid(row=3, column=0)  
    Port = IntVar(value=3306)
    PortEntry = Entry(root, textvariable=Port).grid(row=3, column=1)      
    #login button
    loginButton = Button(root, text="Login", command=partial(validateLogin, username, password,root, Host, Port)).grid(row=4, column=0)  
    root.mainloop()

if __name__ == '__main__':
     main()