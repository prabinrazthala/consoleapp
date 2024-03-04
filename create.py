from estd_connection import estd_connection
cursor = estd_connection()
def create_student():
    id = input("Enter id of the student ")
    name = input("Enter student name ")
    age = input("Enter student age ")
    address = input("Enter student address ")
    sql = f"""
    INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', {age}, '{address}')
"""

    cursor.execute(sql)

    print("Student added successfully !!")
    want_to_continue = input("Do you want to continue? (y/n)")
    return True if want_to_continue.lower() == 'y' else False
