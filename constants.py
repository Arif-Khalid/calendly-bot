# Bot variables
LOAD_TIME_SECONDS=10
TIME_BETWEEN_REFRESH_SECONDS=1

# Booking variables
DAY=14
MONTH=7
YEAR=2025
BASE_URL="https://calendly.com/tabletennis-smrt/smrt-tabletennisbooking"
EMAIL="example@gmail.com"

# To be left alone unless website changes
MONTH_STRING=str(YEAR) + '-' + str(MONTH).rjust(2, "0")
URL=f"{BASE_URL}?month={MONTH_STRING}"
