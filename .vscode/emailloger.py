#emailloger

# Utwórz program, który będzie pobierał argumenty wiersza
# poleceń w postaci adresu e-mail i ciągu tekstowego, a
# następnie za pomocą modułu selenium zaloguje się do Twojego
# konta e-mail i wyświetli wiadomość. Adresat wiadomości i jej
# treść są podawane jako argumenty programu. (Dla tego
# programu rozsądne może być utworzenie oddzielnego konta
# poczty elektronicznej).


#!python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

emailLogin = input(str('podaj swój login'))
emailpassword = input(str('podaj swoje hasło'))


browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('loginusername zabrany z gmaillogin')
emailElem.send_keys(emailLogin)
emailPassword = browser.find_element_by_id('userpassword zabrany z gmaillogin')
emailPassword.send_keys(emailpassword)
emailpassword.submit()

# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.Home)
