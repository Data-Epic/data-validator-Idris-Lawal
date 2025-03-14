import re
from datetime import datetime


class DataValidator:
    def validate_email(self, email):
        self.email = email
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.fullmatch(pattern, self.email):
            print("Email is Valid!")
            return True
        else:
            print("Invalid Email!")
            return False

    def validate_phone_number(self, number):
        self.number = number
        pattern = r'^\+?[0-9]\d{0,14}$'
        if re.fullmatch(pattern, self.number):
            print("Phone Number is Valid!")
            return True
        else:
            print("Invalid Phone Number!")
            return False

    def validate_date(self, date):
        self.date = date
        pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[1-9][0-9]{3}$"
        if re.fullmatch(pattern, self.date):
                datetime.strptime(self.date, "%m-%d-%Y")
                print("Date is Valid")
                return True
        else:
            print("Date is Invalid")
            return False

    def validate_url(self, url):
        self.url = url
        pattern1 = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
        pattern2 = r"^[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
        if re.fullmatch(pattern1, self.url) or re.fullmatch(pattern2, self.url):
            print("url is Valid!")
            return True
        else:
            print("Invalid url")
            return False


def main():
    validator = DataValidator()
    while True:
        print("1. Validate your email\n"
              "2. Validate your Phone Number\n"
              "3. Validate your Date\n"
              "4. Validate your url\n"
              "5. Exit")
        choice = int(input("Pick a task: "))
        if choice == 1:
            email = input("Enter your email: ")
            validator.validate_email(email)
        elif choice == 2:
            number = input("Enter your phone number: ")
            validator.validate_phone_number(number)
        elif choice == 3:
            date = input("Enter your date: ")
            validator.validate_date(date)
        elif choice == 4:
            url = input("Enter your url: ")
            validator.validate_url(url)
        elif choice == 5:
            break
        else:
            print ("Invalid input")

if __name__ == "__main__":
    main()