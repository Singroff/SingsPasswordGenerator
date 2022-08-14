import random
import string


class PW():
    ALPHANUMERIC = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    SPECIAL_CHARS = '!?.,'

    def __init__(self):

        self.passName = str(input("What is this password being generated for? "))
        self.length = int(input("How many characters would you like your password to contain? "))

        charsInput = str(input("Are special characters allowed? "))

        if "y" in charsInput.lower():
            self.specialAllowed = True
        else:
            self.specialAllowed = False

        while self.length < 12:
            self.length = int(input("How many characters would you like your password to contain? "))

        self.passW = ''

        if self.specialAllowed:
            numOfSpecialChars = random.randint(3, self.length - 9)
            print(numOfSpecialChars)

            self.passW = self.passW.join(
                random.SystemRandom().choice(self.ALPHANUMERIC) for i in range(self.length - numOfSpecialChars))
            print(self.length - numOfSpecialChars)
            print(self.passW)

            genSpecChars = ''.join(random.SystemRandom().choice(self.SPECIAL_CHARS) for i in range(numOfSpecialChars))
            self.passW += genSpecChars

            print(numOfSpecialChars)
            print(self.passW)

            l = list(self.passW)
            random.shuffle(l)
            self.passW = ''.join(l)
        else:
            self.passW = self.passW.join(random.choice(self.ALPHANUMERIC) for i in range(self.length))

    def printPW(self):
        print("Password for ", self.passName, " is ", self.passW)


if __name__ == "__main__":
    pw = PW()
    pw.printPW()
