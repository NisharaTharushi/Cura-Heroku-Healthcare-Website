from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Confirmationpage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    MAKE_APPOINTMENT = (By.XPATH, "//a[@id='btn-make-appointment']")
    LOGIN_SECTION = (By.XPATH, "//section[@id='login']//div[@class='container']")
    USERNAME = (By.XPATH, "//input[@id='txt-username']")
    PASSWORD = (By.XPATH, "//input[@id='txt-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='btn-login']")
    FACILITY = (By.XPATH, "//select[@id='combo_facility']")
    APPLY_BUTTON = (By.XPATH, "//input[@id='chk_hospotal_readmission']")
    MEDICAID = (By.XPATH, "//label[normalize-space()='Medicaid']")
    VISIT_DATE = (By.XPATH, "//input[@id='txt_visit_date']")
    COMMENT = (By.XPATH, "//textarea[@id='txt_comment']")
    BOOK_BUTTON = (By.XPATH, "//button[@id='btn-book-appointment']")
    SUMMARY_SECTION = (By.XPATH, "//section[@id='summary']//div[@class='container']")
    GO_TO_HOMEPAGE = (By.XPATH, "//a[@class='btn btn-default']")
    SIDE_MENU = (By.XPATH, "//a[@id='menu-toggle']")
    HISTORY_BUTTON = (By.XPATH, "//a[normalize-space()='History']")
    HISTORY_SECTION = (By.XPATH, "//section[@id='history']//div[@class='container']")
    

    def open_page(self, url):
        self.driver.get(url)

    # click make appointment button and open new URL
    def click_make_appointment(self):
        self.driver.find_element(*self.MAKE_APPOINTMENT).click()
        print("Make Appointment button clicked and open new URL: " + self.driver.current_url)

    def get_current_url(self):
        print("Current URL: " + self.driver.current_url)
   
    def get_content(self):
        print(self.driver.find_element(*self.LOGIN_SECTION).text)
        print(self.driver.find_element(*self.USERNAME).text)
        print(self.driver.find_element(*self.PASSWORD).text)
        print(self.driver.find_element(*self.LOGIN_BUTTON).text)
    
    def add_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        print("Username: " + username)

    def add_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        print("Password: " + password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        print("Login button clicked and open new URL: " + self.driver.current_url)
    
    def select_facility(self, facility):
        self.driver.find_element(*self.FACILITY).send_keys(facility)
        print("Facility: " + facility)

    def click_apply_button(self):
        self.driver.find_element(*self.APPLY_BUTTON).click()
        print("Login button clicked and open new URL: " + self.driver.current_url)

    def click_Medicaid(self):
        self.driver.find_element(*self.MEDICAID).click()
        print("Login button clicked and open new URL: " + self.driver.current_url)

    def add_Visit_date(self, visit_date):
        self.driver.find_element(*self.VISIT_DATE).send_keys(visit_date)
        print("Visit Date: " + visit_date)

    def add_Comment(self, comment):
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        print("Comment: " + comment)

    def click_Book_button(self):
        self.driver.find_element(*self.BOOK_BUTTON).click()
        print("Book button clicked and open new URL: " + self.driver.current_url)
        if "Appointment Confirmation" in self.driver.page_source:
            print("Appointment Booked Successfully Appointment Confirmation text displayed")
        else:
            print("Appointment Booking Failed")

    def print_summary_section_text(self):
        summary = self.driver.find_element(*self.SUMMARY_SECTION)
        print("Summary Content: " + summary.text)

    def click_go_to_homepage(self):
        self.driver.find_element(*self.GO_TO_HOMEPAGE).click()
        print("Go to Homepage button clicked and open new URL: " + self.driver.current_url)
        

    # check appoinment booking in history page 
    def click_side_menu(self):
        self.driver.find_element(*self.SIDE_MENU).click()
        print("Side Menu button clicked")

    def click_history_button(self):
        self.driver.find_element(*self.HISTORY_BUTTON).click()
        print("History button clicked and open new URL: " + self.driver.current_url)

    def print_history_section_text(self):
        history = self.driver.find_element(*self.HISTORY_SECTION)
        print("History Content: " + history.text)

    def back(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()