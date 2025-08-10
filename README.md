## 🔧 Selenium Test Automation for Katalon CURA Website
### 🌐 Project Overview

This project contains automated test scripts written in Python using Selenium WebDriver for the demo healthcare appointment website:

🔗 [Katalon CURA Healthcare Service](https://katalon-demo-cura.herokuapp.com/)

Katalon CURA is a simple web application for booking healthcare appointments. It includes features like user login, appointment scheduling, confirmation, and a sidebar navigation menu — making it ideal for practicing UI test automation with real-world flows.

### ✅ What This Project Covers

I built automated Python test scripts using the Page Object Model (POM) design pattern. Each script focuses on:

    Functional and UI validations

    Form field entry, submission, and validations

    Login and user authentication workflows

    Appointment booking and confirmation

    Sidebar navigation and page element verifications

### 📄 Features and Pages Tested

The following pages were automated:

    Test Appointment Page

    Test Confirmation Page

    Home Page

    Login Page

    Sidebar Page

Each page has its own Page Object class and corresponding test script.

Each page and feature is handled by dedicated test files and Page Object classes for maximum modularity and maintainability.

### 🧰 Tools & Technologies Used

    Language: Python 3.x

    Automation Tool: Selenium WebDriver

    Design Pattern: Page Object Model (POM)

    Browser Drivers: ChromeDriver and GeckoDriver (Firefox)

    Execution Platform: Local (can be integrated with CI like GitHub Actions)

```
📁 Project Structure

Katalon-Demo-CURA/
│
├── pages/
│   ├── test_appointment_page.py
│   ├── test_confirmation_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── sidebar_page.py
│
├── tests/
│   ├── test_appointment.py
│   ├── test_confirmation.py
│   ├── test_home.py
│   ├── test_login.py
│   └── test_sidebar.py
│
├── requirements.txt
├── README.md
└── .gitignore
