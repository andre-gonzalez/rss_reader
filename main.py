# commitar no git
# escrever testes
# ver como o Pauldo documento output da função e essas coisas e fazer igual
from logging_config import setup_logging
from rss_reader.app import RSSReaderApp

logger = setup_logging()

if __name__ == "__main__":
    try:

        logger.info("Starting the RSS Reader application")

        url = input("Enter feed URL: ")

        if not url:
            logger.warning("Received empty URL")
            exit("There was no URL provided, exiting the program...")

        logger.info(f"User entered feed URL: {url}")

        app = RSSReaderApp(url)
        app.run()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
