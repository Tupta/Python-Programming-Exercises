import pyinputplus as pyip

while True:
    prompt = 'Czy chcesz dowiedzieć się, jak zająć kogoś godzinami?\n'
    response = pyip.inputYesNo(prompt, yesVal='tak', noVal='nie')
    if response == 'nie':
        break
print('Dziękuję i życzę Ci miłego dnia.')
