from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    MENU_BUTTON = (By.XPATH, "//i[@class='fa fa-bars']")
    HOME_BUTTON = (By.XPATH, "//a[normalize-space()='Home']")
    LOGIN_BUTTON = (By.XPATH, "//a[normalize-space()='Login']")
    LOGIN_SECTION = (By.XPATH, "//section[@id='login']//div[@class='container']")
    USERNAME = (By.XPATH, "//input[@id='txt-username']")
    PASSWORD = (By.XPATH, "//input[@id='txt-password']")
    LOGIN = (By.XPATH, "//button[@id='btn-login']")
    FACILITY = (By.XPATH, "//select[@id='combo_facility']")
    APPLY_BUTTON = (By.XPATH, "//input[@id='chk_hospotal_readmission']")
    MEDICAID = (By.XPATH, "//label[normalize-space()='Medicaid']")
    VISIT_DATE = (By.XPATH, "//input[@id='txt_visit_date']")
    COMMENT = (By.XPATH, "//textarea[@id='txt_comment']")
    BOOK_BUTTON = (By.XPATH, "//button[@id='btn-book-appointment']")
    SUMMARY_SECTION = (By.XPATH, "//section[@id='summary']//div[@class='container']")
    GO_TO_HOMEPAGE = (By.XPATH, "//a[@class='btn btn-default']")

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
    
    def click_menu_button(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        print("Menu button clicked")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        print("Login button clicked")

    def add_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        print("Username: " + username)

    def add_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        print("Password: " + password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN).click()
        print("Login button clicked")

    def get_content(self):
        print(self.driver.find_element(*self.LOGIN_SECTION).text)
        print(self.driver.find_element(*self.USERNAME).text)
        print(self.driver.find_element(*self.PASSWORD).text)
        print(self.driver.find_element(*self.LOGIN_BUTTON).text)

    def click_facility(self, facility):
        self.driver.find_element(*self.FACILITY).send_keys(facility)
        print("Facility: " + facility)

    def click_apply_button(self):
        self.driver.find_element(*self.APPLY_BUTTON).click()
        print("Apply button clicked")

    def click_medicaid(self):
        self.driver.find_element(*self.MEDICAID).click()
        print("Medicaid button clicked")

    def add_visit_date(self, visit_date):
        self.driver.find_element(*self.VISIT_DATE).send_keys(visit_date)
        print("Visit Date: " + visit_date)

    def add_comment(self, comment):
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        print("Comment: " + comment)

    def click_book_button(self):
        self.driver.find_element(*self.BOOK_BUTTON).click()
        print("Book button clicked")

    def print_summary_section_text(self):
        summary = self.driver.find_element(*self.SUMMARY_SECTION)
        print("Summary Content: " + summary.text)

    def click_go_to_homepage(self):
        self.driver.find_element(*self.GO_TO_HOMEPAGE).click()
        print("Go to Homepage button clicked")

    def quit(self):
        self.driver.quit()