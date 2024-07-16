from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def login(driver, username, password):
    driver.get('https://www.tiktok.com/login')
    time.sleep(2)
    
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    time.sleep(5)

def add_to_cart(driver, product_url, quantity, basket_id):
    driver.get(product_url)
    time.sleep(2)
    for _ in range(quantity):
        basket_button = driver.find_element(By.XPATH, f'//button[@data-basket-id="{basket_id}"]')
        basket_button.click()
        time.sleep(0.5)
        add_button = driver.find_element(By.XPATH, 'xpath ของปุ่มเพิ่มสินค้าลงตะกร้า')
        add_button.click()
        time.sleep(random.uniform(0.5, 1.5))

def checkout(driver, card_number, expiry_date, cvv):
    cart_url = 'url ของหน้าตะกร้าสินค้า'
    driver.get(cart_url)
    time.sleep(2)
    
    checkout_button = driver.find_element(By.XPATH, 'xpath ของปุ่มชำระเงิน')
    checkout_button.click()
    time.sleep(2)
    
    card_number_input = driver.find_element(By.NAME, 'card_number')
    card_number_input.send_keys(card_number)
    
    expiry_date_input = driver.find_element(By.NAME, 'expiry_date')
    expiry_date_input.send_keys(expiry_date)
    
    cvv_input = driver.find_element(By.NAME, 'cvv')
    cvv_input.send_keys(cvv)
    
    confirm_button = driver.find_element(By.XPATH, 'xpath ของปุ่มยืนยันการจ่ายเงิน')
    confirm_button.click()

def run_bot(username, password, product_url, quantity, basket_id, card_number, expiry_date, cvv):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    
    try:
        login(driver, username, password)
        add_to_cart(driver, product_url, quantity, basket_id)
        checkout(driver, card_number, expiry_date, cvv)
    finally:
        driver.quit()
