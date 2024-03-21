# Standard library imports
import json 
# Remote library imports
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

'''
@app.route('/data', methods=['GET'])
def all_data():
    try:
        with open('db.json') as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "data not found"}), 404

'''
'''
# Define route to serve data
@app.route('/postcode', methods=['GET'])
def get_data():
    try:
        # Load data from JSON file
        with open('db.json') as f:
            data = json.load(f)
        
        # Extract required data for the chart (postcode and total_units)
        chart_data = []
        for entry in data['hpd']:
            if 'total_units' in entry:
                chart_data.append({'postcode': entry['postcode'], 'total_units': int(entry['total_units'])})
        
        # Return data as JSON
        return jsonify(chart_data), 200
    except FileNotFoundError:
        return jsonify({"error": "data not found"}), 404
'''

# Define route to serve data
@app.route('/postcode', methods=['GET'])
def get_postcode_totals():
    try:
        # Load data from JSON file
        with open('db.json') as f:
            data = json.load(f)
        
        # Create a dictionary to store total units for each postcode
        postcode_totals = {}
        for entry in data['hpd']:
            if 'total_units' in entry and 'postcode' in entry:
                postcode = entry['postcode']
                total_units = int(entry['total_units'])
                # If the postcode already exists in the dictionary, add the total units to it
                if postcode in postcode_totals:
                    postcode_totals[postcode] += total_units
                # If the postcode is not in the dictionary, initialize it with the total units
                else:
                    postcode_totals[postcode] = total_units
        
        # Convert the dictionary into a list of dictionaries
        chart_data = [{'postcode': postcode, 'total_units': total_units} for postcode, total_units in postcode_totals.items()]
        
        # Return data as JSON
        return jsonify(chart_data), 200
    except FileNotFoundError:
        return jsonify({"error": "data not found"}), 404


# Define route to serve data
@app.route('/borough', methods=['GET'])
def get_borough_totals():
    try:
        # Load data from JSON file
        with open('db.json') as f:
            data = json.load(f)
        
        # Create a dictionary to store total units for each borough
        borough_totals = {}
        for entry in data['hpd']:
            if 'total_units' in entry and 'borough' in entry:
                borough = entry['borough']
                total_units = int(entry['total_units'])
                # If the postcode already exists in the dictionary, add the total units to it
                if borough in borough_totals:
                    borough_totals[borough] += total_units
                # If the postcode is not in the dictionary, initialize it with the total units
                else:
                    borough_totals[borough] = total_units
        
        # Convert the dictionary into a list of dictionaries
        chart_data = [{'borough': borough, 'total_units': total_units} for borough, total_units in borough_totals.items()]
        
        # Return data as JSON
        return jsonify(chart_data), 200
    except FileNotFoundError:
        return jsonify({"error": "data not found"}), 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)