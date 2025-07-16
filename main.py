from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

from constants import BASE_URL, DAY, DEV_MODE, EMAIL, MONTH, MONTH_STRING, NAME, NEXT_BUTTON_XPATH, SHORT_LOAD_TIME_SECONDS, SUBMIT_BUTTON_XPATH, TIME, TIME_BETWEEN_REFRESH_SECONDS, TIME_BUTTON_XPATH, TIME_WAIT_AFTER_CLICK, URL, LOAD_TIME_SECONDS, USER_DATA_DIR, YEAR

options = webdriver.ChromeOptions()
options.add_argument(USER_DATA_DIR)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(LOAD_TIME_SECONDS)
wait = WebDriverWait(driver, LOAD_TIME_SECONDS)

# Returns true if booking was successful, otherwise return false
def make_booking():
    driver.get(URL)
    # Calendar_cells are found first to force webpage to be implicitly loaded, thereby updating the current_url before we check
    wait.until(lambda _ : driver.find_elements(By.TAG_NAME, "td"))
    calendar_cells = driver.find_elements(By.TAG_NAME, "td")

    # Check month and year as specified in queryParam of url, updated from inputted url once page loads
    if(not MONTH_STRING in driver.current_url):
        raise Exception(f"Booking in {MONTH_STRING} not currently available.")

    # Find day in calendar
    def get_calendar_button():
        button_to_press = None
        for calendar_cell in calendar_cells:
            calendar_button = calendar_cell.find_element(By.TAG_NAME, "button")
            button_text = calendar_button.find_element(By.TAG_NAME, "span").text
            if(not button_text):
                continue
            if(int(button_text) == DAY):
                button_to_press = calendar_button
                break
        if(not button_to_press):
            raise TimeoutException
        WebDriverWait(driver, SHORT_LOAD_TIME_SECONDS).until(lambda _ : button_to_press.is_enabled())
        return button_to_press

    def get_next_button():
        WebDriverWait(driver, SHORT_LOAD_TIME_SECONDS).until(lambda _ : driver.find_element(By.XPATH, TIME_BUTTON_XPATH))
        time_button = driver.find_element(By.XPATH, TIME_BUTTON_XPATH)
    
        time_button.click()
        time.sleep(TIME_WAIT_AFTER_CLICK)
        WebDriverWait(driver, SHORT_LOAD_TIME_SECONDS).until(lambda _ : driver.find_element(By.XPATH, NEXT_BUTTON_XPATH))
        next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
        next_button.click()
        time.sleep(TIME_WAIT_AFTER_CLICK)
   
    def input_details_and_confirm():
        def send_keys_slow(inputElem, keys):
            for c in keys:
                inputElem.send_keys(c)
                time.sleep(0.2)
        WebDriverWait(driver, SHORT_LOAD_TIME_SECONDS).until(lambda _ : driver.find_element(By.TAG_NAME, "input"))
        nameInput, emailInput, *_ = driver.find_elements(By.TAG_NAME, "input")
        send_keys_slow(nameInput, NAME)
        # nameInput.send_keys(NAME)
        send_keys_slow(emailInput, EMAIL)
        # emailInput.send_keys(EMAIL)
        submitButton = driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH)
        if(DEV_MODE):
            # Stay at final page for debugging purposes
            while(1):
                pass
        else:
            submitButton.click()
            while(1):
                pass

    # Wait for loading to finish, which will enable the button if there are slots
        
    try:
        button_to_press = get_calendar_button()
    except (TimeoutException, NoSuchElementException):
        raise Exception(f"Booking in {str(DAY)} of {MONTH_STRING} not currently available.")
        
    button_to_press.click()
    time.sleep(TIME_WAIT_AFTER_CLICK)
    
    try:
        get_next_button()
    except (TimeoutException, NoSuchElementException):
        raise Exception(f"Booking of time {TIME} in {str(DAY)} of {MONTH_STRING} not currently available.")
    
    try:
        input_details_and_confirm()
    except (TimeoutException, NoSuchElementException):
        raise Exception("Final stage of inputting name and email error. Likely caused by someone sniping the slot or the webpage changed")
    return True

while(True):
    try:
        if(make_booking()):
            break

        print(f"Waiting {TIME_BETWEEN_REFRESH_SECONDS} seconds before retry")
        time.sleep(TIME_BETWEEN_REFRESH_SECONDS)

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

print(f"{Fore.GREEN}Successfully booked {DAY}/{MONTH}/{YEAR}{Style.RESET_ALL}")
