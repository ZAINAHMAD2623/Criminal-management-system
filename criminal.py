from tkinter import *
from tkinter  import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')


        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()


        

        lbl_title=Label(self.root,text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE",font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)
        
        #ncr Logo
        img_logo=Image.open('images/logo.jpg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)

        
        #img frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        #1 img
        img1=Image.open('images/logo.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=160)

        #2nd img
        img2=Image.open('images/logo.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=540,y=0,width=540,height=160)

        #3rd pic
        img3=Image.open('images/logo.jpg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=1080,y=0,width=540,height=160)
        
        #Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        #upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal information",font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)
        
        #labels-Entry

        #caseId
        caseid=Label(upper_frame,text='Case ID: ',font=('aerial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('aerial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        #criminalNo
        lbl_criminal_no=Label(upper_frame,text='Criminal No:',font=('aerial',11,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('aerial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2)

        #criminalName
        lbl_name=Label(upper_frame,text='Criminal name: ',font=('aerial',12,'bold'),bg='white')
        lbl_name.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        
        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('aerial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7)

        #nickName
        lbl_nickname=Label(upper_frame,text='Nick name: ',font=('aerial',12,'bold'),bg='white')
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        
        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('aerial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        #arrestDate
        lbl_arrestDate=Label(upper_frame,text='Arrest date: ',font=('aerial',12,'bold'),bg='white')
        lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        
        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('aerial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)

        #DateOfCrime
        lbl_dateOfCrime=Label(upper_frame,text='Date of crime: ',font=('aerial',12,'bold'),bg='white')
        lbl_dateOfCrime.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        
        txt_dateOfCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('aerial',11,'bold'))
        txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7)

        #Address
        lbl_address=Label(upper_frame,text='Address: ',font=('aerial',12,'bold'),bg='white')
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('aerial',11,'bold'))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #Age
        lbl_age=Label(upper_frame,text='Age: ',font=('aerial',12,'bold'),bg='white')
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        
        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('aerial',11,'bold'))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        #Occupation
        lbl_occupation=Label(upper_frame,text='Occupation: ',font=('aerial',12,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        
        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('aerial',11,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        #birthMark
        lbl_birthplace=Label(upper_frame,text='BirthMark: ',font=('aerial',12,'bold'),bg='white')
        lbl_birthplace.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        
        txt_birthplace=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=('aerial',11,'bold'))
        txt_birthplace.grid(row=4,column=3,padx=2,pady=7)

        #Crimetype
        lbl_crimeType=Label(upper_frame,text='Crime type: ',font=('aerial',12,'bold'),bg='white')
        lbl_crimeType.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('aerial',11,'bold'))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        #Father name
        lbl_fatherName=Label(upper_frame,text='Father name: ',font=('aerial',12,'bold'),bg='white')
        lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        
        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('aerial',11,'bold'))
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7)
        
        #gender
        lbl_gender=Label(upper_frame,text='Gender: ',font=('aerial',12,'bold'),bg='white')
        lbl_gender.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        #wanted
        lbl_wanted=Label(upper_frame,text='Most wanted: ',font=('aerial',12,'bold'),bg='white')
        lbl_wanted.grid(row=3,column=4,padx=2,pady=7,sticky=W)

        #radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=90,width=190,height=30)
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='male',value='male',font=('aerial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('aerial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=730,y=130,width=190,height=30)
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='yes',value='yes',font=('aerial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='no',value='no',font=('aerial',9,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        #add button
        btn_add=Button(button_frame,command=self.add_data,text='record save',font=('aerial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #update button
        btn_update=Button(button_frame,command=self.update_data,text='update',font=('aerial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        
        #delete button
        btn_delete=Button(button_frame,command=self.delete_data,text='delete',font=('aerial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
        
        #clear button
        btn_clear=Button(button_frame,command=self.clear_data,text='clear',font=('aerial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        
        # background right side image

        img_crime=Image.open('images/logo.jpg')
        img_crime=img_crime.resize((470,245),Image.ANTIALIAS)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=1000,y=0,width=470,height=245)
        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal information",font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="Search criminal record",font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)
        
        search_by=Label(search_frame,text='Search by: ',font=('aerial',11,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('aerial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('aerial',11,'bold'))
        search_txt.grid(row=0,column=2,padx=5,sticky=W)

        #search button
        btn_search=Button(search_frame,command=self.search_data,text='search',font=('aerial',13,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)
        
        #all button
        btn_all=Button(search_frame,command=self.fetch_data,text='show all',font=('aerial',13,'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)
        
        crimeagency=Label(search_frame,text='NATIONAL CRIME AGENCY',font=('aerial',30,'bold'),fg='crimson',bg='white')
        crimeagency.grid(row=0,column=5,padx=50,sticky=W)

        #tabel frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE,)
        table_frame.place(x=0,y=60,width=1470,height=170)

        


        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nick Name')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='DateOfCrime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')
         
        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()
    
    #Add function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Iken5393@',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arrest_date.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_birthMark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_father_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()

                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
    
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Iken5393@',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    #update
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure you want to update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Iken5393@',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal1 set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(

                                                                                                                            
                                                                                                                                                                                                self.var_criminal_no.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_nickname.get(),
                                                                                                                                                                                                self.var_arrest_date.get(),
                                                                                                                                                                                                self.var_date_of_crime.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                self.var_occupation.get(),
                                                                                                                                                                                                self.var_birthMark.get(),
                                                                                                                                                                                                self.var_crime_type.get(),
                                                                                                                                                                                                self.var_father_name.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_wanted.get(),
                                                                                                                                                                                                self.var_case_id.get()



                                                                                                                                                                                                                                                     ))
                else:
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','Criminal record has been successfully updated')
            except Exception as es:
                messagebox.showerror('error',f'Due To{str(es)}')
    
    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure you want to delete this criminal record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Iken5393@',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal1 where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','Criminal record has been successfully deleted')
            except Exception as es:
                messagebox.showerror('error',f'Due To{str(es)}')

    #clear:
    def clear_data(self):
         self.var_case_id.set("")
         self.var_criminal_no.set("")
         self.var_name.set("")
         self.var_nickname.set("")
         self.var_arrest_date.set("")
         self.var_date_of_crime.set("")
         self.var_address.set("")
         self.var_age.set("")
         self.var_occupation.set("")
         self.var_birthMark.set("")
         self.var_crime_type.set("")
         self.var_father_name.set("")
         self.var_gender.set("")
         self.var_wanted.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="":
             messagebox.showerror('error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Iken5393@',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal1 where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                      self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')





             
               

                


            




        








         
        
if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()