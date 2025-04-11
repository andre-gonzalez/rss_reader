from logging_config import setup_logging
from rss_reader.article_reader import ArticleReader
from rss_reader.rss_feed_reader import RSSFeedReader

logger = setup_logging()


class RSSReaderApp:
    """Main application that ties the classes together and runs the program."""

    def __init__(self, url):
        self.rss_reader = RSSFeedReader(url)
        self.article_reader = ArticleReader()
        logger.info(f"Initialized RSSReaderAPP with URL: {url}")

    def run(self):
        """Run the main logic of fetching and displaying articles."""
        try:
            logger.info("Fetching RSS feed...")
            self.rss_reader.fetch_feed()
            chunk_size = 10
            logger.info("Set chunk_size to {chunk_size}")

            for chunk in self.rss_reader.get_articles(chunk_size):
                logger.info("Displaying {len(chunk)} articles")

                for idx, article in enumerate(chunk, start=1):
                    print(f"{idx} - {article.title}")

                user_input = input(
                    "\nPress Enter to see more or type 'q' to quit or type the number of the article you want to read: "
                )
                logger.info(f"User provided input {user_input}")

                if user_input.lower() == "q":
                    logger.info("User chose to quit the application.")
                    break


                if user_input.isnumeric():
                    selected_index = int(user_input) - 1
                    if 0 <= selected_index < len(chunk):
                        selected_article = chunk[selected_index]
                        logger.info(f"User selected article: {selected_article.title}")
                        self.article_reader.parse_html(selected_article.content)
                        # Ask the user if they want to continue or quit after reading
                        continue_input = input(
                            "\nPress Enter to see more articles or 'q' to quit: "
                        )
                        logger.info(f"User input after reading article: {continue_input}")
                        if continue_input.lower() == "q":
                            logger.info("User chose to quit the application after reading an article.")
                            break
                    else:
                        logger.warning("User provided invalid article number")
                        print("Invalid article number. Please try again.")

                else:
                    logger.warning("User provided invalid input")
                    print("Invalid input. Please enter a valid number or 'q' to quit.")
        except Exception as e:
            logger.error(f"Error {e}")
