import bs4, requests

# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# type(noStarchSoup)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
