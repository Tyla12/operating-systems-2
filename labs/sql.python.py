import mysql.connector

# Function to connect to the MySQL database and fetch all records from the "students" table
def fetch_student_records(host, user, password, database):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            # Query to select all records from the "students" table
            query = "SELECT * FROM students"

            # Execute the query
            cursor.execute(query)

            # Fetch all records as a list of tuples
            records = cursor.fetchall()

            # Fetch column names
            column_names = [description[0] for description in cursor.description]

            return column_names, records

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    # Replace with your MySQL database credentials
    host = "your_host"
    user = "your_user"
    password = "your_password"
    database = "your_database"

    column_names, student_records = fetch_student_records(host, user, password, database)

    if student_records:
        print("Column Names:", column_names)
        print("Student Records:")
        for record in student_records:
            print(record)
