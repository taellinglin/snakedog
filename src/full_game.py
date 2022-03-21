# run file

import config
import logging

from game import Game

logging.info("Starting the game")

game = Game()

game.main()

logging.info("main loop exited")
