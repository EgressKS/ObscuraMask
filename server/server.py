from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS
from pathlib import Path

from controller.csvhandler_controller import mask_obfuscate_csv, getcsvheader


# Configure upload and secured files directories
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'temp_uploads')
SECURED_FILES_FOLDER = os.path.join(BASE_DIR, 'secured_files')

# Ensure both directories exist
for folder in [UPLOAD_FOLDER, SECURED_FILES_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECURED_FILES_FOLDER'] = SECURED_FILES_FOLDER

# csv routes
@app.route("/getcsvheader", methods=['POST'])
def get_csv_header_route():
    return getcsvheader()

@app.route("/maskobfcsv", methods=['POST'])
def mask_csv_route():
    return mask_obfuscate_csv()



if __name__ == "__main__":
    app.run(debug=True)