#!python3

#sendDuesReminders.py — Wysyłanie wiadomości e-mail na podstawie
# zapisanych w arkuszu kalkulacyjnym informacji o płatnościach.

iimport openpyxl, smtplib, sys

# Otwieranie arkusza kalkulacyjnego i pobieranie informacji o ostatnich płatnościach.

wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb['Sheet1']
lastCol = sheet.max_column
latestMonth = sheet.cell(row=1, column=lastCol).value

# Sprawdzenie stanu płatności poszczególnych członków klubu.

unpaidMembers = {}
for r in range(2, sheet.max_row + 1):
    payment = sheet.cell(row=r, column=lastCol).value
    if payment != 'zapłacono':
        name = sheet.cell(row=r, column=1).value
        email = sheet.cell(row=r, column=2).value
        unpaidMembers[name] = email

# Logowanie do konta poczty elektronicznej.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('tomaszsendra@gmail.com', sys.argv[1])

# Wysyłanie wiadomości e-mail z przypomnieniem o składce.

for name, email in unpaidMembers.items():
    body = f"Subject: Zaległa składka za {latestMonth}. Proszę o jak najszybsze uregulowanie należności.\n\nDziękuję"
    print(f"Wysyłanie wiadomości e-mail na adres {email}...")
    sendmailStatus = smtpObj.sendmail('tomaszsendra@gmail.com', email, body)
    if sendmailStatus != {}:
        print(f'Wystąpił problem podczas wysyłania wiadomości e-mail na adres {email}: {sendmailStatus}')
smtpObj.quit()
