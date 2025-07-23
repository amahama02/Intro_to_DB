import mysql.connector

# --- Database connection details ---
# REPLACE 'yourusername' and 'yourpassword' with your actual MySQL credentials.
# The 'database' parameter is NOT specified here because we are creating the database itself.
# We first connect to the MySQL server without specifying an existing database.
DB_HOST = "localhost"
DB_USER = "yourusername"
DB_PASSWORD = "yourpassword"
DB_NAME = "alx_book_store"

# --- Main logic ---
def create_alx_book_store_database():
    cnx = None  # Initialize connection object to None
    cursor = None # Initialize cursor object to None
    try:
        # 1. Attempt to establish a connection to the MySQL server
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        if cnx.is_connected():
            print(f"Successfully connected to MySQL server. Attempting to create database '{DB_NAME}'.")

            # 2. Create a cursor object. The cursor allows us to execute SQL commands.
            cursor = cnx.cursor()

            # 3. Execute the SQL command to create the database.
            #    Using 'IF NOT EXISTS' is crucial to prevent the script from failing
            #    if the database already exists, as per requirements.
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
            cursor.execute(create_db_query)

            # 4. Commit the changes. This is necessary to apply the database creation.
            cnx.commit()

            # 5. Print the required success message.
            # Note: Due to the "no SELECT/SHOW" constraint, we cannot definitively
            # know if it was *just created* or *already existed*. We assume success.
            print(f"Database '{DB_NAME}' created successfully!")


    except mysql.connector.Error as err:
        # 6. Handle specific MySQL connection or query execution errors.
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Authentication failed. Please check your MySQL username or password.")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            # This error is less likely here as we don't specify a database initially
            print(f"Error: The specified database '{DB_NAME}' does not exist or is not accessible.")
        else:
            print(f"An unexpected error occurred: {err}")
    finally:
        # 7. Close the cursor and the connection. This is vital to release server resources.
        if cursor:
            cursor.close()
            # print("Cursor closed.") # Uncomment for debugging
        if cnx and cnx.is_connected():
            cnx.close()
            # print("MySQL connection closed.") # Uncomment for debugging

# --- Call the function to run the script when executed directly ---
if __name__ == "__main__":
    create_alx_book_store_database()