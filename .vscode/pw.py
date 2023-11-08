#! python3
# pw.py — Niebezpieczny program menedżera haseł.
PASSWORDS = {'email': '1234',
'blog': '5678',
'luggage': '91011'}
import sys 
import pyperclip
if len(sys.argv) < 2:
    print('Uzycie : pythona pw.py [konto] - skopiowanie hasła wskazzanego konta')
    sys.exit()
account = sys.argv[1] # Pierwszym argumentem wiersza poleceń jest nazwa konta.
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Hasło do konta ' + account + ' zostało skopiowane do schowka.')
else:
    print('Nie istnieje konto o nazwie ' + account + '.')
