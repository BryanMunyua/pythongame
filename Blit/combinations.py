import requests


chunk_size = 256

url =  'https://www.pornhub.com/view_video.php?viewkey=ph5d0b9d24ba4a0'

r = requests.get(url, stream = True)

with open ('phb.html','wb') as f:
    for chunk in r.iter_content(chunk_size= chunk_size):
        f.write(chunk)
