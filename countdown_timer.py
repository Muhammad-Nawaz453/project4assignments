import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'.format(mins, secs)
        print(timer, end='\r')  # Overwrites the previous line
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

# Taking input from the user
time_in_seconds = int(input("Enter countdown time in seconds: "))
countdown_timer(int(time_in_seconds))