from wsgiref.headers import Headers

import tkinter
from tabulate import tabulate
import pyodbc
import  customtkinter
from pyodbc import connect
def connect_database():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=RICHARD;'
        f'DATABASE={entry_database.get()};'
        'Trusted_Connection=True;'
    )


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1080x720")
app.title('Employee Database Management')

entry_database = customtkinter.CTkEntry(app,placeholder_text="Database Name")
entry_database.place(relx=0.1,rely=0.1)

def create_db():
    try:

        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=RICHARD;'
            f'DATABASE=master;'
            'Trusted_Connection=True;'
        )
        connection.autocommit = True
        connection.execute(f'Create database {entry_database.get()}')
        info_label.configure(text="Database Created successfully")


    except Exception as e:
        print("Connection Failed", e)
        info_label.configure(text="Database Creation Failed")
    finally:
        if connection:
            connection.close()
            print('Connection closed')
create_button = customtkinter.CTkButton(app,text="Create Database",command=create_db,fg_color= "green")
create_button.place(relx=0.1,rely=0.2)
def connect_db():
    try:

        connection = connect_database()
        info_label.configure(text="Connection Successfull")

    except Exception as e:
        print("Connection Failed", e)
        info_label.configure(text="Connection Failed")

def delete_db():
    try:

        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=RICHARD;'
            f'DATABASE=master;'
            'Trusted_Connection=True;'
        )
        connection.autocommit = True
        connection.execute(f'drop database {entry_database.get()}')
        info_label.configure(text="Database Deleted")

    except Exception as e:
        print("Deletion Failed", e)
        info_label.configure(text="Deletion Failed")

connect_button = customtkinter.CTkButton(app,text="Connect to Database",command=connect_db,fg_color= "blue")
connect_button.place(relx=0.1,rely=0.3)
delete_button = customtkinter.CTkButton(app,text="Delete Database",command=delete_db,fg_color= "red")
delete_button.place(relx=0.1,rely=0.4)
info_label = customtkinter.CTkLabel(app, text="")
info_label1 = customtkinter.CTkLabel(app, text="")
info_label.place(relx = 0.1, rely = 0.5)


#TABLE CREATION DELETION CODE


entry_table_name = customtkinter.CTkEntry(app,placeholder_text="Create Table Name",width=150)
entry_table_name.place(relx=0.25,rely=0.1)

entry_column1 = customtkinter.CTkEntry(app,placeholder_text="Create Column_1",width=150)
entry_column1.place(relx=0.25,rely=0.2)

entry_column2 = customtkinter.CTkEntry(app,placeholder_text="Create Column_2",width=150)
entry_column2.place(relx=0.25,rely=0.3)

entry_column3 = customtkinter.CTkEntry(app,placeholder_text="Create Column_3",width=150)
entry_column3.place(relx=0.25,rely=0.4)

def create_table():
    try:

        connection =connect_database()
        connection.autocommit = True
        sql_create_tbl = f"CREATE TABLE {entry_table_name.get()}\
                           ({entry_column1.get()} {radio_var_col1.get()},\
                           {entry_column2.get()} {radio_var_col2.get()},\
                           {entry_column3.get()} {radio_var_col3.get()})"
        connection.execute(sql_create_tbl)

        info_label.configure(text="Table Created")

    except Exception as e:
        print("Tabele Creation failed", e)
        info_label.configure(text="Table Creation Failed")

def delete_table():
    try:

        connection = connect_database()
        connection.autocommit = True
        sql_delete_tbl = f"Drop TABLE {entry_table_name.get()}"
        connection.execute(sql_delete_tbl)

        info_label.configure(text="Table Deleted")

    except Exception as e:
        print("Tabele Creation failed", e)
        info_label.configure(text="Table Creation Failed")


create_button = customtkinter.CTkButton(app,text="Create Table",command=create_table)
create_button.place(relx=0.5,rely=0.1)

delete_button = customtkinter.CTkButton(app,text="Delete Table",command=delete_table)
delete_button.place(relx=0.4,rely=0.1)

radio_var_col1 = tkinter.StringVar(value="")
col1_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable = radio_var_col1,
                                                 value="varchar(50)")
col1_rd_varchar50.place(relx=0.4,rely=0.2)
col1_rd_int = customtkinter.CTkRadioButton(app,
                                                 text="integer",
                                                 variable = radio_var_col1,
                                                 value="integer")
col1_rd_int.place(relx=0.5,rely=0.2)

radio_var_col2 = tkinter.StringVar(value="")
col2_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable = radio_var_col2,
                                                 value="varchar(50)")
