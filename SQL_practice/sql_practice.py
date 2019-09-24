
import sqlite3
from employee import Employee
# SQLite
# we want an app -> create, update, delete employees
# we have connected file and db, created a db
conn = sqlite3.connect('employee.db')

# middlestuff between db and file. It is a python obj that represents the table
c = conn.cursor()

# run an SQL command
# c.execute("""CREATE TABLE employees (
#              first text,
#              last text,
#              pay integer
#              )""")
# to create a table
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
# print(emp_1.first)

# c.execute("INSERT INTO employees VALUES (?, ?, ?)",
#           (emp_2.first, emp_2.last, emp_2.pay))
# # execute SQL code

# # recommended -> c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
# #      {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})

# #c.execute("SELECT * from employees WHERE last='Ivannikov'")
# c.execute("SELECT * from employees WHERE last='Doe' or last ='Ivanniko'")
# print(c.fetchall())
# conn.close()
# # fetchone() get 1 value, fetchmany(n) -> get n records, fetchall() - get all
# conn.commit()
# # commit the changes may be seen as refresh (?) in PSequel


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def remove_emp(emp):
    with conn:
        c.execute("""DELETE from employees
                  WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})


# now we can do it properly
# insert_emp(emp_1)
# insert_emp(emp_2)

emps = get_emps_by_name('Doe')

update_pay(emp_2, 92000)
remove_emp(emp_1)
remove_emp(emp_2)
print(emps)

conn.close()
