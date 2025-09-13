from flask import Flask, jsonify,request, render_template
import mysql.connector 

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'app_user',
    'password': 'StrongPassword123!',
    'database': 'user_management'
}
@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/signup', methods=['POST'])
def show_register_form():
    return render_template('about.html')
@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')
@app.route('/employee',methods=['GET'])
def employee(): 
    return render_template('employee.html')
@app.route('/index', methods=['POST'])
def about():
    return render_template('about.html')
@app.route('/about', methods=['GET'])
def about1():
    return render_template('about.html')
@app.route('/employeedetails', methods=['GET'])
def employeedetails():
    return render_template('employeedetails.html')
@app.route('/get_users')
def get_users():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)  # To get results as dictionaries

        # Execute query
        cursor.execute("SELECT * FROM users")  # Replace 'users' with your actual table name
        users = cursor.fetchall()

        # Close connection
        cursor.close()
        conn.close()

        if not users:
            return jsonify({"message": "No users found"}), 404

        # Remove passwords before sending response
        for user in users:
            user.pop('password', None)

        return jsonify(users)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


if __name__ == '__main__':
    app.run(debug=True)
