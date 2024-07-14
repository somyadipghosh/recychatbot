from flask import Flask, request, render_template, Blueprint
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.0-pro-latest')

server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'
static_bp = Blueprint('static', __name__, static_url_path='/static', static_folder='static')
server.register_blueprint(static_bp)

initiate_txt = """You are an ai bot named RecyCraft made by Team codeARC, 
I will send Item names as prompts you will give 3 ways how to recycle it and 
also give youtube links searching from google how to recycle the given item. 
You are not able to do other things except this. 
Tell it is inappropriate if the prompt is inappropriate.
if the prompt is not a garbage then respond accordingly as the prompt.
\nNow recycle this:\n"""

def send_gpt(prompt):
    try:
        response = model.generate_content(initiate_txt + prompt)
        return response
    except Exception as e:
        return {"error": str(e)}

def save_response_to_json(resp):
    # Save the entire response attribute to a JSON file
    with open('response.json', 'w') as json_file:
        json.dump(resp.to_dict(), json_file, indent=4)

def extract_text_from_json():
    try:
        with open('response.json', 'r') as json_file:
            resp_data = json.load(json_file)
        
        text_parts = []
        for candidate in resp_data['candidates']:
            for part in candidate['content']['parts']:
                text_parts.append(part['text'])
        
        return "\n".join(text_parts)
    except Exception as e:
        return {"error": str(e)}

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat3.5.html',
                question="I have nothing to recycle. Provide some of your quotes regarding waste recycling",
                res=quote
            )
        question = request.form['question']
        resp = send_gpt(question)
        
        if isinstance(resp, dict) and "error" in resp:
            res = resp["error"]
        else:
            save_response_to_json(resp)
            res = extract_text_from_json()

        return render_template('chat3.5.html', question=question, res=res)
    return render_template('chat3.5.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5001)
