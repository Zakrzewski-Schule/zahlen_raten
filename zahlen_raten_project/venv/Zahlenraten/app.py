from flask import Flask
from db import setup_database, Station, Measurement


app=Flask(__name__)

@app.route("/")
def home():
    return "Hallo von Flask auf macOS!"

if __name__ == "__main__":
    engine, session = setup_database()
    app.run(debug=True)