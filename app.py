from flask import Flask, render_template
from routes.trip_routes import trip_bp
from config import Config
import mysql.connector

app = Flask(__name__)
app.config.from_object(Config)

# Setup MySQL connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DATABASE']
    )
    return conn

# Home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Register the trip routes for the API
app.register_blueprint(trip_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
