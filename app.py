from flask import Flask, request, send_file, render_template
from google.cloud import storage
import subprocess
import os
import uuid

app = Flask(__name__)

# Set up Google Cloud Storage client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Your Service Account.json"
storage_client = storage.Client()
bucket_name = 'Your Bucket Name'
bucket = storage_client.bucket(bucket_name)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'out'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def upload_to_gcs(local_file_path, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)
    return blob.public_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return "No file part", 400
    
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    
    if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Save the uploaded file
        upload_filename = f"{uuid.uuid4()}.png"
        upload_path = os.path.join(UPLOAD_FOLDER, upload_filename)
        file.save(upload_path)

        # Define processed image filename
        base_filename = os.path.splitext(upload_filename)[0]
        processed_filename = f"{base_filename}_edited.png"
        processed_path = os.path.join(PROCESSED_FOLDER, processed_filename)
        
        # Process the image
        command = [
            'python', 'writing_artifact.py',
            upload_path,
            '-o', PROCESSED_FOLDER,
            '-f', 'png'
        ]
        
        # Log command for debugging
        print("Running command:", " ".join(command))
        
        # Run the processing script
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Log subprocess output for debugging
        print("Subprocess output:", result.stdout)
        print("Subprocess error:", result.stderr)
        
        # Upload processed file to Google Cloud Storage
        processed_blob_url = upload_to_gcs(processed_path, processed_filename)
        
        # Remove local files
        os.remove(upload_path)
        os.remove(processed_path)
        
        return f'Processed file available at: <a href="{processed_blob_url}">{processed_blob_url}</a>'

    return "Invalid file type", 400

