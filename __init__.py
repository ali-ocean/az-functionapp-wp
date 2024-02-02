import json
import os
from flask import Flask, render_template, request
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Parse form data
    student_id = request.form['student_id']
    name = request.form['name']
    course = request.form['course']

    # Azure Storage Account Configuration
    connection_string = "flPUZCqra3HwGV+2Cfg3+PrJ+oeumAiPdb5/FWSccrSVXzHEg9O/57czIX426E+HV8DPHjzoxwz8+ASt8GLP9w=="

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Create a Blob for each student registration
    blob_name = f"{student_id}.json"
    blob_data = json.dumps({'student_id': student_id, 'name': name, 'course': course})
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(blob_data)

    return render_template('success.html', student_id=student_id)

if __name__ == '__main__':
    app.run(debug=True)
