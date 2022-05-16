from dotenv import load_dotenv
import os
import requests
import json

from action_lib import day_converter

load_dotenv()

def schedule(nbi="", day="", time=""):
    if time == "jam":
        time = "selanjutnya"

    converted = day_converter.convert(day, time)
    converted_day = converted['day']
    converted_time = converted['time']

    req = requests.get(os.getenv('WEB_BASE_URL')+f"api/v1/schedules/student/{nbi}?day={converted_day}&time={converted_time}")
    result = req.json()
    data = result['data']
    code = result['code']

    text = ""
    if code == 200:
        if time:
            text = f"berikut ini jadwal mata kuliah {time}"
        elif day:
            text = f"berikut ini jadwal mata kuliah hari {converted_day}"
        else:
            text = f"Berikut ini jadwal mata kuliah anda semester ini"
    else:
        if time:
            text = f"tidak ada jadwal mata kuliah {time}"
        elif day:
            text = f"jadwal hari {converted_day} kosong"
        else:
            text = f"Mohon maaf, jadwal kuliah semester ini tidak ditemukan"

    response = {
        "text": text,
        "data": data,
        "code": code,
        "intent":"student_schedule"
    }

    return response