# Calendly bot
This bot is used to automatically make a booking on calendly. Should be modified appropriately for different params of different bookings

# Setup
1. Clone this repo into a directory. For example `your_dir/calendly-bot/`.
2. Install python3 if not already installed
    * Check by performing `python3 -V` in the terminal
    * The program is only ran and tested on `Python 3.13.5`, but should run fine on most versions
3. Create virtual environment and install required packages
    * Navigate to the directory by typing `cd your_dir/calendly-bot` and pressing enter in a terminal
    * Type `python3 -m venv .venv` and press enter which creates the virtual env
    * Activate the venv by running typing `./venv/Scripts/activate` and press enter (this is for Windows OS) [For non-windows](https://docs.python.org/3/tutorial/venv.html)
    * Install from requirements.txt file by typing `pip install -r requirements.txt` and press enter
4. Adjust variables to your requirements
    * Open `your_dir/constants.py` in your favourite text editor
    * Ensure DEV_MODE is False
    * Change the commented `Booking variables` as required

# Running the code
1. Navigate to the repo directory as in step 3 of the setup
2. Type `.venv/Scripts/python.exe main.py` and press enter
3. Use Cntrl-C to quit the program from the terminal you ran it from when required as it runs endlessly until a successful booking is made

# Additional information
* If you see availability but the bot always refreshes without clicking through, lengthen SHORT_LOAD_TIME_SECONDS by 1 or 2 seconds
* If you want to run the bot without opening a chrome window, set IS_HEADLESS to True
