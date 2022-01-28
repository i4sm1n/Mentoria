from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


@given('a user logged on Lead’s platform, on edit profile page #1')
def given(context):
    context.driver = webdriver.Chrome("C:/Users/iasmi/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("iasmin.santos@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("1234abcd")

    enter_button = context.driver.find_element_by_id("login-btn")
    enter_button.click()

    time.sleep(3)

    profile_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/button/img")
    profile_btn.click()

    edit_profile_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/div/div[2]/div[1]/button")
    edit_profile_btn.click()

    time.sleep(3)

@when('modify the field ‘Escolha o idioma’ to ‘Inglês’ and save the change')
def when(context):
    language_field = context.driver.find_element_by_id("language")
    language_field.click()

    eng_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[7]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[1]")
    eng_btn.click()

    save_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[11]/button")
    save_btn.click()

@then('the system notifies the change and updates the page to English language')
def then(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/div/app-alert/div/div/div[1]/span[2]"), "Data saved successfully!"))

    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[1]/h3"),"Personal Information"))

    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[2]/div[1]/label"),"Profile picture")) #completar com xpath e mensagem de texto em ingles

    context.driver.quit()