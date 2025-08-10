import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.home_page import Homepage   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH

# create object of PageName
home = Homepage(driver)

home.open_page("https://katalon-demo-cura.herokuapp.com/")
home.page_title()
home.page_sub_title()
home.click_menu_button()
home.click_home_button()
home.click_menu_button()
home.click_login_button()
home.go_back()
home.click_make_appointment()
home.go_back()
home.print_footer_section_text()
home.print_body_section_text()
home.quit()
