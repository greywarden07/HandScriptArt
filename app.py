from flask import Flask, request, send_file, render_template
import subprocess
import os
import uuid
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'out'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

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
        
        try:
            # Run the processing script with timeout
            result = subprocess.run(command, capture_output=True, text=True, timeout=60)
            
            # Check if subprocess failed or returned error
            if result.returncode != 0:
                return f"Processing failed: The image may not contain suitable text or the format is unsupported.", 400
            
            # Check if the subprocess output indicates failure
            if "Could not process image" in result.stdout or "high <= 0" in result.stdout:
                return "Processing failed: The image may not contain suitable text for handwriting conversion.", 400
            
            # Check if processed file actually exists
            if not os.path.exists(processed_path):
                return "Processing completed but output file was not generated.", 500
            
            # Return success response with download link
            return f'''
            <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
                <h2>✅ Processing Complete!</h2>
                <p>Your handwritten-style image has been generated successfully.</p>
                <a href="/download/{processed_filename}" 
                   style="display: inline-block; background: #4CAF50; color: white; 
                          padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px;">
                    📥 Download Processed Image
                </a>
                <br><br>
                <a href="/" style="color: #007bff;">← Process Another Image</a>
            </div>
            '''
            
        except subprocess.TimeoutExpired:
            return "Processing timeout: The image took too long to process.", 500
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}", 500
        finally:
            # Clean up uploaded file
            try:
                if os.path.exists(upload_path):
                    os.remove(upload_path)
            except Exception as e:
                print(f"Could not remove uploaded file: {e}")

    return "Invalid file type. Please upload a PNG, JPG, or JPEG image.", 400

@app.route('/download/<filename>')
def download_file(filename):
    """Serve processed files for download"""
    file_path = os.path.join(PROCESSED_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

@app.route('/out/<filename>')
def serve_processed_file(filename):
    """Serve processed files for viewing"""
    file_path = os.path.join(PROCESSED_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "File not found", 404

if __name__ == '__main__':
    # Use environment variables for production
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host=host, port=port, debug=debug)
