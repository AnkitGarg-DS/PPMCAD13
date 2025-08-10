# Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency 
# and managing infrastructure efficiently.

# ●       The program should read a configuration file (you can provide them with a sample configuration file).
# ●       It should extract specific key-value pairs from the configuration file.
# ●       The program should store the extracted information in a data structure (e.g., dictionary or list).
# ●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
# ●       Finally save the output file data as JSON data in the database.
# ●       Create a GET request to fetch this information.

# Sample Configuration file: 
# [Database]
# host = localhost
# port = 3306
# username = admin
# password = secret

# [Server]
# address = 192.168.0.1
# port = 8080

# Sample Output: 
# Configuration File Parser Results:
# Database:
# - host: localhost
# - port: 3306
# - username: admin
# - password: secret

# Server:
# - address: 192.168.0.1
# - port: 8080
#C:\Users\HP\OneDrive\Desktop\Ankit\Hero Vired\config.ini

import configparser
import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Krishav%4074@localhost/flaskdemo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Configuration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    config_data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Configuration {self.id}>"

def parse_config_file(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        config_data = {}
        for section in config.sections():
            config_data[section] = dict(config.items(section))
        return config_data
    except FileNotFoundError:
        print(f"Configuration file {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the configuration file: {e}")
        return None

def save_config_to_db(config_data):
    try:
        config_json = json.dumps(config_data)
        new_config = Configuration(config_data=config_json)
        db.session.add(new_config)
        db.session.commit()
        print("Configuration data saved to database.")
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")

@app.route('/get_config', methods=['GET'])
def get_config():
    try:
        configurations = Configuration.query.all()
        config_list = []
        for config in configurations:
            config_list.append(json.loads(config.config_data))
        return jsonify(config_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
        config_file_path = r'C:\Users\HP\Git\PPMCAD13\config.ini'  # Path to your configuration file
        config_data = parse_config_file(config_file_path)
        
        if config_data:
            save_config_to_db(config_data)
            print("Configuration File Parser Results:")
            for section, items in config_data.items():
                print(f"{section}:")
                for key, value in items.items():
                    print(f"- {key}: {value}")
    app.run(debug=True)  # Start the Flask application

