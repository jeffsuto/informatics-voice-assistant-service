from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def schedule(registration_type, practicum="", nbi=""):
    if registration_type:
        if registration_type.startswith("pendaftaran"):
            registration_type = registration_type[len("pendaftaran "):]

    req = ""
    if practicum:
        if nbi[:2] in "46" or (nbi[:5] in ["14614", "14615"]):
            if practicum == "Pengembangan Teknologi Website":
                practicum = "Pemrogaman Web"
        elif practicum == "Sistem Jaringan Komputer":
            practicum = "Manajemen Jaringan Komputer"

        if not registration_type:
            registration_type = "praktikum"
        
        registration_type = registration_type+" "+practicum
        req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/schedules/registration?type={registration_type}")
    else:
        req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/schedules/registration?type={registration_type}")
    
    result = req.json()
    data = result['data']
    code = result['code']

    response = ""
    if code == 200:
        response = {
            "text": f"Pendaftaran {registration_type} dibuka tanggal {data['start']} sampai {data['end']}",
            "data": data,
            "code": code,
            "intent": "registration_schedule"
        }
    else:
        response = {
            "text": f"Mohon maaf, saya tidak menemukan jadwal pendaftaran {registration_type}. sepertinya pendaftaran masih belum dibuka",
            "data": data,
            "code": code,
            "intent": "registration_schedule"
        }

    return response