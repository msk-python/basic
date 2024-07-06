import requests

def check_Internet_Access():
    url = 'https://google.com'
    
    time = 2

    try:
        _ = requests.get(url, timeout=time)
        print("Internet Connected")
        return True
    except requests.ConnectionError:
        print("Please Connect Internet")
        return False
    
check_Internet_Access()