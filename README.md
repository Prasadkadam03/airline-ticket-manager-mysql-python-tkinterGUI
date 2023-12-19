# Airline Ticket Booking System

## Overview
The Airline Ticket Booking System is a Python-based application with a Tkinter GUI for managing customer information, flight reservations, and ticket pricing. The system allows users to register customers, calculate ticket prices based on class types and luggage weight, and display detailed customer and ticket information.

## Features
- Register Customer: Input customer details such as customer number, name, address, date of journey, source, and destination.
- Calculate Ticket Price: Calculate ticket prices based on class types (First Class, Business Class, Economy Class) and luggage weight.
- Display Customer Details: Retrieve and display individual customer details based on customer number.
- Display All Details: View a list of all customers along with their ticket information.

## Database Setup
The application uses MySQL as a database backend. Two tables are created:
- pdata Table: Stores customer information (custno, custname, addr, jrdate, source, destination).
- tkt Table: Stores ticket information (custno, tkt_tot, lug_tot, g_tot).

## Dependencies
- Python 3
- MySQL Connector
- Tkinter

## How to Run
1. Make sure you have Python installed on your system.
2. Install the required dependencies using `pip install mysql-connector-python`.
3. Execute the script `airline_ticket_system.py` to run the application.

## Usage
1. Run the application.
2. Use the provided GUI to register customers, calculate ticket prices, and display customer details.
3. Exit the application when done.

## Working Video


https://github.com/Prasadkadam03/airline-ticket-manager-mysql-python-tkinterGUI/assets/125743357/cc64aaa3-29c6-4829-9b62-d8dbbed42c88



