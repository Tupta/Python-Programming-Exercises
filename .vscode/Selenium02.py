# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('bookcover')
#     print('Znaleziono element <%s> wraz z taką nawzą klasy!' %(elem.tag_name))
# except:
#     print('Nie udało się znaleźć elementu wraz z podaną nazwą kaly.')            
    


####################### druga wersja tego programu

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')

# try:
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'bookcover'))
#     )
#     print('Znaleziono element <%s> z taką nazwą klasy!' % (element.tag_name))
# except Exception as e:
#     print('Nie udało się znaleźć elementu z podaną nazwą klasy.')
#     print(e)
    

#########################
# W powyższym fragmencie kodu przeglądarka Firefox
# przechodzi do witryny http://inventwithpython.com/, pobiera
# obiekt WebElement dla elementu <a> zawierającego tekst Read It
# Online, a następnie symuluje kliknięcie tego elementu <a>
##########################

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# linkElem = browser.find_element_by_partial_link_text('Read It Online')
# type(linkElem)
# #<class 'selenium.webdriver.remote.webelement.WebElement'>
# linkElem.click()


########################################################################
# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')

# try:
#     # Użyj find_element_by_partial_link_text, aby znaleźć element na podstawie fragmentu tekstu łącza
#     linkElem = browser.find_element_by_partial_link_text('Read It Online')
#     print('Znaleziono element z tekstem "Read It Online".')
# except Exception as e:
#     print('Nie udało się znaleźć elementu z podanym tekstem łącza.')
#     print(e)
    
#################################################Symulowanie naciśnięcia klawiszy w polu tekstowym:

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://mail.yahoo.com')
# emailElem = browser.find_element_by_id('login-username')
# emailElem.send.keys('nieprawdziwy_adres_e-mail')
# passwordElem = browser.find_element_by_id('login-passwd')
# passwordElem.send_keys('12345')
# passwordElem.submit()

################################################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
# browser.get('http://nostrach.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.Home)

########################################
# 
# ponuizej inna wersja tego programu bo ten powyzej jakos nie chce dzialac, nie zeby ten ponizej byl lepszy :D
###################################################################

# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://nostrach.com')

# # Przewiń stronę na dół
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # Przewiń stronę na górę
# browser.execute_script("window.scrollTo(0, 0);")

###############################################################################################