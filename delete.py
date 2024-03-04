from estd_connection import estd_connection
cursor = estd_connection()

def delete_student():
    
    id = input("Enter student ID ")
    sql = f"""DELETE FROM STUDENT WHERE ID='{id}'"""
    cursor.execute(sql)

    print("Student deleted successfully !!")
    want_to_continue = input("Do you want to continue? (y/n)")
    return True if want_to_continue.lower() == 'y' else False

