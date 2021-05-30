import requests


chunk_size = 256

url =  'https://www.youtube.com/watch?v=pTA0DSfrGZ0'
r = requests.get(url, stream = True)


try:
    with open ('doyofeelit.mp4','wb') as f:
        for chunk in r.iter_content(chunk_size= chunk_size):
            f.write(chunk)
except:
    print("This video could not be downloaded")
