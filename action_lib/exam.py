from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def schedule(nbi, exam):
    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/schedules/exam?nbi={nbi}&type={exam}")
    result = req.json()
    data = result['data']
    code = result['code']

    response = ""
    if code == 200:
        response = {
            "text": f"Berikut ini jadwal {exam.upper()} sesuai dengan mata kuliah anda",
            "data": data,
            "code": code,
            "intent": "exam_schedule"
        }
    else:
        response = {
            "text": f"Mohon maaf, saya tidak menemukan jadwal {exam.upper()} anda",
            "data": data,
            "code": code,
            "intent": "exam_schedule"
        }

    return response