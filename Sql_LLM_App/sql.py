# TEXT TO SQL LLM APPLICATION

# PROMPT --> LLM --> GEMINI PRO -> QUERY -> SQL DATABASE -> RESPONSE


# IMPLEMENTATION 
# SQLITE --> INSERTING SOME DATA --> PYTHON PROGRAMMING 
# LLM APPLICATION --> GEMINI PRO --> SQL DATABASE 



import sqlite3


# Connect to sqlite3
connection = sqlite3.connect("student.db")

# Create a cursor that used to insert the records, modify it or delete or performs operation on the database
cursor = connection.cursor()


# create a table 
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

# Execute this query to which will create table student 
cursor.execute(table_info)

# INSERTING SOME MORE RECORDS OF THE STUDENTS

cursor.execute('''INSERT INTO STUDENT VALUES("KRISH","DATA SCIENCE","A+", 96)''') 
cursor.execute('''INSERT INTO STUDENT VALUES("NITISH","ARTIFICIAL INTELLIGENCE","A+", 97)''') 
cursor.execute('''INSERT INTO STUDENT VALUES("HITESH","ARTIFICIAL INTELLIGENCE","A", 94)''') 
cursor.execute('''INSERT INTO STUDENT VALUES("HARKIRAT","COMPUTER SCIENCE","A", 90)''') 



print("The Inserted Records are ")

data = cursor.execute(''' SELECT * FROM STUDENT ''')

for row in data:
    print(row)



# Close the connection
connection.commit()
connection.close()
