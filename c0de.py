import requests
import time

def get_online_data(count):
    """ 1k data per request 
        from https://qrng.anu.edu.au/
    """


    data = list()

    for _ in range(count):
        url = 'https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8'
        response = requests.get(url)
        response = response.json()
        data.extend(response['data'])
        time.sleep(5)
    return data

def to_txt(name,lst):
    
    file = open(name,'w')    
    for numbers in lst:
        file.write(str(numbers)+"\n")

    file.close()

to_txt("1k randy.txt",get_online_data(1))