import logging
from server import app


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    logger.info('hello world')


if __name__=="__main__":
    app.run(debug=True)
