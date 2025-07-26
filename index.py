from flask import Flask, render_template, request, session
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',        # Default password for root in XAMPP is empty
            database='nts_db'   # Replace with your database name
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor to perform database operations
            cursor = connection.cursor()

            # Fetch data
            cursor.execute("SELECT * FROM student_info")
            user = cursor.fetchone()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
    return user
    

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/st_login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['st_name']
        password = request.form['st_pass']
        user = connect_to_database()
        user



    




if __name__ == "__main__":
    app.run(debug=True)