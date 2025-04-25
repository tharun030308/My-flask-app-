import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

    # Hardcoding the DATABASE URL directly
DATABASE_URL = "postgresql://messages_z31b_user:SxwLRJE3LZ1N1WTHwrlkqBUUFPjCRnJw@dpg-d05am82li9vc738kiim0-a.oregon-postgres.render.com/messages_z31b"

    # Connect to PostgreSQL database
    
def connect_db():
        conn = psycopg2.connect(DATABASE_URL)
        return conn

    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]

            # Connect to the database and insert data
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO questions (col) VALUES (%s)", (question,))
        conn.commit()
        conn.close()

        return "Your message was submitted"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
