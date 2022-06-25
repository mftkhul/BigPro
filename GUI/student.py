from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Informasi Siswa")

        #-----------Variables-------------------
        self.var_kampus=StringVar()
        self.var_jurusan=StringVar()
        self.var_tahun=StringVar()
        self.var_semester=StringVar()
        self.var_nim=StringVar()
        self.var_nama=StringVar()
        self.var_kelas=StringVar()
        self.var_absen=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_hp=StringVar()
        self.var_alamat=StringVar()
        self.var_dosen=StringVar()

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI/banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Panel Informasi Siswa",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Detail Siswa",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        # Jurusan frame 
        jurusan_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Kejuruan",font=("verdana",12,"bold"),fg="navyblue")
        jurusan_frame.place(x=10,y=5,width=635,height=150)

        #label kampus
        kampus_label=Label(jurusan_frame,text="Kampus",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        kampus_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        kampus_combo=ttk.Combobox(jurusan_frame,textvariable=self.var_kampus,width=15,font=("verdana",12,"bold"),state="readonly")
        kampus_combo["values"]=("Select Kampus","Harapan Bersama")
        kampus_combo.current(0)
        kampus_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        # -----------------------------------------------------

        #label jurusan
        jurusan_label=Label(jurusan_frame,text="Jurusan",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        jurusan_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box 
        jurusan_combo=ttk.Combobox(jurusan_frame,textvariable=self.var_jurusan,width=15,font=("verdana",12,"bold"),state="readonly")
        jurusan_combo["values"]=("Pilih Jurusan","T.Komputer","T.Informatika","Farmasi")
        jurusan_combo.current(0)
        jurusan_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        #-------------------------------------------------------------

        #label Year
        tahun_label=Label(jurusan_frame,text="Tahun",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        tahun_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        tahun_combo=ttk.Combobox(jurusan_frame,textvariable=self.var_tahun,width=15,font=("verdana",12,"bold"),state="readonly")
        tahun_combo["values"]=("Pilih tahun masuk","2017","2018","2019","2020","2021","2022")
        tahun_combo.current(0)
        tahun_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #-----------------------------------------------------------------

        #label Semester 
        semester_label=Label(jurusan_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        #combo box 
        semester_combo=ttk.Combobox(jurusan_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        #Class Student Information
        detail_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Detail Siswa",font=("verdana",12,"bold"),fg="navyblue")
        detail_frame.place(x=10,y=160,width=635,height=230)

        #Student id
        nim_label = Label(detail_frame,text="Nim:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        nim_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        nim_entry = ttk.Entry(detail_frame,textvariable=self.var_nim,width=15,font=("verdana",12,"bold"))
        nim_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        student_name_label = Label(detail_frame,text="Nama Siswa:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(detail_frame,textvariable=self.var_nama,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Kelas
        kelas_label = Label(detail_frame,text="Kelas:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        kelas_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        kelas_combo=ttk.Combobox(detail_frame,textvariable=self.var_kelas,width=13,font=("verdana",12,"bold"),state="readonly")
        kelas_combo["values"]=("A","B","C","D")
        kelas_combo.current(0)
        kelas_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #No. Absen
        absen_label = Label(detail_frame,text="No-Absen:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        absen_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        absen_entry = ttk.Entry(detail_frame,textvariable=self.var_absen,width=15,font=("verdana",12,"bold"))
        absen_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        gender_label = Label(detail_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(detail_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date of Birth
        date_label = Label(detail_frame,text="Tanggal Lahir:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(detail_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        email_label = Label(detail_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        email_entry = ttk.Entry(detail_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        hp_label = Label(detail_frame,text="No-Hp:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        hp_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        hp_entry = ttk.Entry(detail_frame,textvariable=self.var_hp,width=15,font=("verdana",12,"bold"))
        hp_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        alamat_label = Label(detail_frame,text="Alamat:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        alamat_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        alamat_entry = ttk.Entry(detail_frame,textvariable=self.var_alamat,width=15,font=("verdana",12,"bold"))
        alamat_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Teacher Name
        dosen_label = Label(detail_frame,text="Dosen:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dosen_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        dosen_entry = ttk.Entry(detail_frame,textvariable=self.var_dosen,width=15,font=("verdana",12,"bold"))
        dosen_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(detail_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(detail_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pict",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Pict",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)





        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Detail Siswa",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Searching",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Nim")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("Nim","Nama","Kampus","Jurusan","Tahun","Sem",
                                                            "Kelas","Gender","Tanggal Lahir","No-Hp","Alamat","No-Absen",
                                                            "Email","Dosen","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Nim",text="Nim")
        self.student_table.heading("Nama",text="Nama")
        self.student_table.heading("Kampus",text="Kampus")
        self.student_table.heading("Jurusan",text="Jurusan")
        self.student_table.heading("Tahun",text="Tahun")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Kelas",text="Kelas")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Tanggal Lahir",text="Tanggal Lahir")
        self.student_table.heading("No-Hp",text="No-Hp")
        self.student_table.heading("Alamat",text="Alamat")
        self.student_table.heading("No-Absen",text="No-Absen")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Dosen",text="Dosen")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"


        #Set Width of Colums 
        self.student_table.column("Nim",width=80)
        self.student_table.column("Nama",width=120)
        self.student_table.column("Kampus",width=120)
        self.student_table.column("Jurusan",width=120)
        self.student_table.column("Tahun",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Kelas",width=50)
        self.student_table.column("Gender",width=50)
        self.student_table.column("Tanggal Lahir",width=100)
        self.student_table.column("No-Hp",width=100)
        self.student_table.column("Alamat",width=120)
        self.student_table.column("No-Absen",width=50)
        self.student_table.column("Email",width=100)
        self.student_table.column("Dosen",width=100)
        self.student_table.column("Photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    def add_data(self):
        if self.var_kampus.get()=="Pilih Kampus" or self.var_jurusan.get=="Pilih Jurusan" or self.var_tahun.get()=="Pilih tahun masuk" or self.var_semester.get()=="Pilih Semester" or self.var_nim.get()=="" or self.var_nama.get()=="" or self.var_kelas.get()=="" or self.var_absen.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_hp.get()=="" or self.var_alamat.get()=="" or self.var_dosen.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='25desember',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_nim.get(),
                self.var_nama.get(),
                self.var_kampus.get(),
                self.var_jurusan.get(),
                self.var_tahun.get(),
                self.var_semester.get(),
                self.var_kelas.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_hp.get(),
                self.var_alamat.get(),
                self.var_absen.get(),
                self.var_email.get(),
                self.var_dosen.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='25desember',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_nim.set(data[0]),
        self.var_nama.set(data[1]),
        self.var_kampus.set(data[2]),
        self.var_jurusan.set(data[3]),
        self.var_tahun.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_kelas.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_hp.set(data[9]),
        self.var_alamat.set(data[10]),
        self.var_absen.set(data[11]),
        self.var_email.set(data[12]),
        self.var_dosen.set(data[13]),
        self.var_radio1.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_kampus.get()=="Pilih Kampus" or self.var_jurusan.get=="Pilih Jurusan" or self.var_tahun.get()=="Pilih tahun masuk" or self.var_semester.get()=="Pilih Semester" or self.var_nim.get()=="" or self.var_nama.get()=="" or self.var_kelas.get()=="" or self.var_absen.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_hp.get()=="" or self.var_alamat.get()=="" or self.var_dosen.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='25desember',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Nama=%s,Kampus=%s,Jurusan=%s,Tahun=%s,Semester=%s,Kelas=%s,Gender=%s,Tanggal_Lahir=%s,Hp=%s,Alamat=%s,Absen=%s,Email=%s,Dosen=%s,PhotoSample=%s where Nim=%s",( 
                    self.var_nama.get(),
                    self.var_kampus.get(),
                    self.var_jurusan.get(),
                    self.var_tahun.get(),
                    self.var_semester.get(),
                    self.var_kelas.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_hp.get(),
                    self.var_alamat.get(),
                    self.var_absen.get(),
                    self.var_email.get(),
                    self.var_dosen.get(),
                    self.var_radio1.get(),
                    self.var_nim.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_nim.get()=="":
            messagebox.showerror("Error","Nim Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='25desember',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where Nim=%s"
                    val=(self.var_nim.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_nim.set(""),
        self.var_nama.set(""),
        self.var_kampus.set("Pilih Kampus"),
        self.var_jurusan.set("Pilih jurusan"),
        self.var_tahun.set("Pilih tahun"),
        self.var_semester.set("Pilih Semester"),
        self.var_kelas.set("A"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_hp.set(""),
        self.var_alamat.set(""),
        self.var_absen.set(""),
        self.var_email.set(""),
        self.var_dosen.set(""),
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='25desember',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT Nim,Nama,Kampus,Jurusan,Tahun,Semester,Kelas,Gender,Tanggal_Lahir,Hp,Alamat,Absen,Email,Dosen,PhotoSample FROM student where Nim='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Absen= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_kampus.get()=="Pilih Kampus" or self.var_jurusan.get=="Pilih Jurusan" or self.var_tahun.get()=="Pilih tahun masuk" or self.var_semester.get()=="Pilih Semester" or self.var_nim.get()=="" or self.var_nama.get()=="" or self.var_kelas.get()=="" or self.var_absen.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_hp.get()=="" or self.var_alamat.get()=="" or self.var_dosen.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='25desember',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Nama=%s,Kampus=%s,Jurusan=%s,Tahun=%s,Semester=%s,Kelas=%s,Gender=%s,Tanggal_Lahir=%s,Hp=%s,Alamat=%s,Absen=%s,Email=%s,Dosen=%s,PhotoSample=%s where Nim=%s",( 
                    self.var_nama.get(),
                    self.var_kampus.get(),
                    self.var_jurusan.get(),
                    self.var_tahun.get(),
                    self.var_semester.get(),
                    self.var_kelas.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_hp.get(),
                    self.var_alamat.get(),
                    self.var_absen.get(),
                    self.var_email.get(),
                    self.var_dosen.get(),
                    self.var_radio1.get(),
                    self.var_nim.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
