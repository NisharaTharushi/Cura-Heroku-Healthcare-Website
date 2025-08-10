import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import Loginpage   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH

# create object of PageName
page = Loginpage(driver)

page.open_page("https://katalon-demo-cura.herokuapp.com/")
page.click_menu_button()
page.click_login_button()
page.add_username("John Doe")
page.add_password("ThisIsNotAPassword")
page.click_login()
page.get_current_url()
page.click_facility("Hongkong CURA Healthcare Center")
page.click_apply_button()
page.click_medicaid()
page.add_visit_date("10/06/2025")
page.add_comment("Test Comment")
page.click_book_button()
page.get_current_url()
page.print_summary_section_text()
page.click_go_to_homepage()
page.quit()
