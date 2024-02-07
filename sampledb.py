import mysql.connector
from mysql.connector import errorcode

# db config
mydbconfig = {
    'host': '****(host_name)',
    'user': '****(username)',
    'password': '****(password)',
    'database': '*****(db_name)',
    'raise_on_warnings': True
}

# method to create table
def create_table(cursor):
    cursor.execute( """
        CREATE TABLE Register (
            ID INT PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR(50) NOT NULL,
            Email VARCHAR(255) NOT NULL,
            DateOfBirth DATE,
            MobileNo. BIGINT NOT NULL );
            """ )

# C - new record creation
def create_registration(cursor, name, email, date_of_birth, mobile):
    cursor.execute( """
        INSERT INTO Register (Name, Email, DateOfBirth, MobileNo.)
        VALUES (%s, %s, %s, %s); """, 
        (name, email, date_of_birth, mobile) )

# R - read record by ID
def read_registration(cursor, registration_id):
    cursor.execute( """
        SELECT * FROM Register
        WHERE ID = %s;
    """, (registration_id,))
    result = cursor.fetchone()
    return result

# U - update record by ID
def update_registration(cursor, registration_id, name, email, date_of_birth):
    cursor.execute( """
        UPDATE Register
        SET Name = %s, Email = %s, DateOfBirth = %s, MobileNo. = %s
        WHERE ID = %s;
    """, (name, email, date_of_birth,MobileNo., registration_id) )

# D - delete record by ID
def delete_registration(cursor, registration_id):
    delete_query = """
        DELETE FROM Register
        WHERE ID = %s;
    """
    cursor.execute(delete_query, (registration_id,))

# display all records
def display_all_registrations(cursor):
    cursor.execute( """
        SELECT * FROM Register;
    """ )
    results = cursor.fetchall()
    for result in results:
        print(result)

# Main block
try:
    connection = mysql.connector.connect(**mydbconfig)
    cursor = connection.cursor()
    create_registration_table(cursor)
    
    create_registration(cursor, "John Doe", "john.doe@example.com", "1990-01-01")

    # Retrieve record
    registration_info = read_registration(cursor, ID) # you can replace with any ID
    print(registration_info)
    # Update the registration record
    update_registration(cursor, ID, "Updated Name", "updated@example.com", "Some date", UpdatedMobileNum)

    print("\nAll Registration Records:")
    display_all_registrations(cursor)
    # Delete the registration record
    delete_registration(cursor, ID)  # replace ID
    
    connection.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error Check credentials.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error Database not exist.")
    else:
        print(f"Error: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
