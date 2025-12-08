import time
import sys

def slow_print(text, delay=0.01):
    """
    Print text letter by letter (typewriter effect)
    delay: seconds between characters (0.03 = 30ms)
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()