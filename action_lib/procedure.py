from dotenv import load_dotenv
load_dotenv()
import os
import requests
import json

def get(procedure_type):
    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/procedure?type={procedure_type}")
    result = req.json()
    data = result['data']
    code = result['code']

    response = ""
    if code == 200:
        response = {
            "text": f"Berikut ini prosedur {procedure_type}",
            "data": data,
            "code": code,
            "intent": "procedure"
        }
    else:
        response = {
            "text": f"Mohon maaf, prosedur {procedure_type} tidak ditemukan. Untuk informasi lebih lanjut, silahkan tanya kepada pihak loket fakultas",
            "data": data,
            "code": code,
            "intent": "procedure"
        }

    return response