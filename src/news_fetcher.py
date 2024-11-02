import openai
import requests

def fetch_news_data(news_api_key):
    # create news api url
    news_api_url = "https://newsapi.org/v2/top-headlines?category=politics&apiKey=" + news_api_key
    news_data = requests.get(news_api_url).json()
    return news_data

def generate_daily_update(news_api_key):
    news_data = fetch_news_data(news_api_key)
    print("News data received successfully")

    # Define the prompt with the latest data
    prompt = (
        f"Provide a concise daily update on the election with at least 5 numbered bullet points and including sources. Here’s the latest election news data: {news_data}."
    )

    # Generate summary with ChatGPT
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an election update bot providing a morning summary."},
            {"role": "user", "content": prompt}
        ]
    )

    message_content = response.choices[0].message.content
    print(message_content)

    return message_content