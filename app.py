# app.py

from flask import Flask, jsonify

app = Flask(__name__)

# Sample patient data
patients = [
    {"id": 1, "name": "John Doe", "age": 30, "gender": "Male"},
    {"id": 2, "name": "Jane Smith", "age": 25, "gender": "Female"},
    {"id": 3, "name": "Vera John", "age": 23, "gender": "Female"},
    # Add more patient information as needed
]

@app.route('/')
def home():
    return 'Health Data API is up and running!'

@app.route('/patients', methods=['GET'])
def get_all_patients():
    return jsonify({"patients": patients})

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = next((p for p in patients if p['id'] == patient_id), None)
    if patient:
        return jsonify({"patient": patient})
    return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
