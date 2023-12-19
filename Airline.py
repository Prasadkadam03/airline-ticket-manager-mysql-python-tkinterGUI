import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

mydb = mysql.connector.connect(host="localhost", user="root", password="8055", charset="utf8")
mycursor = mydb.cursor()
AirlineD = 'create database if not exists Airline'
AirlineU = 'use Airline'
pdataT = 'create table if not exists pdata(custno int primary key,custname varchar(30),addr varchar(30),jrdate date,source varchar(30),destination varchar(30))'
tktT = 'create table if not exists tkt(custno int ,tkt_tot int,lug_tot int,g_tot int)'
mycursor.execute(AirlineD)
mycursor.execute(AirlineU)
mycursor.execute(pdataT)
mycursor.execute(tktT)

root = tk.Tk()
root.title("Airline Ticket Booking System")
root.geometry("800x600")

primary_color = "#2196F3"  # Material Blue
secondary_color = "#FFC107"  # Material Amber
background_color = "#E1F5FE"  # Light Blue background color
text_color = "#000000"  # Black text color

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), background=primary_color, foreground=text_color)
style.configure("TLabel", font=("Helvetica", 14), background=background_color, foreground=text_color)
style.configure("TEntry", font=("Helvetica", 12), fieldbackground=background_color)

root.configure(background=background_color)

