import logging

import config
from game import Game


def main():
    logging.info("Starting game")
    # All logic goes here
    game = Game()

    game.main()

    logging.info("Exiting game")
