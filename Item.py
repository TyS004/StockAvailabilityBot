import operator as op
from smtplib import *
import ssl

class ItemTag:
    def __init__(self, sourceCode):
        #super.__init__(sourceCode)
        self.possibleTags = ['"availability":"InStock":"Buy Now"']

    def findAvalibilityTag(self):

        for tag in self.possibleTags:

            #if op.contains(, tag):
                return tag

        return 'No Tag found'


class Item:

    def __init__(self, source_code, availabilityTag):
        self.mySourceCode = source_code
        self.availabilityTag = availabilityTag

    def in_Stock(self):
        is_Stock = op.contains(self.mySourceCode, self.availabilityTag)

        if is_Stock:
            return True
        else:
            return False


class EmailHandler:

    def __init__(self, user, password, toaddrs, fromaddr, domain, msg):
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.domain = domain
        self.user = user
        self.password = password
        self.emailHandler = SMTP(domain, 587)
        self.context = ssl.create_default_context()
        self.msg = msg

    def checkPassword(self):
        self.emailHandler.set_debuglevel(1)
        self.emailHandler.starttls(context=self.context)

        while True:
            try:
                self.emailHandler.login(self.user, self.password)
                break

            except SMTPAuthenticationError:
                print('Invalid Password')
                self.password = input('Enter a new Password: ')

    def sendEmail(self):
        self.emailHandler.sendmail(self.fromaddr, self.toaddrs, self.msg)
        self.emailHandler.close()