def register_customer():
    custno = custno_entry.get()
    name = name_entry.get()
    addr = addr_entry.get()
    jr_date = jrdate_entry.get()
    source = source_entry.get()
    destination = destination_entry.get()
    
    try:
        sql = 'INSERT INTO pdata(custno, custname, addr, jrdate, source, destination) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (custno, name, addr, jr_date, source, destination)
        mycursor.execute(sql, values)
        mydb.commit()
        messagebox.showinfo("Success", "Customer data inserted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def calculate_ticket_price():
    try:
        cno = int(custno_calc_entry.get())
        class_type = class_type_var.get()
        num_passengers = int(passengers_entry.get())
        luggage_weight = int(luggage_entry.get())

        ticket_price = 0
        if class_type == 1:
            ticket_price = 6000 * num_passengers
        elif class_type == 2:
            ticket_price = 4000 * num_passengers
        elif class_type == 3:
            ticket_price = 2000 * num_passengers
        else:
            messagebox.showerror("Error", "Invalid class type")
            return

        luggage_charge = luggage_weight * 100
        total_price = ticket_price + luggage_charge

        sql = "INSERT INTO tkt (custno, tkt_tot, lug_tot, g_tot) VALUES (%s, %s, %s, %s)"
        values = (cno, ticket_price, luggage_charge, total_price)
        mycursor.execute(sql, values)
        mydb.commit()

        messagebox.showinfo("Success", f"Ticket details inserted successfully. Total Price: {total_price}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_customer_details():
    custno = custno_display_entry.get()
    try:
        sql = "SELECT pdata.custno, pdata.custname, pdata.addr, pdata.source, pdata.destination, tkt.tkt_tot, tkt.lug_tot, tkt.g_tot FROM pdata INNER JOIN tkt ON pdata.custno = tkt.custno AND tkt.custno = %s"
        rl = (custno,)
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        display_text.config(state=tk.NORMAL)
        display_text.delete(1.0, tk.END)
        for x in res:
            display_text.insert(tk.END, f"{x}\n")
        display_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_all_details():
    try:
        sql = "SELECT pdata.custno, pdata.custname, pdata.addr, pdata.source, pdata.destination, tkt.tkt_tot, tkt.lug_tot, tkt.g_tot FROM pdata INNER JOIN tkt ON pdata.custno = tkt.custno"
        mycursor.execute(sql)
        res = mycursor.fetchall()
        display_text.config(state=tk.NORMAL)
        display_text.delete(1.0, tk.END)
        for x in res:
            display_text.insert(tk.END, f"{x}\n")
        display_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def exit_application():
    root.destroy()


# GUI elements
custno_label = ttk.Label(root, text="Customer Number:")
custno_label.grid(row=0, column=0, sticky="w")
custno_entry = ttk.Entry(root)
custno_entry.grid(row=0, column=1, sticky="w")

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=1, column=0, sticky="w")
name_entry = ttk.Entry(root)
name_entry.grid(row=1, column=1, sticky="w")

addr_label = ttk.Label(root, text="Address:")
addr_label.grid(row=2, column=0, sticky="w")
addr_entry = ttk.Entry(root)
addr_entry.grid(row=2, column=1, sticky="w")

jrdate_label = ttk.Label(root, text="Date of Journey (YYYY-MM-DD):")
jrdate_label.grid(row=3, column=0, sticky="w")
jrdate_entry = ttk.Entry(root)
jrdate_entry.grid(row=3, column=1, sticky="w")

source_label = ttk.Label(root, text="Source:")
source_label.grid(row=4, column=0, sticky="w")
source_entry = ttk.Entry(root)
source_entry.grid(row=4, column=1, sticky="w")

destination_label = ttk.Label(root, text="Destination:")
destination_label.grid(row=5, column=0, sticky="w")
destination_entry = ttk.Entry(root)
destination_entry.grid(row=5, column=1, sticky="w")

register_button = ttk.Button(root, text="Register Customer", command=register_customer)
register_button.grid(row=6, column=0, columnspan=2, pady=10)

custno_calc_label = ttk.Label(root, text="Enter Customer Number:")
custno_calc_label.grid(row=7, column=0, sticky="w")
custno_calc_entry = ttk.Entry(root)
custno_calc_entry.grid(row=7, column=1, sticky="w")

class_type_var = tk.IntVar()
class_type_var.set(1)  # Default value

class_type_label = ttk.Label(root, text="Select Class Type:")
class_type_label.grid(row=8, column=0, sticky="w")
class_type_first = ttk.Radiobutton(root, text="First Class (Rs 6000 PN)", variable=class_type_var, value=1)
class_type_first.grid(row=8, column=1, sticky="w")
class_type_business = ttk.Radiobutton(root, text="Business Class (Rs 4000 PN)", variable=class_type_var, value=2)
class_type_business.grid(row=9, column=1, sticky="w")
class_type_economy = ttk.Radiobutton(root, text="Economy Class (Rs 2000 PN)", variable=class_type_var, value=3)
class_type_economy.grid(row=10, column=1, sticky="w")

passengers_label = ttk.Label(root, text="Number of Passengers:")
passengers_label.grid(row=11, column=0, sticky="w")
passengers_entry = ttk.Entry(root)
passengers_entry.grid(row=11, column=1, sticky="w")

luggage_label = ttk.Label(root, text="Luggage Weight (Rs.100 per kg):")
luggage_label.grid(row=12, column=0, sticky="w")
luggage_entry = ttk.Entry(root)
luggage_entry.grid(row=12, column=1, sticky="w")

calculate_button = ttk.Button(root, text="Calculate Ticket Price", command=calculate_ticket_price)
calculate_button.grid(row=13, column=0, columnspan=2, pady=10)

custno_display_label = ttk.Label(root, text="Enter Customer Number:")
custno_display_label.grid(row=14, column=0, sticky="w")
custno_display_entry = ttk.Entry(root)
custno_display_entry.grid(row=14, column=1, sticky="w")

display_button = ttk.Button(root, text="Display Customer Details", command=display_customer_details)
display_button.grid(row=15, column=0, columnspan=2, pady=10)

display_all_button = ttk.Button(root, text="Display All Details", command=display_all_details)
display_all_button.grid(row=16, column=0, columnspan=2, pady=10)

display_text = tk.Text(root, height=15, width=100)
display_text.grid(row=17, column=0, columnspan=2)
display_text.config(state=tk.DISABLED)

exit_button = ttk.Button(root, text="Exit", command=exit_application)
exit_button.grid(row=18, column=0, columnspan=2, pady=10)

root.mainloop()
