import twint
import time

# NOTES

# Open Terminal on Ubuntu
# Execute `cd /mnt/c/Users/Labyrinth/Desktop/twint/`
# Execute python3 MAIN.py
# To kill it, CTRL+C

# Config: https://github.com/twintproject/twint/wiki/Configuration

# To add an option, do this:
# c.{ParameterName} = {parameterValue}
# Examples:
# c.{String Parameter} = "value"
# c.{Bool Parameter} = True or False
# c.{Integer Parameter} = 42

# Parameters
OUTPUT_CSV = "OUTPUT/metinelas.csv"
RESUME_FILE = "OUTPUT/resume_file.txt"
SLEEP_TIME = 3 # seconds


# Configure
c = twint.Config()

#c.Username = "stdaste"
c.Search = ("#Με_την_ΕΛΑΣ")
c.Since = "2021-03-07"
c.Until = "2021-03-11"
c.Count = True
c.Limit = 100
c.Show_hashtags = True
#c.Popular_tweets = True

#c.Min_replies = 5

c.Lang = "el"
c.Hide_output = True

c.Resume = RESUME_FILE
c.Store_csv = True
c.Output = OUTPUT_CSV

# Run
while True:
    # twint.run.Followers(c)
    twint.run.Search(c)

    try:
        with open(OUTPUT_CSV) as f:
            total = len(f.readlines())-1
            print(f"Total tweets: {total}")
    except:
        pass

    sleep_msg = f"Sleeping for {SLEEP_TIME} seconds."
    print(f"Sleeping for {SLEEP_TIME} seconds.")
    print("=" * len(sleep_msg) * 2) 
    time.sleep(SLEEP_TIME)
