# #1. Import required library
import psycopg2

# #2. Function to execute SQL scripts
def execute_sql_scripts(filenames):
    """
    Connects to the PostgreSQL database, executes multiple SQL scripts, 
    and handles errors if they occur.
    """
    try:
        # #3. Establish connection to the database with secure credentials
        conn = psycopg2.connect(
            dbname="retail_db",
            user="retail_manager",
            password="secureRetail2024",
            host="localhost",
            port="5433"
        )
        
        cur = conn.cursor()  # #4. Opens a cursor to execute database operations

        for filename in filenames:
            try:
                # #5. Reads the SQL script from the specified file
                with open(filename, 'r') as file:
                    sql_script = file.read()

                # #6. Executes the SQL script
                cur.execute(sql_script)
                
                # #7. Commits changes to the database
                conn.commit()
                print(f"\nSQL script '{filename}' executed successfully!\n")

            except Exception as error:
                # #8. Rolls back changes in case of an error
                conn.rollback()
                print(f"Error executing '{filename}': {error}")

        # #9. Closes the cursor and database connection
        cur.close()
        conn.close()

    except Exception as conn_error:
        print(f"Database connection failed: {conn_error}")

# #10. Executes the SQL scripts for database setup
execute_sql_scripts(['RetailProject-DBSchema.sql'])