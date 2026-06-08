# OrangehrmApplication_Selenium_Behave_BDD_Framework

A robust **Behave** + **Selenium WebDriver (Python)** + **Allure** based automation framework for the OrangeHrm web application.  
This project demonstrates end-to-end test automation, modular framework design, configurable test data, and maintainable code, ideal for showcasing Automation skills.

---

##  Tech Stack & Tools

- **Python 3.x**  
- **Selenium WebDriver**  
- **Behave(BDD **
- **Page Object Model (POM)** design pattern  
- **CSV / Test Data files** – External test data  
- **Reports** – Test report folder (Allure)  
- **Git & GitHub** – Version control & code hosting  

---

##  Project Structure

```
OrangeHRMApplication_Selenium_behave_Automation/
│
├── features/
│   ├── Admin.feature
│   ├── claim.feature
│   ├── Homepage.feature
│   ├── info.feature
│   ├── Leave.feature
|    ├── login_feature
│   ├── steps/
│   │   ├── Admin_steps.py
│   │   ├── claim_steps.py
│   │   ├── homepage_steps.py
│   │   ├── info_steps.py
│   │	├── leave_steps.py
|   |	├── leave_steps.py
│   └── environment.py
│
├── testdata/
│   ├── data.py
|   ├── login_data.xlsx
│
├── reports/
│   ├── allure-report/
│   └── allure-results/
│
├── test_logs.log
├── requirement.txt
├── README.md
└── .gitignore
```

##  Features / What this Framework Provides
- **BDD implementation using behave framework
- **Modular design using POM** — Pages  cleanly separates features and steps for maintainability.  
- **Externalized test data** — Excel sheet for test data, keeps test logic separate from data.  
- **Explicit wait** — For reliable synchronization with web elements
- **Logger file**- For easy tracking of test execution and debugging
- **Screenshots**- Automatically capture screenshots for failed scenarios and also for specified one.  
- **Clean reporting support** — Reports folder set up for HTML or other report generation after test execution.
- **Cross browser compatibility**-Executes the test cases in chrome and firefox browser 
- **Scalable & extendable** — You can easily add more PageObjects, test scripts, utilities, or integrations (API, CI/CD) without breaking structure. 
---

##  Setup & Execution

```
### **1. Install dependencies**
```bash
pip install -r requirements.txt
```
### **2. Run tests**

### Run all tests:
```bash
behave

```

```
### **After execution, check Reports/ folder for HTML or configured report results**

## **Test Cases Covered**
```
1. Home URL validation 
2. Login functionality
3. Forgot password link functionality
4. Validation of main menu items after login
5. New user creation and validating the login
6. Validating menu items under "My info"
7.Leave assignment functionality
8.claim functionality
```
