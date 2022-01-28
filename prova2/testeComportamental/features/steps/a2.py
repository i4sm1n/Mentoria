from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


@given('a user logged on Lead’s platform, on internal mail page #2')
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

    intMail_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/nav/ul/div/li[4]/a[1]")
    intMail_btn.click()

    time.sleep(3)

@when('the user selects all items from the sent list, clicks on “Delete” and confirm the exclusion')
def when(context):
    sent_tab_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[1]/app-intern-mail-tabs/ul/li[2]/div")
    sent_tab_btn.click()

    time.sleep(3)

    select_all_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/form/div[2]/table/thead/tr/th[1]/div/label")
    select_all_btn.click()

    delete_btn = context.driver.find_element_by_id("btn-delete")
    delete_btn.click()

    confirm_btn = context.driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-delete-modal/div[3]/button[2]")
    confirm_btn.click()

    time.sleep(3)

@then('the system shows the empty sent list')
def then(context):
    search_field = context.driver.find_element_by_id("subject")
    search_field.send_keys("teste automatizado")

    search_btn = context.driver.find_element_by_id("btn-search")
    search_btn.click()

    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/form/div[2]/div/p"), "Resultado não encontrado")) # completar com xpath do campo no result e texto

    context.driver.quit()