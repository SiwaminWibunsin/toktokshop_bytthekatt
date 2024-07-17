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

def add_to_cart(driver, product_url, quantity, basket):
    driver.get(product_url)
    time.sleep(2)
    for _ in range(quantity):
        # คลิกเลือกสินค้าจากตะกร้า
        basket_button = driver.find_element(By.XPATH, f'//xpath ของปุ่มเลือกตะกร้า[{basket}]')
        basket_button.click()
        time.sleep(1)
        
        # เลือกตัวเลือกสินค้า
        option_button = driver.find_element(By.XPATH, 'xpath ของตัวเลือกสินค้า')
        option_button.click()
        time.sleep(1)

        add_button = driver.find_element(By.XPATH, '//button[contains(text(), "ซื้อ")]')
        add_button.click()
        time.sleep(random.uniform(0.5, 1.5))

def checkout(driver, card_number, expiry_date, cvv):
    cart_url = 'https://www.tiktok.com/cart'
    driver.get(cart_url)
    time.sleep(2)
    
    checkout_button = driver.find_element(By.XPATH, '//button[contains(text(), "ทำการสั่งซื้อ")]')
    checkout_button.click()
    time.sleep(2)
    
    # เลือกวิธีการชำระเงิน
    payment_option = driver.find_element(By.XPATH, 'xpath ของวิธีการชำระเงินที่ต้องการ')
    payment_option.click()
    time.sleep(1)

    if payment_option == "Visa":
        card_number_input = driver.find_element(By.NAME, 'card_number')
        card_number_input.send_keys(card_number)
        
        expiry_date_input = driver.find_element(By.NAME, 'expiry_date')
        expiry_date_input.send_keys(expiry_date)
        
        cvv_input = driver.find_element(By.NAME, 'cvv')
        cvv_input.send_keys(cvv)
    
    confirm_button = driver.find_element(By.XPATH, '//button[contains(text(), "ทำการสั่งซื้อ")]')
    confirm_button.click()

def run_bot(username, password, product_url, quantity, basket, card_number, expiry_date, cvv):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    
    try:
        login(driver, username, password)
        add_to_cart(driver, product_url, quantity, basket)
        checkout(driver, card_number, expiry_date, cvv)
    finally:
        driver.quit()
