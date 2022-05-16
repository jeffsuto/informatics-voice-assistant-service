from datetime import datetime
from datetime import timedelta
import locale

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def convert(day="", time=""):
    if time:
        if not day:
            day = datetime.now().strftime('%A')
        
        if time == "sebelumnya":
            time = "previous"
        elif time == "selanjutnya":
            time = "next"
        elif time == "sekarang":
            time = "now"
    else:
        time = ""

    if day:
        if day == 'hari ini':
            day = datetime.now().strftime('%A')
        elif day == 'besok':
            day = (datetime.now() + timedelta(days=1)).strftime('%A')
            time = ""
        elif day == 'kemarin':
            day = (datetime.now() + timedelta(days=-1)).strftime('%A')
            time = ""
        elif day == 'lusa':
            day = (datetime.now() + timedelta(days=2)).strftime('%A')
            time = ""
    else:
        day = ""

    return {"day": day, "time": time}