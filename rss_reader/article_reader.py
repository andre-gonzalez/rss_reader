import pydoc

import html2text

from logging_config import setup_logging

logger = setup_logging()


class ArticleReader:
    """Converts HTML content of articles to plain text and displays it."""

    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        logger.info("ArticleReader initialized with link conversion enabled.")

    def parse_html(self, html_content):
        """Convert HTML content to plain text and display it."""
        if not html_content:
            logger.warning("Received empty HTML content.")
            return

        try:
            logger.info("Parsing HTML to plain_text")
            plain_text = self.converter.handle(html_content)
            logger.info("Displaying the article as plain_text")
            pydoc.pager("\n" + plain_text)
            logger.info("HTML content successfully converted and displayed.")
        except Exception as e:
            logger.error(f"Error converting html content: {e}")
