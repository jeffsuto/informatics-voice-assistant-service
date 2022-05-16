from dotenv import load_dotenv
import os
import requests
import json

from action_lib import day_converter

load_dotenv()

def schedule(lecturer, day="", time=""):
    # if time == "jam":
    #     time = "selanjutnya"
    converted = day_converter.convert(day, time)
    converted_day = converted['day']
    converted_time = converted['time']

    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/schedules/lecturer?name={lecturer}&day={converted_day}&time={converted_time}")
    result = req.json()
    data = result['data']
    code = result['code']

    text = ""
    if code == 200:
        if time:
            text = f"berikut ini jadwal mengajar {data[0]['gender']} {data[0]['lecturer']} {time}"
        elif day:
            text = f"berikut ini jadwal mengajar {data[0]['gender']} {data[0]['lecturer']} hari {converted_day}"
        else:
            text = f"Berikut ini jadwal mengajar {data[0]['gender']} {data[0]['lecturer']}"
        
    elif code == 404 and data:
        if time:
            text = f"jadwal mengajar {data[0]['gender']} {data[0]['lecturer']} {time} kosong"
        else:
            text = f"jadwal mengajar {data[0]['gender']} {data[0]['lecturer']} hari {converted_day} kosong"
    else:
        text = f"Mohon maaf, saya tidak dapat menemukan jadwal dosen atas nama {lecturer}"

    response = {
        "text": text,
        "data": data,
        "code": code,
        "intent": "lecturer_schedule"
    }
    
    return response

def location(lecturer):
    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/lecturers/location?name={lecturer}")
    result = req.json()
    data = result['data']
    code = result['code']

    text = ""
    if code == 200:
        text = f"berikut ini lokasi dosen atas nama {data[0]['gender']} {data[0]['nickname']}"
    else:
        text = f"Mohon maaf, saya tidak dapat menemukan data dosen atas nama {lecturer}"

    response = {
        "text": text,
        "data": data,
        "code": code,
        "intent": "lecturer_location"
    }
    
    return response

def whatsapp_number(lecturer):
    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/lecturers/whatsapp?name={lecturer}")
    result = req.json()
    data = result['data']
    code = result['code']

    text = ""
    if code == 200:
        text = f"berikut ini nomor whatsapp dosen atas nama {data[0]['gender']} {data[0]['nickname']}"
    else:
        text = f"Mohon maaf, saya tidak dapat menemukan data dosen atas nama {lecturer}"
    
    response = {
        "text": text,
        "data": data,
        "intent": "lecturer_whatsapp_number"
    }	

    return response