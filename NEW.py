from time import sleep
import sleep




def slow_print(text, delay=0.002):
    """Function to simulate typing text gradually."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
