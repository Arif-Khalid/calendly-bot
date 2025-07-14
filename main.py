from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from constants import BASE_URL, DAY, MONTH, MONTH_STRING, TIME_BETWEEN_REFRESH_SECONDS, URL, LOAD_TIME_SECONDS, YEAR

print("Hello World")
driver = webdriver.Chrome()
driver.implicitly_wait(LOAD_TIME_SECONDS)

# Returns true if booking was successful, otherwise return false
def make_booking():
    driver.get(URL)
    # Calendar_cells are found first to force webpage to be implicitly loaded, thereby updating the current_url before we check
    calendar_cells = driver.find_elements(By.TAG_NAME, "td")

    # Check month and year as specified in queryParam of url, updated from inputted url once page loads
    if(not MONTH_STRING in driver.current_url):
        print(f"Error: Booking in {MONTH_STRING} not currently available")
        return False

    # Find day in calendar
    button_to_press = None
    for calendar_cell in calendar_cells:
        calendar_button = calendar_cell.find_element(By.TAG_NAME, "button")
        button_text = calendar_button.find_element(By.TAG_NAME, "span").text
        if(not button_text):
            continue
        if(int(button_text) == DAY):
            button_to_press = calendar_button
            break

    if(not button_to_press or not button_to_press.is_enabled()):
        print(f"Error: Booking in {str(DAY)} of {MONTH_STRING} not currently available")
        return False

    button_to_press.click()

    # TODO: Input information
    return True

while(True):
    if(make_booking()):
        break

    print(f"Waiting {TIME_BETWEEN_REFRESH_SECONDS} seconds before retry")
    time.sleep(TIME_BETWEEN_REFRESH_SECONDS)

print(f"Successfully booked {DAY}/{MONTH}/{YEAR}")
