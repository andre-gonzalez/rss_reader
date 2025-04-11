import feedparser

from logging_config import setup_logging
from rss_reader.article import Article

logger = setup_logging()


class RSSFeedReader:
    """Handles fetching and parsing of an RSS feed."""

    def __init__(self, url):
        self.url = url
        self.feed = None

    def fetch_feed(self):
        """Fetch and parse the RSS feed."""
        try:
            logger.info(f"Fetching RSS feed from: {self.url}")
            self.feed = feedparser.parse(self.url)
            if self.feed.bozo:
                logger.error(f"Error parsing feed: {self.feed.bozo_exception}")
            else:
                logger.info("Feed fetching RSS feed")
        except Exception as e:
            logger.error(f"Error fetching RSS feed: {e}")

    def get_articles(self, chunk_size=10):
        """Return articles in chunks."""
        if self.feed is None:
            logger.warning("Feed has not been fetched yet.")
            return

        articles = [
            Article(entry.title, entry.content[0].value) for entry in self.feed.entries
        ]

        logger.info(f"Returning {len(articles)} articles in chunks of {chunk_size}.")

        for i in range(0, len(articles), chunk_size):
            logger.debug(f"Returning chunk {i//chunk_size + 1} of articles.")
            yield articles[i : i + chunk_size]
