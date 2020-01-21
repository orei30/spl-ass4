import sqlite3
import atexit

# Data Transfer Objects:
class Employee:
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand
    def toString(self):
        return "("+ id + ", " + name + ", " + salary + ", " + coffee_stand + ")"

class Supplier:
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information
    def toString(self):
        return "("+ id + ", " + name + ", " + contact_information + ")"

class Product:
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity


class CoffeeStand:
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activity:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

# Data Access Objects:
# All of these are meant to be singletons
class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
               INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
           """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Employees WHERE id = ?
        """, [employee_id])

        return Employee(*c.fetchone())
    
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Employees
        """).fetchall()
 
        return [Employee(*row) for row in all]

class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
               INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
           """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Suppliers WHERE id = ?
        """, [supplier_id])

        return Supplier(*c.fetchone())
    
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Suppliers
        """).fetchall()
 
        return [Supplier(*row) for row in all]

class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
                INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.id, product.description, product.price, product.quantity])

    def find(self, product):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM Products WHERE id = ?
            """, [product.id])

        return Product(*c.fetchone())

    def update(self, product):
        self._conn.execute("""
               UPDATE Products SET quantity=(?) WHERE id=(?)
           """, [product.quantity, product.id])
    
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Products
        """).fetchall()
 
        return [Product(*row) for row in all]

class _CoffeeStands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffeeStand):
        self._conn.execute("""
            INSERT INTO Coffee_stands (id,location, number_of_employees) VALUES (?, ?, ?)
        """, [coffeeStand.id, coffeeStand.location, coffeeStand.number_of_employees])
    
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Coffee_stands
        """).fetchall()
 
        return [CoffeeStand(*row) for row in all]

class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("""
               INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
           """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])
    
    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Activities
        """).fetchall()
 
        return [Activity(*row) for row in all]

#The Repository
class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.employees = _Employees(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.products = _Products(self._conn)
        self.coffeeStands = _CoffeeStands(self._conn)
        self.activities = _Activities(self._conn)
     
    def _close(self):
        self._conn.commit()
        self._conn.close()
     
    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE Suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_information TEXT
        );

        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        );
        
        CREATE TABLE Coffee_stands (
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            number_of_employees INTEGER
        );
            
        CREATE TABLE Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary REAL NOT NULL,
            coffee_stand INTEGER REFERENCES Coffee_stand(id)
        );

        CREATE TABLE Activities (
            product_id INTEGER INTEGER REFERENCES Product(id),
            quantity INTEGER NOT NULL,
            activator_id INTEGER NOT NULL,
            date DATE NOT NULL
        );
    """)

    # def init_tables(self):
    #     with open('config.txt', 'r') as reader:
    #         for line in reader.readlines():
    #             words = line.split(',')
    #             if words[0] == 'C':
    #                 _CoffeeStands.insert(self, CoffeeStand(words[1].strip(), words[2].strip(), words[3].strip()))
    #             if words[0] == 'S':
    #                 _Suppliers.insert(self, Supplier(words[1].strip(), words[2].strip(), words[3].strip()))
    #             if words[0] == 'E':
    #                 _Employees.insert(self, Employee(words[1].strip(), words[2].strip(), words[3].strip(), words[4].strip()))
    #             if words[0] == 'P':
    #                 _Products.insert(self, Product(words[1].strip(), words[2].strip(), words[3].strip(), 0))

# the repository singleton
repo = _Repository()
atexit.register(repo._close)