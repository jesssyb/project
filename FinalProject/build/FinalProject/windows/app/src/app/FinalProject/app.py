"""
Final project for CS50x
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import sqlite3
import os


class FinalProject(toga.App):


    def startup(self):
        
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        con = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "applist.db"))
        cur = con.cursor()

        con.commit()

        cur.execute("SELECT * FROM data")

        self.data = (cur.fetchall())

        con.commit()

        self.table = toga.Table(
            headings=["Item", "Quantity"],
            data = self.data,
            style=Pack(flex=1),
            on_activate=self.clicked)
        

        item_label = toga.Label(
            "Item: ",
            style=Pack(padding=(0, 5))
        )

        self.item_input = toga.TextInput(style=Pack(flex=1))

        item_box = toga.Box(style=Pack(direction=ROW, padding=5))
        item_box.add(item_label)
        item_box.add(self.item_input)

        quantity_label = toga.Label(
            "Quantity: ",
            style=Pack(padding=(0, 5))
        )

        self.quantity_input = toga.NumberInput(style=Pack(flex=1), min = 0)

        quantity_box = toga.Box(style=Pack(direction=ROW, padding=5))
        quantity_box.add(quantity_label)
        quantity_box.add(self.quantity_input)
        
        button = toga.Button(
            "Add",
            on_press=self.addItem,
            style=Pack(padding=5)
        )

        self.main_box.add(item_box)
        self.main_box.add(quantity_box)
        self.main_box.add(button)
        self.main_box.add(self.table)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
    
    
    def addItem(self, widget):

        self.main_box.remove(self.table)

        con = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "applist.db"))
        cur = con.cursor()

        cur.execute("INSERT INTO data (item, quantity) VALUES (?, ?)", (str(self.item_input.value), int(self.quantity_input.value)))

        con.commit()

        cur.execute("SELECT * FROM data")

        self.data = (cur.fetchall())

        con.commit()
    
        self.table = toga.Table(
            headings=["Item", "Quantity"],
            data = self.data,
            style=Pack(flex=1),
            on_activate=self.clicked)

        self.main_box.add(self.table)

        
    def clicked(self, table, row):

        self.main_box.remove(self.table)

        try:

            print("Before",self.data)

            con = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "applist.db"))
            cur = con.cursor()

            con.commit()

            cur.execute("DELETE FROM data WHERE item = (?) AND quantity = (?)", (row.item, row.quantity))

            con.commit()

            cur.execute("SELECT * FROM data")

            self.data = (cur.fetchall())

            print("After",self.data)

            con.commit()

            self.table = toga.Table(
                headings=["Item", "Quantity"],
                data = self.data,
                style=Pack(flex=1),
                on_activate=self.clicked)

        except Exception as e:

            print(e)

        row._source = None
        row.item = ''
        row.quantity = ''

        self.main_box.add(self.table)
        
        
def main():
    return FinalProject()
