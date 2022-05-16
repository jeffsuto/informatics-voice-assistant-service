from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def schedule(nbi, trial_type=""):
    if not trial_type:
        trial_type = ""
    
    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/schedules/trial?type={trial_type}&nbi={nbi}")
    result = req.json()
    data = result['data']
    code = result['code']

    text = ""
    if code == 200:
        if trial_type:
            text = f"Berikut ini jadwal sidang {trial_type} anda"
        else:
            text = f"Berikut ini jadwal sidang anda"
    else:
        if trial_type:
            text = f"mohon maaf, saya tidak menemukan jadwal sidang {trial_type} anda. silahkan hubungi koordinator {trial_type}"
        else:
            text = f"mohon maaf, saya tidak menemukan jadwal sidang anda. Bisa jadi jadwal belum dimasukkan atau anda tidak terdaftar dalam sidang saat ini"

    response = {
        "text": text,
        "data": data,
        "code": code,
        "intent": "trial_schedule"
    }

    return response