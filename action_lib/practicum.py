from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def schedule(nbi, practicum=""):
    response = ""
    if practicum:
        if nbi[:2] in "46" or (nbi[:5] in ["14614", "14615"]):
            if practicum == "Pengembangan Teknologi Website":
                practicum = "Pemrogaman Web"
            elif practicum == "Sistem Jaringan Komputer":
                practicum = "Manajemen Jaringan Komputer"
        
        req = requests.get(os.getenv('SILAB_BASE_URL')+f"api/v1/jadwal/praktikum?praktikum={practicum}&nbi={nbi}")
        result = req.json()
        data = result['data']
        code = result['code']

        if code == 200:
            response = {
                "text": f"berikut ini jadwal praktikum {practicum} anda",
                "data": data,
                "intent": "practicum_schedule"
            }
        else:
            response = {
                "text": f"Mohon maaf, jadwal praktikum {practicum} anda tidak ditemukan. silahkan menemui asisten laboratorium yang bersangkutan",
                "data": data,
                "intent": "practicum_schedule"
            }
    else:
        req = requests.get(os.getenv('SILAB_BASE_URL')+f"api/v1/jadwal/praktikum?nbi={nbi}")
        result = req.json()
        data = result['data']
        code = result['code']
        
        if code == 200:
            response = {
                "text": f"berikut ini jadwal seluruh praktikum yang anda ikuti pada semester ini",
                "data": data,
                "intent": "practicum_schedule"
            }
        else:
            response = {
                "text": f"Mohon maaf, jadwal praktikum anda tidak ditemukan. silahkan menemui asisten laboratorium yang bersangkutan",
                "data": data,
                "intent": "practicum_schedule"
            }

    return response

def value(nbi, practicum=""):
    response = ""
    if practicum:
        if nbi[:2] in "46" or (nbi[:5] in ["14614", "14615"]):
            if practicum == "Pengembangan Teknologi Website":
                practicum = "Pemrogaman Web"
            elif practicum == "Sistem Jaringan Komputer":
                practicum = "Manajemen Jaringan Komputer"
        
        req = requests.get(os.getenv('SILAB_BASE_URL')+f"api/v1/nilai?praktikum={practicum}&nbi={nbi}")
        result = req.json()
        data = result['data']
        code = result['code']

        if code == 200:
            text_grade = ""
            if data['grade'].endswith('+'):
                text_grade = data['grade']+" plus"
            if data['grade'].endswith('-'):
                text_grade = data['grade']+" minus"
            else:
                text_grade = data['grade']

            response = {
                "text": f"nilai praktikum {practicum} anda {text_grade}",
                "data": data,
                "intent": "practicum_value"
            }
        else:
            response = {
                "text": f"Mohon maaf, nilai praktikum {practicum} anda tidak ditemukan. silahkan menemui asisten laboratorium yang bersangkutan",
                "data": data,
                "intent": "practicum_value"
            }
    else:
        req = requests.get(os.getenv('SILAB_BASE_URL')+f"api/v1/nilai?nbi={nbi}")
        result = req.json()
        data = result['data']
        code = result['code']
        
        if code == 200:
            response = {
                "text": f"berikut ini nilai seluruh praktikum yang anda ikuti",
                "data": data,
                "intent": "practicum_value"
            }
        else:
            response = {
                "text": f"Mohon maaf, nilai praktikum anda tidak ditemukan. silahkan menemui asisten laboratorium yang bersangkutan",
                "data": data,
                "intent": "practicum_value"
            }

    return response