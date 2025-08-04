# Does not perform final submission if true. Set to true when testing, set to False when using in production
DEV_MODE=False                 

# Bot variables
LOAD_TIME_SECONDS=10                # Main page load time
SHORT_LOAD_TIME_SECONDS=1           # How long to wait for things to become enabled after actions, should be adjusted to as short as possible for fast refreshes
TIME_WAIT_AFTER_CLICK=0             # Used if need to simulate a real user, deemed unceccesary for calendly
SELENIUM_POLLING_TIME_SECONDS = 0.1 # Seconds between each check of wait conditional for short load times, default is 0.5
IS_HEADLESS=False                   # Whether you want to see what the bot does. Set to True if you want it to run in the background.

# Booking variables
TIME="10:00"                        # Input in string of "HH:MM" in 24HR format. I.e. "14:00"
DAY=16
MONTH=8
YEAR=2025
NAME="john"
EMAIL="arifkhalid99@gmail.com"
BASE_URL="https://calendly.com/tabletennis-smrt/smrt-tabletennisbooking"

# Website variables
# To be left alone unless website changes
MONTH_STRING=str(YEAR) + '-' + str(MONTH).rjust(2, "0")
URL=f"{BASE_URL}?month={MONTH_STRING}"
LOADING_ELEMENT_XPATH="//div[@data-testid='calendar-loader']"
TIME_BUTTON_XPATH=f"//button[@data-start-time='{TIME}']"
NEXT_BUTTON_XPATH=f"//button[@aria-label='Next {TIME}']"
SUBMIT_BUTTON_XPATH="//button[@type='submit']"
SCHEDULED_SUCCESS_MESSAGE_XPATH="//h1[contains(text(), 'You are scheduled')]"
