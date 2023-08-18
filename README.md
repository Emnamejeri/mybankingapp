# mybank

Welcome to MyBank, an application that empowers your financial freedom and helps you manage your daily finances. With MyBank, you can track your expenses, apply for loans, and gain valuable insights into international exchange rates.

Prerequisites
Before running the code, make sure you have the following dependencies installed:

random
csv
os
datetime
re
sys
smtplib
email.mime.multipart
email.mime.text
validate_email
requests
You can install the dependencies using pip:

bash
Copy code
pip install validate_email requests
Usage
To use the MyBank application, follow these steps:

Run the code in a Python environment.
You will be greeted with the welcome message and the main menu options.
Choose the corresponding number for the desired action.
Follow the prompts and enter the required information.
The application will perform the requested action, such as creating a profile, managing transactions, applying for loans, or checking exchange rates.
Functionality
The code provides the following functionality:

intro()
Displays the welcome message and introduces the MyBank application.

welcome_page()
Displays the main menu options and allows the user to choose an action.

my_profile()
Prompts the user to enter their personal information to create a profile. The information includes the customer's title, first name, last name, nationality, date of birth, email, phone number, and country of residence. The entered information is saved in a CSV file called customerdata.csv.

my_transactions(actual_balance)
Allows the user to perform various banking operations, such as depositing and withdrawing money, viewing transaction history, and returning to the main menu. The user's account balance is maintained throughout the session.

my_loans()
Provides information about available loans and allows the user to check their eligibility for a home loan or a car loan. The user needs to enter their monthly income, monthly expenses, and loan duration. Based on this information, the maximum loan amount, total repayment amount, and monthly payment are calculated and displayed.

my_fx_account()
Allows the user to consult the latest Forex rates for fiat and crypto currencies. The user can choose to view rates for crypto or fiat currencies. For crypto currencies, the code makes an API request to retrieve the rates for 1 Bitcoin (BTC) as the base currency. The rates are then displayed for USD, EUR, CHF, and CNY.
