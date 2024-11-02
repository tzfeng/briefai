from src import news_fetcher, emailer  # Importing main application functions
from src.config import load_config  # Configuration functions

def main():
    # Load configuration
    config = load_config()

    # Run the main application
    email_address = config["EMAIL_ADDRESS"]
    email_password = config["EMAIL_PASSWORD"]
    recipient_email = config["RECIPIENT_EMAIL"]
    smtp_server = config["SMTP_SERVER"]
    smtp_port = int(config["SMTP_PORT"])
    news_api_key = config["NEWS_API_KEY"]

    update_content = news_fetcher.generate_daily_update(news_api_key)

    emailer.send_email_update(smtp_server, smtp_port, email_address, email_password, recipient_email, update_content)

if __name__ == "__main__":
    # Call the main function to start the program
    main()