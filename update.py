from estd_connection import estd_connection

cursor = estd_connection()





def update_student():
    id = input("Enter student ID")
    to_change = input("Enter the data you want to change ")
    changed_value = input(f"Enter new {to_change} ")
    sql = f"""UPDATE STUDENT SET {to_change}='{changed_value}' WHERE ID='{id}'"""
    cursor.execute(sql)


    print("Student Updated Successfully")
    want_to_continue = input("Do you want to continue? (y/n)")
    return True if want_to_continue.lower() == 'y' else False
