from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Step 1: Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Step 2: Add a product to cart
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    time.sleep(2)

    # Step 3: Validate Add to Cart
    assert driver.find_element(By.XPATH, "//button[text()='Remove']"), "Add to cart failed!"
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1", "Cart badge count mismatch!"

    # Step 4: Navigate to Cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Step 5: Validate Cart Information
    assert "Sauce Labs" in driver.page_source, "Product details missing in cart!"

    # Step 6: Click Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    # Step 7: Fill Checkout Information
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Step 8: Validate Checkout Information
    assert "Sauce Labs" in driver.page_source, "Product details missing at checkout!"

    # Step 9: Click Finish
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # Step 10: Validate Checkout Completion
    assert "Checkout: Complete!" in driver.page_source, "Checkout completion message missing!"

    print("Test Passed: All steps completed successfully!")
    driver.quit()

if __name__ == "__main__":
    test_saucedemo()
