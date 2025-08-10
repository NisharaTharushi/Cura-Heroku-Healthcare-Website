import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.confirmation_page import Confirmationpage   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH

# create object of PageName
page = Confirmationpage(driver)

page.open_page("https://katalon-demo-cura.herokuapp.com/")
page.get_current_url()
page.click_make_appointment()
page.get_current_url()
page.get_content()
page.add_username("John Doe")
page.add_password("ThisIsNotAPassword")
page.click_login_button()
page.get_current_url()
page.select_facility("Hongkong CURA Healthcare Center")
page.click_apply_button()
page.click_Medicaid()
page.add_Visit_date("10/06/2025")
page.add_Comment("Test Comment")
page.click_Book_button()
page.print_summary_section_text()
page.click_go_to_homepage()

page.click_side_menu()
page.click_history_button()
page.print_history_section_text()
page.back()
page.get_current_url()

page.open_page("https://katalon-demo-cura.herokuapp.com/")
page.click_make_appointment()
page.get_current_url()
page.select_facility("Hongkong CURA Healthcare Center")
page.click_apply_button()
page.click_Medicaid()
page.add_Visit_date("10/06/2025")
page.add_Comment("Test Comment")
page.click_Book_button()
page.print_summary_section_text()
page.click_go_to_homepage()

page.click_side_menu()
page.click_history_button()
page.print_history_section_text()
page.back()
page.get_current_url()
page.quit()



