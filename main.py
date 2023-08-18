import random
import csv
import os
import datetime
import re
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email_address import validate_email
import requests


def intro():
    print(
        "Welcome to MyBank\n\nYour App for Empowering you Financial Freedom\nYour Money, Your Way!!!\nThe ultimate financial application that revolutionizes how you manage your daily finances. \nTake control of your money like never before with our intuitive and user-friendly interface. \nTrack your expenses, apply for loans, and gain valuable insights into international exchange rates."
    )
    return welcome_page()

def welcome_page():
    print(
        "Press the corresponding Number to start:\n 1.My Profile\n 2.My Operations\n 3.My Loans\n 4.My Card\n 5.My Fx account\n 6.Help\n 7.Data"
    )
    user_choice = int(input("Enter choice: "))

    if user_choice == 1:
        return my_profile()
    elif user_choice == 2:
        return my_transactions()
    elif user_choice == 3:
        return my_loans()
    elif user_choice == 4:
        return my_card()
    elif user_choice == 5:
        return my_fx_account()
    elif user_choice == 6:
        return help_section()
    elif user_choice == 7:
        return my_data()
    elif user_choice > 7 or user_choice <= 0:
        print("Invalid choice, try again")
        return user_choice


def my_profile():
    print("Please enter your data to create a profile with us\n\n You can always write stop to end the process")
    customer_id = random.randint(100000, 999999)

    while True:
        customer_title = input("Title (Mrs/Mr): ").lower()

        if customer_title == "mrs" or customer_title == "mr":
            break
        elif customer_title == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid customer title. Please try again with Mrs or Mr.")
            continue

    while True:
        customer_first_name = input("First Name (include any middle names): ").lower()
        if re.match("^[a-z]+(?:\s[a-z]+)*$", customer_first_name):
            break
        elif customer_first_name == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid name. Please try again without any digits or special characters.")
            continue

    while True:
        customer_last_name = input("Last Name: ").lower()
        if re.match("^[a-z]+(?:\s[a-z]+)*$", customer_last_name):
            break
        elif customer_last_name == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid name. Please try again without any digits or special characters.")
            continue

    while True:
        customer_nationality = input("Nationality(ies): ").lower()
        if re.match("^[a-z]+(?:\s[a-z]+)*$", customer_nationality):
            break
        elif customer_nationality == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid input. Please try again without any digits or special characters.")
            continue

    while True:
        customer_dob = input("Date of birth (DD.MM.YYYY): ")
        date_regex = r"^(0[1-9]|1\d|2\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"

        if re.match(date_regex, customer_dob):
            break
        elif customer_dob == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid date format. Please use the format DD.MM.YYYY.")

    while True:
        customer_email = input("E-mail: ")
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}$"

        if re.match(email_regex, customer_email):
            break
        elif customer_email == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid email format. Please use the format (example@domain.com)")

    while True:
        customer_phone = input("Phone: ")
        phone_regex = r"^\d{8}$"

        if re.match(phone_regex, customer_phone):
            break
        elif customer_phone == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid phone format. Please only enter 8 digits")

    while True:
        customer_address = input("Country of Residence: ").lower()
        if re.match("^[a-z]+(?:\s[a-z]+)*$", customer_address):
            break
        elif customer_address == "stop":
            print("Exiting registration process...")
            return welcome_page()
        else:
            print("Invalid Country name. Please try again without any special characters.")
            continue

    while True:
        try:
            customer_agreement = input("Please refer to our terms and conditions in the terms.txt file\n Confirm if you agree to processing your data by MyBank as per international financial regulations (yes/no): ").lower()

            if customer_agreement == "yes" or customer_agreement == "y":
                print("Welcome to My Bank", customer_title, customer_last_name, "\nYour user ID is", customer_id, "\nSaving your details...\nDiscover our wide range of banking services")
                create_customer_data_csv(customer_id, customer_title, customer_first_name, customer_last_name, customer_dob, customer_address, customer_nationality, customer_email, customer_phone)
                return welcome_page()
            elif customer_agreement == "no" or customer_agreement == "n":
                print("Unfortunately", customer_title, customer_last_name, "we cannot offer you our services without your consent to processing your data.")
                exit_choice = input("Please type 'exit' to abandon the process or 'yes' to agree to our Terms and Conditions: ").lower()

                if exit_choice == "yes" or exit_choice == "y":
                    print("Welcome to My Bank", customer_title, customer_last_name, "\nYour user ID is", customer_id, "\nSaving your details...\nDiscover our wide range of banking services")
                    create_customer_data_csv(customer_id, customer_title, customer_first_name, customer_last_name, customer_dob, customer_address, customer_nationality, customer_email, customer_phone)
                    return welcome_page()
                elif exit_choice == "exit":
                    print("Sad to see you go", customer_title, customer_last_name)
                    sys.exit()
                else:
                    print("Invalid Choice. Kindly enter 'yes' or 'exit'.")
            else:
                print("Invalid Choice. Kindly enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid input. Please enter text.")


