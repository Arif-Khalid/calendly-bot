# Does not perform final submission if true. Set to true when testing, set to False when using in production
DEV_MODE=False                   

# Bot variables
LOAD_TIME_SECONDS=10            # Main page load time
SHORT_LOAD_TIME_SECONDS=3       # How long to wait for things to become enabled after actions, should be adjusted to as short as possible for fast refreshes
TIME_BETWEEN_REFRESH_SECONDS=1
TIME_WAIT_AFTER_CLICK=1
USER_DATA_DIR="--user-data-dir=/home/arif/.config/google-chrome/Default"

# Booking variables
TIME="15:00"                    # Input in string of "HH:MM" in 24HR format. I.e. "14:00"
DAY=16
MONTH=7
YEAR=2025
BASE_URL="https://calendly.com/tabletennis-smrt/smrt-tabletennisbooking"
NAME="nicholas"
EMAIL="arifkhalid99@gmail.com"

# Website variables
# To be left alone unless website changes
MONTH_STRING=str(YEAR) + '-' + str(MONTH).rjust(2, "0")
URL=f"{BASE_URL}?month={MONTH_STRING}"
LOADING_ELEMENT_XPATH="//div[@data-testid='calendar-loader']"
TIME_BUTTON_XPATH=f"//button[@data-start-time='{TIME}']"
NEXT_BUTTON_XPATH=f"//button[@aria-label='Next {TIME}']"
SUBMIT_BUTTON_XPATH="//button[@type='submit']"
