import requests
import os 



def download (url_file):
    if  not os.path.exists('../data/IN/valeursfoncieres-2019.txt'):
        r = requests.get(url_file)
        with open ('../data/IN/valeursfoncieres-2019.txt', 'wb') as f:
            f.write(r.content)
    else:
        print('file already exists')



