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

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    new_patient = Patient(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient created successfully"})

@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    data = request.json
    patient.name = data['name']
    patient.age = data['age']
    patient.gender = data['gender']
    db.session.commit()

    return jsonify({"message": "Patient updated successfully"})

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()

    return jsonify({"message": "Patient deleted successfully"})
