import time
import random
from textblob import TextBlob  # A sentiment analysis library for simplicity

def compliment_to_timer(compliment):
    # Analyze sentiment
    sentiment = TextBlob(compliment).sentiment.polarity

    # Create timer duration based on sentiment
    timer_duration = max(int(sentiment * 20), random.randint(10, 30))

    print(f"Your timer is set for {timer_duration} seconds!")
    time.sleep(timer_duration)
    print("Time's up! Hope your eggs are… cooked emotionally!")

# Example usage
user_input = input("Give me a compliment: ")
compliment_to_timer(user_input)