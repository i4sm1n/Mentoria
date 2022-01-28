from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

@given('a user logged on Lead’s platform, on internal mail page #1')
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

    time.sleep(5)

    intMail_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/nav/ul/div/li[4]/a[1]")
    intMail_btn.click()

    time.sleep(3)

@when('the user fill the required fields on tab ‘New message’ and send the mail')
def when(context):
    newMessage_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[1]/app-intern-mail-tabs/ul/li[3]")
    newMessage_btn.click()

    mail_field = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/app-new-intern-message/div/form/div/div[1]/div[2]/ng-select/div/div/div[2]/input")
    mail_field.send_keys("IASMIN TESTE")

    mail_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/app-new-intern-message/div/form/div/div[1]/div[2]/ng-select/ng-dropdown-panel")
    mail_btn.click()


    title_field = context.driver.find_element_by_id("messageSubject")
    title_field.send_keys("teste automatizado")

    body_field = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/app-new-intern-message/div/form/div/div[3]/div/app-text-editor/div/form/div[1]/div/div[2]/div[3]/div[2]")
    body_field.send_keys("Teste automatizado")

    body_field.click()
    body_field.send_keys(Keys.PAGE_DOWN)

    send_btn = context.driver.find_element_by_id("btn-send")
    send_btn.click()

    time.sleep(3)

@then('the system adds the submission to the sent list')
def then(context):
    search_field = context.driver.find_element_by_id("subject")
    search_field.send_keys("teste automatizado")

    search_btn = context.driver.find_element_by_id("btn-search")
    search_btn.click()

    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/form/div[2]/table/tbody/tr/td[3]")))

    context.driver.quit()