# This is another example to create Restful API with python Flask framework
# pip install db-sqlite3
# pip install flask
# pip install flask-cors

import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

# Define a web app with Flask
app = Flask(__name__)

######################################################################
# PART 1: Create or connect a database: Users.DB
######################################################################
# Define a function to create a new database: Users.DB
def connect_to_db():
    conn = sqlite3.connect("Users.DB")
    return conn

# Define a function to cerate a DB table: users
def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
            """
        )
        conn.commit()
        print("The users table is created or connected successfully!")
    except:
        print("The users table creation is failed!")
    finally:
        conn.close()


# let's call the function to create the database and table
create_db_table()


# define the get user by id
def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id, ))
        row = cursor.fetchone()
        # convert row object into a dictionary
        user['user_id'] = row['user_id']
        user['name'] = row['name']
        user['email'] = row['email']
        user['phone'] = row['phone']
        user['address'] = row['address']
        user['country'] = row['country']
    except:
        user = {}
    finally:
        conn.close()
    
    return user

# Let's define a function to insert the data into the DB table
def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)
            """, (user['name'], user['email'], user['phone'], user['address'], user['country'])
        )
        conn.commit()
        inserted_user = get_user_by_id(cursor.lastrowid)
    except:
        conn.rollback()
    finally:
        conn.close()

    return inserted_user


# define a funtion to get all users
def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        for i in rows:
            user = {}
            user['user_Id'] = i['user_id']
            user['name'] = i['name']
            user['email'] = i['email']
            user['phone'] = i['phone']
            user['address'] = i['address']
            user['country'] = i['country']
            users.append(user)

    except:
        users = []
    finally:
        conn.close()

    return users


# define a function to update a user
def update_user(user_id, user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users SET name=?, email=?, phone=?, address=?, country=? WHERE user_id = ?
            """, (user['name'], user['email'], user['phone'], user['address'], user['country'],user_id)
        )
        conn.commit()
        updated_user = get_user_by_id(user_id)
    except Exception as e:
        conn.rollback()
        print(f"Error updating user: {e}")
    finally:
        conn.close()

    return updated_user


######################################################################
# PART 2: Create some dataset and insert the data into the DB table
######################################################################
users = []

user1 = {
    "name": "David C. Li",
    "email": "davidli@mail.mcu.edu.tw",
    "phone": "09888888888",
    "address": "XinYi Road No. 5",
    "country": "Taiwan"
}

user2 = {
    "name": "Peter Wang",
    "email": "peterwang@mail.mcu.edu.tw",
    "phone": "097777777777",
    "address": "XinYi Road No. 1",
    "country": "Vietnam"
}

user3 = {
    "name": "Alice Chang",
    "email": "alicechang@mail.mcu.edu.tw",
    "phone": "0955555555555",
    "address": "XinYi Road No. 3",
    "country": "China"
}

user4 = {
    "name": "Richard Liu",
    "email": "richardliu@mail.mcu.edu.tw",
    "phone": "098954122123",
    "address": "XinYi Road No. 9",
    "country": "USA"
}


user5 = {
    "name": "Lynn Lee",
    "email": "lynnlee@mail.mcu.edu.tw",
    "phone": "04653202023323",
    "address": "XinYi Road No. 10",
    "country": "Taiwan"
}

users.append(user1)
users.append(user2)
users.append(user3)
users.append(user4)
users.append(user5)

# call the function insert_user() to insert all users into the DB table
for i in users:
    print(insert_user(i))

print()


######################################################################
# PART 3: Create some RESTful API to manage the DB and tables
######################################################################
CORS(app, resources={r"/*": {"origins": "*"}})

# API 1: get a user by user_id
@app.route('/users/<int:user_id>', methods=['GET'])
def api_get_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))


# API 2: get all users
@app.route('/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

# API 3: Create a new user
@app.route('/users', methods=['POST'])
def api_create_users():
    user = request.get_json()
    return jsonify(insert_user(user))


# API 4: update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def api_update_users(user_id):
    user = request.get_json()
    return jsonify(update_user(user_id, user))

# main entry to run the web app
if __name__ == "__main__":
    app.run(debug=True)
