# Program to test a contact form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

# Prompt the tester to type in test details.
rp_name = input("What is your roleplay name? REQUIRED BY FORM: ")
rp_email = input("Enter your roleplay email address. REQUIRED BY FORM: ")
rp_website = input("Enter a roleplay website: ")
rp_comment = input("Enter message. REQUIRED BY FORM: ")

#Let the user know they shouldn't shut down the program until it is finished running
print("Due to the dynamic nature of the contact form, it can take as much as 10 minutes to finish loading. Please don't shut down the program until you receive confirmation of whether or not the test has passed or failed.")

# Connect to the browser and web page
driver = webdriver.Chrome()
driver.get("https://thefoolsays.wordpress.com/contact/")

# Find form elements
name = driver.find_element(By.NAME, "g10-name")
email = driver.find_element(By.NAME, "g10-email")
comment = driver.find_element(By.NAME, "g10-comment")
website = driver.find_element(By.NAME, "g10-website")

# Declare input values and also check if forms have been filled in
name.send_keys(rp_name)
email.send_keys(rp_email)
website.send_keys(rp_website)
comment.send_keys(rp_comment)

# Accept cookies. The cookie menu sometimes prevents automated scripts from running
wp_cookie = driver.find_element(By.CLASS_NAME, "accept")
wp_cookie.click()

# Explicit wait for all form fields to be filled, just in case
wait = WebDriverWait(driver, 10)

# Wait for each input field to have a non-empty value
wait.until(conditions.text_to_be_present_in_element_value((By.NAME, "g10-name"), rp_name))
wait.until(conditions.text_to_be_present_in_element_value((By.NAME, "g10-email"), rp_email))
wait.until(conditions.text_to_be_present_in_element_value((By.NAME, "g10-website"), rp_website))
wait.until(conditions.text_to_be_present_in_element_value((By.NAME, "g10-comment"), rp_comment))

# Find and click the submit button
submit_button = driver.find_element(By.CLASS_NAME, "pushbutton-wide")
submit_button.click()

# Print something to the screen if the operation was successful
if "Your message has been sent" in driver.page_source:
    print("Test passed")
else:
    print("Test failed")

# Close the browser
driver.quit()