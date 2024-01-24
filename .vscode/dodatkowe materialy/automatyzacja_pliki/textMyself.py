#! python3
# textMyself.py - Definiuje funkcję textmyself(), która wysyła wiadomość 
# przekazaną jej jako argument.

# Ustawienia:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15559998888'
twilioNumber = '+15552225678'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
