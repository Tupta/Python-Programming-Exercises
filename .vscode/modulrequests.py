#!python3

# import requests
# res = requests.get('http://www.gutenberg.org/files/27062/27062-0.txt')
# type(res)

# res.status_code == requests.codes.ok

# len(res.text)

# print(res.text[:250])

##################################################################
# import requests
# res = requests.get('http://inventwithpython.com/strona_ktora_nie_istnieje')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('Wystąpił następujący problem: %s' % (exc))
    
###############################

import requests


res =requests.get('http://www.gutenberg.org/files/27062/27062-0.txt')

res.raise_for_status()
playFile = open('Romeo-i-Julia.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()