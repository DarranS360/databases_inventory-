import sqlite3

#connect to database
conn = sqlite3.connect('database.db')

#create a cursor
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
    )
    """)

except sqlite3.OperationalError:
    print("Table already exists")

try:
    cursor.execute("""
    INSERT INTO python_programming (id, name, grade)
    VALUES (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
    """)

except sqlite3.Error as e:
    print("Error inserting data: ", e)

# Selecting records with grades between 60 and 80 and printing them
try:
    cursor.execute("""
    SELECT * FROM python_programming
    WHERE grade BETWEEN 60 AND 80
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Error selecting data: ", e)

# Update Carl Davis's grade to 65
try:
    cursor.execute("""
    UPDATE python_programming
    SET grade = 65
    WHERE name = 'Carl Davis'
    """)
except sqlite3.Error as e:
    print("Error updating data: ", e)

# Delete Dennis Fredrickson's row
try:
    cursor.execute("""
    DELETE FROM python_programming
    WHERE name = 'Dennis Fredrickson'
    """)
except sqlite3.Error as e:
    print("Error deleting data: ", e)

#Update the grade of all people with an id below 55
try:
    cursor.execute("""
    UPDATE python_programming
    SET grade = grade + 5
    WHERE id < 55
    """)
except sqlite3.Error as e:
    print("Error updating data: ", e)


conn.commit()

conn.close()