def create_customer_data_csv(customer_id, customer_title, customer_first_name, customer_last_name, customer_dob, customer_address, customer_nationality, customer_email, customer_phone):
    if not os.path.isfile("customerdata.csv"):
        with open("customerdata.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow([
                "customer_id",
                "customer_title",
                "customer_first_name",
                "customer_last_name",
                "customer_dob",
                "customer_address",
                "customer_nationality",
                "customer_email",
                "customer_phone",
            ])

    with open("customerdata.csv", "a") as results_file:
        writer = csv.writer(results_file)
        writer.writerow([
            customer_id,
            customer_title,
            customer_first_name,
            customer_last_name,
            customer_dob,
            customer_address,
            customer_nationality,
            customer_email,
            customer_phone,
        ])

    return customer_id



        

def my_transactions(actual_balance=0):
    session_date = datetime.date.today()
    session_time = datetime.datetime.now().strftime("%H:%M:%S")

    print(
        "What type of operation would you like to make?\nPress the corresponding number:\n1. Deposit\n2. Withdrawal\n3. History\n4. Menu"
    )

    writer = None

    while True:
        user_choice = input("Enter a number: ")

        if user_choice == "1":
            while True:
                try:
                    user_deposit_amount = input("Enter a sum (minimum 1 EUR): ")
                    deposit_amount = float(user_deposit_amount)
                    if deposit_amount < 1:
                        print("You need to deposit a minimum of 1 EUR.")
                    else:
                        actual_balance += deposit_amount
                        print(
                            f"You now hold: {actual_balance} EUR\n\nBack to the main section..."
                        )
                        # Write the transaction to the history.csv file
                        with open("history.csv", "a") as results_file:
                            writer = csv.writer(results_file)
                            writer.writerow(
                                ["Transaction Type", "Amount", "Date", "Time"]
                            )
                            writer.writerow(
                                ["deposit", deposit_amount, session_date, session_time]
                            )
                            results_file.write("\n")
                        return my_transactions(actual_balance)
                except ValueError:
                    print("Invalid input. You must enter a valid number.")

        elif user_choice == "2":
            print(f"Your current account balance is {actual_balance}")
            while True:
                try:
                    user_withdrawal_amount = input("Enter a sum: ")
                    withdrawal_amount = float(user_withdrawal_amount)
                    if withdrawal_amount <= actual_balance:
                        print("Withdrawal successful")
                        actual_balance -= withdrawal_amount
                        print(f"Your current account balance is {actual_balance} EUR")
                        with open("history.csv", "a") as results_file:
                            writer = csv.writer(results_file)
                            writer.writerow(
                                ["Transaction Type", "Amount", "Date", "Time"]
                            )
                            writer.writerow(
                                [
                                    "withdrawal",
                                    withdrawal_amount,
                                    session_date,
                                    session_time,
                                ]
                            )
                            results_file.write("\n")
                        return my_transactions(actual_balance)
                    else:
                        print("Insufficient funds")
                except ValueError:
                    print("Invalid input. You must enter a valid number.")

        elif user_choice == "3":
            if not os.path.isfile("history.csv"):
                print("No transaction history found.")
            else:
                print(
                    "You can find all of your history transactions in the History.csv file"
                )
            return my_transactions()
        elif user_choice == "4":
            print("Exiting operations section...")
            return welcome_page()

        else:
            print("Invalid choice, select the appropriate number.")

        return actual_balance


