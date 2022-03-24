import logging
import sys

fmt = "[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s"

logging.basicConfig(
    filename="game.debug.log", level=logging.DEBUG, filemode="w", format=fmt
)
logging.info("loaded logger from config")

root = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
root.addHandler(handler)
