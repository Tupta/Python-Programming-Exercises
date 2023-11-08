#emailloger

# Utwórz program, który będzie pobierał argumenty wiersza
# poleceń w postaci adresu e-mail i ciągu tekstowego, a
# następnie za pomocą modułu selenium zaloguje się do Twojego
# konta e-mail i wyświetli wiadomość. Adresat wiadomości i jej
# treść są podawane jako argumenty programu. (Dla tego
# programu rozsądne może być utworzenie oddzielnego konta
# poczty elektronicznej).
# Dobrze byłoby dodać funkcję powiadamiania. Możesz
# utworzyć również podobny program przeznaczony do
# wysyłania komunikatów z serwisów Facebook lub Twitter.



#!python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

emailLogin = input(str('podaj swój login'))
emailpassword = input(str('podaj swoje hasło'))


browser.get('http://gmail.com')

# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.Home)
