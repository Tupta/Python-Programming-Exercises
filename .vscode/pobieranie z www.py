import bs4, requests

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

# exampleFile = open('C:\Users\sendrat\Documents\python\.vscode\example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read())
# elems = exampleSoup.select('#author')
# type(elems)
# len(elems)
