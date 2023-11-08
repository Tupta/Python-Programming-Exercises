#!python3



import requests

res = requests.get('http://www.gutenberg.org/files/27062/27062-0.txt')
type(res)
res.status_code == requests.codes.ok

try:
    res.raise_for_status()
except Exception as exc:
    print('Wystąpił następujący problem: %s' % (exc))
len(res.text)
print(res.text[:250])