def my_loans():
    print(
        "Our Selection of available loans is displayed below \n Press the corresponding Number to verify your eligibility:\n 1.Home Loan\n 2.Car Loan \n 3.Menu"
    )

    try:
        user_loan_choice = int(input("Enter a number: "))
        if user_loan_choice == 1:
            print(
                "You are now one step closer to your dream home - Please enter the required data"
            )
            try:
                user_monthly_income = int(input("Net monthly income (after Taxes): "))
                user_monthly_expenses = int(input("Net monthly expenses: "))
                if user_monthly_income <= user_monthly_expenses:
                    print(
                        "Unfortunately, your monthly income doesn't allow you to apply for a loan"
                    )
                    return my_loans()
                loan_duration = int(input("Number of Years: ")) * 12

                if loan_duration >= 12 and loan_duration <= 300:
                    pass
                else:
                    print(
                        "Note the number of years should be starting 1 year and below 25 years"
                    )
                    return loan_duration

                monthly_installment = round(
                    (user_monthly_income - user_monthly_expenses) * 0.75, 3
                )

                loan_amount = monthly_installment * loan_duration
                loan_cost = round(loan_amount * 1.09, 3)
                total_monthly_payment = round(loan_cost / loan_duration, 3)

                print(
                    f"Congrats! your are eligible for a loan \nThe maximum amount you can borrow is {loan_amount} EUR \nThe amount to be repaid based on a 9% interest rate is {loan_cost} EUR \nThe monthly amount to be paid is {total_monthly_payment} EUR"
                )

            except ValueError:
                print("Invalid input. Please enter valid integer values.")
                return my_loans()

        elif user_loan_choice == 2:
            print(
                "You are now one step closer to owning your dream car - Please enter the required data"
            )
            try:
                user_monthly_income = int(input("Net monthly income (after Taxes): "))
                user_monthly_expenses = int(input("Net monthly expenses: "))

                if user_monthly_income <= user_monthly_expenses:
                    print(
                        "Unfortunately, your monthly income doesn't allow you to apply for a loan"
                    )
                    return my_loans()

                loan_duration = 60  # number of months in 5 years is (5 * 12)
                monthly_installment = round(
                    (user_monthly_income - user_monthly_expenses) * 0.75, 3
                )
                loan_amount = monthly_installment * loan_duration
                loan_cost = round(loan_amount * 1.05, 3)
                total_monthly_payment = round(loan_cost / loan_duration, 3)

                print(
                    f"Congrats! your are eligible for a loan \nThe maximum amount you can borrow is {loan_amount} EUR \nThe amount to be repaid based on a 5% interest rate during 5 years is {loan_cost} EUR \nThe monthly amount to be paid is {total_monthly_payment} EUR"
                )
                return my_loans()

            except ValueError:
                print("Invalid input. Please enter valid integer values.")
                return my_loans()

        elif user_loan_choice >= 3:
            print("Exiting loans section...\nBack to main page......")
        return welcome_page()

    except ValueError:
        print("Invalid input. Please enter valid integer values (1|2|3).")
        return my_loans()


def my_fx_account():
    try:
        fx_user_choice = int(
            input(
                "Consult the latest Forex rates for Fiat and Crypto currencies \n Press the corresponding Number:\n 1.Cypto\n 2.Fiat\n 3.Menu\n"
            )
        )

        if fx_user_choice == 1:
            print("List of exchange rates for 1 Bitcoin BTC as a base currency: ")
            try:
                url = "https://api.coingecko.com/api/v3/exchange_rates"

                response = requests.get(url)
                data = response.json()

                usd_rate = data["rates"]["usd"]["value"]
                eur_rate = data["rates"]["eur"]["value"]
                egp_rate = data["rates"]["chf"]["value"]
                cny_rate = data["rates"]["cny"]["value"]

                print("USD Rate:", usd_rate)
                print("EUR Rate:", eur_rate)
                print("CHF Rate:", egp_rate)
                print("CNY Rate:", cny_rate)
                return my_fx_account()

            except requests.exceptions.RequestException as e:
                print("Apologies - An error occurred while making the API request:", e)
            except ValueError:
                print("Invalid input. Please enter valid integer values (1|2|3).")

        elif fx_user_choice == 2:
            print("List of exchange rates for 1 USD as base currency: ")
            api_key = "fa9f8e4cc8c9faf86d3e0d1c"
            base_currency = "USD"
            target_currencies = ["CHF", "EUR", "EGP", "TND", "CNY", "GBP", "JPY"]

            url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and data["result"] == "success":
                rates = data["conversion_rates"]

                for currency in target_currencies:
                    if currency in rates:
                        rate = rates[currency]
                        print(f"1 {base_currency} = {rate} {currency}")
                    else:
                        print(f"Currency {currency} not found in the API response.")
            else:
                print("Apologies - An error occurred while making the API request.")
            return my_fx_account()

        elif fx_user_choice >= 3:
            print("Exiting forex trading section...\nBack to the main page......")
        return welcome_page()

    except ValueError:
        print("Invalid input. Please enter valid integer values (1|2|3|4).")
        return my_fx_account()



