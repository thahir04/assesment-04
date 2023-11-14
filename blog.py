from flask import Flask, render_template, request
import sqlite3

app = Flask(_name_)

# Function to connect to the database
def connect_db():
    return sqlite3.connect('blog.db')

# Route to display blog posts
@app.route('/')
def index():
    # Connect to the database
    conn = connect_db()

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to fetch blog posts
    cur.execute('SELECT * FROM blog_posts')

    # Fetch all results
    posts = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return render_template('index.html', posts=posts)

if _name_ == '_main_':
    app.run(debug=True)