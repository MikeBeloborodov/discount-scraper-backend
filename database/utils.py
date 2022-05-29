from datetime import datetime

def time_stamp():
    return datetime.now().strftime("%H:%M:%S %Y-%m-%d")