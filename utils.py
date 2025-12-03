import time
import random

def simulate_delay(min_sec=0.2, max_sec=0.7):
    time.sleep(random.uniform(min_sec, max_sec))

def random_click_simulation():
    # Higher chance: ignore email
    return random.choice([False, False, False, True])
