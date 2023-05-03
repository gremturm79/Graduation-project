import sys
from time import sleep
# from typing import Tuple

DELAY: float = .06  # Change this to speed up/slow down typewriting speed


def typewrite(*paragraph: str) -> None:
    """This function mimics a typewriting effect by printing strings letter by letter.
    Args:
        *paragraph -- variable length args of setences to typewrite
    """
    for sentence in paragraph:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(DELAY)
        print()
        sleep(DELAY)


# Usage (you can put as many sentences as you want)
typewrite(
    "Hello World!",
    "Another Sentence.",
)
