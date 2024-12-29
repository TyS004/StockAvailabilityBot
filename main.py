#Importing Nessesary Modules
from urllib.request import urlopen
from Item import *
from Time import PgrmTime as pg

#Defining String Based Varabiles
url = input('Enter a URL: ')
filepath = 'C:\\Users\Tyler\Desktop\\test.txt'
user, password, toaddrs, fromaddr, domain, msg = 'tylerstier13@gmail.com', input('Enter the Password: '), 'tylerstier13@gmail.com', 'tylerstier13@gmail.com', 'smtp.gmail.com', (input('Message to Send: '))

#Password Check
emailObj = EmailHandler(user, password, toaddrs, fromaddr, domain, msg)

emailObj.checkPassword()
print('Password Accepted!')

def run():
    timeLimit = int(input('How Long Will the Program Run for: '))
    timeInterval = int(input('How Long in Between Checks: '))
    timeObj = pg()
    temprunTime = 1

    while True:
        runTime = timeObj.timeSinceStart()

        if runTime != temprunTime:
            temprunTime = timeObj.timeSinceStart()
            print(runTime)

            if runTime > timeLimit:
                break

            elif runTime % timeInterval == 0:
                UrlSourceCode = str(urlopen(url, data=None).read())
                print(UrlSourceCode)
                GPUItem = Item(UrlSourceCode, 'In Stock')
                print('Checking:')

                if GPUItem.in_Stock():
                    emailObj.sendEmail()
                    break

run()

#kjfv lmsv ikjn jwso