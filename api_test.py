import requests
import pyttsx3

# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=f536e3fe97c0444d88418a41d9f3d0d7')
# response = requests.get(url)
# a=response.json()
# articles = a.get('articles', [])
# for i,article in enumerate(articles):
#     print(f"{i}: {article['title']}")




# import requests

# Replace with your News API key
api_key = "f536e3fe97c0444d88418a41d9f3d0d7"

# Define the endpoint and parameters
url = "https://newsapi.org/v2/top-headlines?"
params = {
    "country": "us",  # Change the country code as needed
    "category": "technology",  # Choose a category (e.g., business, entertainment, etc.)
    "apiKey": api_key
}

# Fetch the news
response = requests.get(url, params)

# Check if the request was successful
# if response.status_code == 200:
news_data = response.json()  # Parse the JSON response

    # Display the top headlines
print("Top Headlines:\n")
for index, article in enumerate(news_data['articles'], start=1):
        print(f"{index}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}\n")
# else:
#     print(f"Failed to fetch news. HTTP Status Code: {response.status_code}")


# import requests


# def fetch_and_speak_news():
#     # Replace with your News API key
#     api_key = "f536e3fe97c0444d88418a41d9f3d0d7"

#     # Define the endpoint and parameters
#     url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-24&sortBy=publishedAt&apiKey"
#     params = {
#         "country": "india",  # Change the country code as needed
#         "category": "technology",  # Choose a category (e.g., business, entertainment, etc.)
#         "apiKey": api_key
#     }

#     # Fetch the news
#     response = requests.get(url, params=params)

#     # Initialize the TTS engine
#     engine = pyttsx3.init()

#     # Check if the request was successful
#     if response.status_code == 200:
#         news_data = response.json()  # Parse the JSON response

#         # Display and speak the top headlines
#         print("Top Headlines:\n")
#         for article in enumerate(news_data["articles"], start=1):
#             title = article['title']
#             # source = article['source']['name']
#             # headline = f"{index}. {title} (Source: {source})"
            
#             print(title)
            
#             # Use TTS to speak the headline
#             engine.say(title)
#         engine.runAndWait()
        
#         # Wait for TTS to finish
        
#     else:
#         error_message = f"Failed to fetch news. HTTP Status Code: {response.status_code}"
#         print(error_message)
#         engine.say(error_message)
#         engine.runAndWait()

# # Call the function
# fetch_and_speak_news()