def my_card():
    delivery_address = input(
        "To order our card please enter a delivery address \nThe address must be composed of: \nThe house number(digits) \nThe street name(string) \nThe Zip/Postal code \nThe city name \nThe Country: \n\n"
    )

    match = re.match(
        r"^(\d{1,3})\s+(?:[A-Za-z]+\s?){1,3}\s+(\d{3,6})\s+((?:[A-Za-z]+\s?)+)\s+([A-Za-z]+)$",
        delivery_address,
    )
    if match:
        print(
            "Thank you! The card should reach your specified address in 10 working days.\nBack to the main menu section....."
        )
        return welcome_page()
    elif delivery_address == "return":
        print("Back to the main menu section.....")
        return welcome_page()
    else:
        print(
            "The provided address is not valid. Please enter a new one and respect the indicated format."
        )
        return my_card()


def verify_email(email):
    return validate_email(email)


def send_email(email_address, message):
    msg = MIMEMultipart()
    msg["From"] = "emnaemna092@gmail.com"
    msg["To"] = email_address
    msg["Subject"] = "Your Support Request Confirmation"
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("emnaemna092@gmail.com", "fsiecgjohczzwevm")
        server.send_message(msg)
        server.quit()
        

    except smtplib.SMTPException as e:
        print("An error occurred while sending the confirmation email:", str(e))


def help_section():
    print(
        "If you need assistance or have any questions, please don't hesitate to reach out to our dedicated support team - \nWe are always happy to help."
    )
    support_request = input(
        "Would you like to contact our support team (enter yes or no)? "
    ).lower()

    if support_request == "yes" or support_request == "y":
        user_request = input("Please write your question: ").lower()
        user_email = input("Please enter your email address: ").lower()

        if verify_email(user_email):
            send_email("emnaemna092@gmail.com", f"User Request: {user_request} \n\nUser Email: {user_email}")
            confirmation_message = "Thank you for contacting us, \n\nyour Email was well received. \n\nWe will get back to you promptly with an answer. \nThanks for using our services."
            send_email(user_email, confirmation_message)

            print(
                "Question submitted successfully. A confirmation email has been sent to your email address."
            )
            return welcome_page()
        else:
            print("Invalid email address. Please try again.")
            return help_section()
    elif support_request == "no" or support_request == "n":
        print(
            "We are glad everything is clear dear customer \n\nBack to the main menu section....."
        )
        return welcome_page()


def my_data():
    print("Below are your saved details on records")

    with open("customerdata.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            identification = row["customer_id"]
            title = row["customer_title"]
            firstMiddleName = row["customer_first_name"]
            lastName = row["customer_last_name"]
            dob = row["customer_dob"]
            address = row["customer_address"]
            nationality = row["customer_nationality"]
            email = row["customer_email"]
            telephone = row["customer_phone"]

            print(f"Your ID: {identification}")
            print(f"Title: {title}")
            print(f"Registered first/middle name(s): {firstMiddleName}")
            print(f"Registered last name: {lastName}")
            print(f"Registered DOB(dd.mm.yyyy): {dob}")
            print(f"Registered residential address: {address}")
            print(f"Registered nationality(ies): {nationality}")
            print(f"Registered e-mail: {email}")
            print(f"Registered phone(+372): {telephone}")
            print(
                "Reminder: You have agreed to our user terms and conditions upon registration \n ------------------------------------"
            )
    return welcome_page()


if __name__ == "__main__":
    intro()