col2_rd_varchar50.place(relx=0.4,rely=0.3)
col2_rd_int = customtkinter.CTkRadioButton(app,
                                                 text="integer",
                                                 variable = radio_var_col2,
                                                 value="integer")
col2_rd_int.place(relx=0.5,rely=0.3)

radio_var_col3 = tkinter.StringVar(value="")
col3_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable = radio_var_col3,
                                                 value="varchar(50)")
col3_rd_varchar50.place(relx=0.4,rely=0.4)
col3_rd_int = customtkinter.CTkRadioButton(app,
                                                 text="integer",
                                                 variable = radio_var_col3,
                                                 value="integer")
col3_rd_int.place(relx=0.5,rely=0.4)


#INSERT INTO CODE
def insert_into_table():
    try:

        connection = connect_database()
        connection.autocommit = True
        sql_insertinto_tbl = f"Insert into {entry_ins_table_name.get()}\
                           Values ({entry_ins_column1.get()},'{entry_ins_column2.get()}','{entry_ins_column3.get()}')"
        connection.execute(sql_insertinto_tbl)

        info_label.configure(text="Value Insertion successfull")

    except Exception as e:
        print("Value Insertion failed", e)
        info_label.configure(text="Value Insertion Failed")

entry_ins_table_name = customtkinter.CTkEntry(app,placeholder_text="Insert/Select Table Name",width=150)
entry_ins_table_name.place(relx=0.6,rely=0.1)

entry_ins_column1 = customtkinter.CTkEntry(app,placeholder_text="ID",width=150)
entry_ins_column1.place(relx=0.6,rely=0.2)

entry_ins_column2 = customtkinter.CTkEntry(app,placeholder_text="First Name",width=150)
entry_ins_column2.place(relx=0.6,rely=0.3)

entry_ins_column3 = customtkinter.CTkEntry(app,placeholder_text="Last Name",width=150)
entry_ins_column3.place(relx=0.6, rely=0.4)


insert_button = customtkinter.CTkButton(app,text="Insert Values into Table",command=insert_into_table)
insert_button.place(relx=0.75,rely=0.4)

#SELECT TABLE CODE:
def select_row():
    try:
        connection = connect_database()  # Get the connection object
        connection.autocommit = True
        cursor = connection.cursor()
        select_query = f"Select * from {entry_ins_table_name.get()} where id = {entry_ins_column1.get()}"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        cursor.close()
        info_label.configure(text="Rows Displayed below")
        if rows:
            info_label1.configure(text= tabulate(rows, headers = ['ID','First Name','Last Name']),
                                  justify ="left",
                                  wraplength=300,font=('Arial',15))
            info_label1.place(relx=0.3,rely=0.65,relwidth=0.5)
        else:
            info_label1.configure(text=f"No record Found")
            info_label1.place(relx=0.3, rely=0.65, relwidth=0.5)
    except Exception as e:
        print("Select Failed", e)
        info_label.configure(text="Select Query Failed")



select_button = customtkinter.CTkButton(app,text="Select Where ID",command=select_row)
select_button.place(relx=0.75,rely=0.1)

#DELETE ROW CODE:

def delete_row():
    try:
        connection = connect_database()  # Get the connection object
        connection.autocommit = True
        cursor = connection.cursor()
        delete_row_query = f"delete from {entry_ins_table_name.get()} where id = {entry_ins_column1.get()}"
        cursor.execute(delete_row_query)

        cursor.close()
        info_label.configure(text="Row Deleted Successfully")
    except Exception as e:
        print("Row Deletion Failed", e)
        info_label.configure(text="Delete Row Query Failed")
delete_row_button = customtkinter.CTkButton(app,text="Delete Where ID",command=delete_row)
delete_row_button.place(relx=0.75,rely=0.2)

#Update ROW CODE:
def update_row():
    try:
        connection = connect_database()  # Get the connection object
        connection.autocommit = True
        cursor = connection.cursor()
        update_row_query = (f"update {entry_ins_table_name.get()}\
                            set first_name = '{entry_ins_column2.get()}', last_name = '{entry_ins_column3.get()}'\
                            where id = {entry_ins_column1.get()}")
        cursor.execute(update_row_query)

        cursor.close()
        info_label.configure(text="Row updated Successfully")
    except Exception as e:
        print("Row Deletion Failed", e)
        info_label.configure(text="update Row Query Failed")


Update_row_button = customtkinter.CTkButton(app,text="Update Where ID",command=update_row)
Update_row_button.place(relx=0.75,rely=0.3)
app.mainloop()
