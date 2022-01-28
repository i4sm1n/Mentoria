from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


@given('a user logged on Lead’s platform, on edit profile page #4')
def given(context):
    context.driver = webdriver.Chrome("C:/Users/iasmi/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("iasmin.santos@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    enter_button = context.driver.find_element_by_id("login-btn")
    enter_button.click()

    time.sleep(3)

    profile_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/button/img")
    profile_btn.click()

    edit_profile_btn = context.driver.find_element_by_xpath( "/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/div/div[2]/div[1]/button")
    edit_profile_btn.click()

    time.sleep(3)

@when('the user fill the required fields on tab ‘Change password’ and save the change#')
def when(context):
    change_password_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/form/div/div/button")
    change_password_btn.click()

    old_password_field = context.driver.find_element_by_id("currentPassword")
    old_password_field.send_keys("abcd1234")

    new_password_field = context.driver.find_element_by_id("password")
    new_password_field.send_keys(Keys.CONTROL+"a")
    new_password_field.send_keys(Keys.DELETE)
    new_password_field.send_keys("1234abcd")

    confirm_password_field = context.driver.find_element_by_id("confirmPassword")
    confirm_password_field.send_keys("1234abcd")

    save_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[11]/button")
    save_btn.click()

@then('the system notifies the user that update was successful#')
def then(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/div/app-alert/div/div/div[1]/span[2]"),"Dados salvos com sucesso!"))

    context.driver.quit()