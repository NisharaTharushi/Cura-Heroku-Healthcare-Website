import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.sidebar_page import Sidebarpage   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH

# create object of PageName
page = Sidebarpage(driver)

page.open_page("https://katalon-demo-cura.herokuapp.com/")
page.get_current_url()
page.click_menu_button()
page.click_login_button()
page.add_username("John Doe")
page.add_password("ThisIsNotAPassword")
page.click_login()
page.get_current_url()
page.click_menu_button()
page.click_history_button()
page.click_menu_button()
page.click_profile()
page.click_menu_button()
page.click_logout_button()
page.get_current_url()
page.quit()