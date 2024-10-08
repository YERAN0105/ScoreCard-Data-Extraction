# from flask import Flask, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# import pandas as pd
# import re
#
# app = Flask(__name__)
#
# # Enable CORS for all routes
# CORS(app)
#
# @app.route('/run-scorecard', methods=['GET'])
# def run_scorecard():
#     # The content of your Jupyter notebook, slightly modified:
#     GOOGLE_API_KEY = "AIzaSyDnio5ITdIdAp0gxV1mEpe_o6igx0RwOxQ"
#
#     genai.configure(api_key=GOOGLE_API_KEY)
#
#     # Code for interacting with Generative AI and getting data...
#     sample_file = genai.upload_file(path="4wb26jnia7gc1.jpeg",
#                                     display_name="Jetpack drawing")
#
#     # Assume content is retrieved here...
#     model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
#     # Prompt the model with text and the previously uploaded image.
#     response = model.generate_content([sample_file,
#                                        "I want each batsman name, 4s, 6s, balls faced and total runs in this exact format, name '\n' 4s: '\n' 6s: '\n' ballsFaced: '\n' totalRuns: '\n'. Don't use single or double quotation marks."])
#     text = response.text
#     text = text.replace(" ", "")
#
#     # Define regex to capture the player data
#     pattern = re.compile(
#         r'(?P<name>[A-Za-z.]+)\n4s:(?P<fours>\d*)\n6s:(?P<sixes>\d*)\nballsFaced:(?P<balls_faced>\d*)\ntotalRuns:(?P<total_runs>\d*)')
#
#     # Find all matches in the text
#     matches = pattern.findall(text)
#     # Create a DataFrame from the matches
#     df_batsman_info = pd.DataFrame(matches, columns=['name', 'fours', 'sixes', 'balls_faced', 'total_runs'])
#
#     # Convert columns to appropriate data types
#     df_batsman_info['fours'] = pd.to_numeric(df_batsman_info['fours'], errors='coerce').fillna(0).astype(int)
#     df_batsman_info['sixes'] = pd.to_numeric(df_batsman_info['sixes'], errors='coerce').fillna(0).astype(int)
#     df_batsman_info['balls_faced'] = pd.to_numeric(df_batsman_info['balls_faced'], errors='coerce').fillna(0).astype(
#         int)
#     df_batsman_info['total_runs'] = pd.to_numeric(df_batsman_info['total_runs'], errors='coerce').fillna(0).astype(int)
#
#     print(df_batsman_info)
#
#
#
#     # Convert DataFrame to JSON and return as a response
#     return jsonify(df_batsman_info.to_dict(orient="records"))
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# import pandas as pd
# import re
# import os
#
# app = Flask(__name__)
#
# # Enable CORS for all routes
# CORS(app)
#
# # Set the Google API key
# GOOGLE_API_KEY = "AIzaSyDnio5ITdIdAp0gxV1mEpe_o6igx0RwOxQ"
# genai.configure(api_key=GOOGLE_API_KEY)
#
#
# @app.route('/run-scorecard', methods=['POST'])
# def run_scorecard():
#     # Check if the request contains a file
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
#
#     file = request.files['file']
#
#     # Save the file temporarily
#     file_path = os.path.join("uploads", file.filename)
#     file.save(file_path)
#
#     # Upload the file to Generative AI (Google Gemini)
#     sample_file = genai.upload_file(path=file_path, display_name="Uploaded Scorecard")
#
#     # Use Generative AI to extract data
#     model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
#     response = model.generate_content([sample_file,
#                                        "I want each batsman name, 4s, 6s, balls faced and total runs in this exact format, name '\n' 4s: '\n' 6s: '\n' ballsFaced: '\n' totalRuns: '\n'. Don't use single or double quotation marks."])
#
#     # Process the text response
#     text = response.text.replace(" ", "")
#
#     # Define regex to capture the player data
#     pattern = re.compile(
#         r'(?P<name>[A-Za-z.]+)\n4s:(?P<fours>\d*)\n6s:(?P<sixes>\d*)\nballsFaced:(?P<balls_faced>\d*)\ntotalRuns:(?P<total_runs>\d*)')
#
#     # Find all matches in the text
#     matches = pattern.findall(text)
#
#     # Create a DataFrame from the matches
#     df_batsman_info = pd.DataFrame(matches, columns=['name', 'fours', 'sixes', 'balls_faced', 'total_runs'])
#
#     # Convert columns to appropriate data types
#     df_batsman_info['fours'] = pd.to_numeric(df_batsman_info['fours'], errors='coerce').fillna(0).astype(int)
#     df_batsman_info['sixes'] = pd.to_numeric(df_batsman_info['sixes'], errors='coerce').fillna(0).astype(int)
#     df_batsman_info['balls_faced'] = pd.to_numeric(df_batsman_info['balls_faced'], errors='coerce').fillna(0).astype(
#         int)
#     df_batsman_info['total_runs'] = pd.to_numeric(df_batsman_info['total_runs'], errors='coerce').fillna(0).astype(int)
#
#     # Clean up: Remove the uploaded file
#     os.remove(file_path)
#
#     # Convert DataFrame to JSON and return as a response
#     return jsonify(df_batsman_info.to_dict(orient="records"))
#
#
# if __name__ == "__main__":
#     # Create uploads folder if it doesn't exist
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import pandas as pd
import re
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Set the Google API key
GOOGLE_API_KEY = "AIzaSyDnio5ITdIdAp0gxV1mEpe_o6igx0RwOxQ"
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/run-scorecard', methods=['POST'])
def run_scorecard():
    # Check if both 'batsman_file' and 'bowler_file' are in the request
    if 'batsman_file' not in request.files or 'bowler_file' not in request.files:
        return jsonify({'error': 'Both batsman and bowler files are required'}), 400

    batsman_file = request.files['batsman_file']
    bowler_file = request.files['bowler_file']

    # Save both files temporarily
    batsman_path = os.path.join("uploads", batsman_file.filename)
    bowler_path = os.path.join("uploads", bowler_file.filename)
    batsman_file.save(batsman_path)
    bowler_file.save(bowler_path)

    # **Process batsman image**
    batsman_sample_file = genai.upload_file(path=batsman_path, display_name="Batsman Scorecard")
    batsman_model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    batsman_response = batsman_model.generate_content([batsman_sample_file,
        "I want each batsman name, 4s, 6s, balls faced and total runs in this exact format, name '\n' 4s: '\n' 6s: '\n' ballsFaced: '\n' totalRuns: '\n'. Don't use single or double quotation marks."])

    batsman_text = batsman_response.text.replace(" ", "")
    batsman_pattern = re.compile(
        r'(?P<name>[A-Za-z.]+)\n4s:(?P<fours>\d*)\n6s:(?P<sixes>\d*)\nballsFaced:(?P<balls_faced>\d*)\ntotalRuns:(?P<total_runs>\d*)')
    batsman_matches = batsman_pattern.findall(batsman_text)
    df_batsman_info = pd.DataFrame(batsman_matches, columns=['name', 'fours', 'sixes', 'balls_faced', 'total_runs'])

    df_batsman_info['fours'] = pd.to_numeric(df_batsman_info['fours'], errors='coerce').fillna(0).astype(int)
    df_batsman_info['sixes'] = pd.to_numeric(df_batsman_info['sixes'], errors='coerce').fillna(0).astype(int)
    df_batsman_info['balls_faced'] = pd.to_numeric(df_batsman_info['balls_faced'], errors='coerce').fillna(0).astype(int)
    df_batsman_info['total_runs'] = pd.to_numeric(df_batsman_info['total_runs'], errors='coerce').fillna(0).astype(int)

    # **Process bowler image**
    bowler_sample_file = genai.upload_file(path=bowler_path, display_name="Bowler Scorecard")
    bowler_model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    bowler_response = bowler_model.generate_content([bowler_sample_file,
        "I want each bowler name, overs, runs and wickets in this exact format, name '\n' overs: '\n' runs: '\n' wickets: '\n'. Don't use single or double quotation marks."])

    bowler_text = bowler_response.text.replace(" ", "")
    bowler_pattern = re.compile(r'(?P<name>[A-Za-z.]+)\novers:(?P<overs>\d*)\nruns:(?P<runs>\d*)\nwickets:(?P<wickets>\d*)')
    bowler_matches = bowler_pattern.findall(bowler_text)
    df_bowler_info = pd.DataFrame(bowler_matches, columns=['name', 'overs', 'runs', 'wickets'])

    df_bowler_info['overs'] = pd.to_numeric(df_bowler_info['overs'], errors='coerce').fillna(0).astype(int)
    df_bowler_info['runs'] = pd.to_numeric(df_bowler_info['runs'], errors='coerce').fillna(0).astype(int)
    df_bowler_info['wickets'] = pd.to_numeric(df_bowler_info['wickets'], errors='coerce').fillna(0).astype(int)

    # **Merge batsman and bowler data**
    df = pd.merge(df_batsman_info, df_bowler_info, on='name', how='outer')


    # Convert columns to appropriate data types, replacing NaN with 0 or a suitable default
    df['fours'] = pd.to_numeric(df['fours'], errors='coerce').fillna(0).astype(int)
    df['sixes'] = pd.to_numeric(df['sixes'], errors='coerce').fillna(0).astype(int)
    df['balls_faced'] = pd.to_numeric(df['balls_faced'], errors='coerce').fillna(0).astype(
        int)
    df['total_runs'] = pd.to_numeric(df['total_runs'], errors='coerce').fillna(0).astype(int)

    df['overs'] = pd.to_numeric(df['overs'], errors='coerce').fillna(0).astype(int)
    df['runs'] = pd.to_numeric(df['runs'], errors='coerce').fillna(0).astype(int)
    df['wickets'] = pd.to_numeric(df['wickets'], errors='coerce').fillna(0).astype(int)

    # Clean up: Remove the uploaded files
    os.remove(batsman_path)
    os.remove(bowler_path)
    print(df)

    # Convert DataFrame to JSON and return as a response
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    # Create uploads folder if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
