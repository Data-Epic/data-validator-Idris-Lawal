import re
from datetime import datetime


# Create the data validator class
class DataValidator:
    """
    defines the class validator class

    Methods:
        validate_email - validates email format
        vaildate_phone_number - validates phone number format
        validate_date - validates date format
        validate_url - validates url format
    """
    def validate_email(self, email, verbose=False):
        """
        takes an email input and verifies its comformity with standard email format.

        param email (str): The email to validate
        param verbose (boolean) : prints function's details if True, default=False
        returns boolean:
                True if the valid email
                False if invalid email
        """
        self.email = email
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' #sets standard email format
        if verbose:
            if re.fullmatch(pattern, self.email): #checks if the given email comforms with the set standard
                print("Email is valid")
            else:
                print("Invalid Email!")
        return True

    def validate_phone_number(self, number, verbose=False):
        """
        takes a phone number input and verifies its comformity with standard phone number format.

        param number (str): The phone number to validate
        param verbose (boolean) : prints function's details if True, default=False
        returns boolean:
                        True if the valid phone number
                        False if invalid phone number
        """
        self.number = number
        pattern = r'^\+?[0-9]\d{0,14}$' #sets standard phone number format
        if verbose:
            if re.fullmatch(pattern, self.number): #checks if the given phone number comforms with the set standard
                print("Phone Number is Valid!")
            else:
                print("Invalid Phone Number!")
        return True

    def validate_date(self, date, verbose=False):
        """
            takes a phone number input and verifies its comformity with standard phone number format.

            param date (str): The date to validate
            param verbose (boolean) : prints function's details if True, default=False
            returns boolean:
                            True if the valid phone number
                            False if invalid phone number
        """
        self.date = date
        pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[1-9][0-9]{3}$" #sets standard date format
        if verbose:
            if re.fullmatch(pattern, self.date):    #checks if the given date comforms with the set standard
                datetime.strptime(self.date, "%m-%d-%Y")
                print("Date is Valid")
            else:
                print("Date is Invalid")
        return True

    def validate_url(self, url, verbose= True):
        """
        takes a phone number input and verifies its comformity with standard phone number format.

        param date (str): The date to validate
        param verbose (boolean) : prints function's details if True, default=False
        returns boolean:
                        True if the valid phone number
                        False if invalid phone number
        """
        self.url = url
        pattern1 = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
                        # sets standard url format with "https://" inititalization
        pattern2 = r"^[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
                        # sets standard url format without "https://" inititalization
        if verbose:
            if re.fullmatch(pattern1, self.url) or re.fullmatch(pattern2, self.url): #checks if the given url comforms with either of the set standards
                print("url is Valid!")
            else:
                print("Invalid url")
        return True