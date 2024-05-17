from transformers import pipeline


sentiment_analysis = pipeline(
  "sentiment-analysis",
  framework="pt",
  model="SamLowe/roberta-base-go_emotions"
)

def analyze_sentiment(text):
  results = sentiment_analysis(text)
  sentiment_results = {
    result['label']: result['score'] for result in results
  }
  return sentiment_results


def get_bubble_shape(sentiment):
  # Define the mapping of sentiments to bubble shapes
  # Normal - 0, Jagged - 1
  bubble_shape_mapping = {
    "disappointment": 0,
    "sadness": 0,
    "annoyance": 1,
    "neutral": 0,
    "disapproval": 0,
    "realization": 0,
    "nervousness": 1,
    "approval": 0,
    "joy": 0,
    "anger": 1,
    "embarrassment": 0,
    "caring": 0,
    "remorse": 0,
    "disgust": 1,
    "grief": 0,
    "confusion": 0,
    "relief": 0,
    "desire": 0,
    "admiration": 0,
    "optimism": 0,
    "fear": 1,
    "love": 0,
    "excitement": 1,
    "curiosity": 1,
    "amusement": 1,
    "surprise": 1,
    "gratitude": 0,
    "pride": 0
  }


  if bubble_shape_mapping.get(sentiment, "") == 0:
    return "normal"
  else:
    return "jagged"


def display_sentiment_results(sentiment_results, option):
  sentiment_text = ""
  for sentiment, score in sentiment_results.items():
    bubble_shape = get_bubble_shape(sentiment)
    if option == "Sentiment Only":
      sentiment_text += f"{bubble_shape}"
    elif option == "Sentiment + Score":
      sentiment_text += f"{bubble_shape}: {score}\n"
  return sentiment_text


def inference(sub, sentiment_option):
  sentiment_results = analyze_sentiment(sub)
  sentiment_output = display_sentiment_results(sentiment_results, sentiment_option)
  return sentiment_output

def get_bubble_type(dialogue):
    # print(dialogue)
    sentiment_option_choices = ["Sentiment Only", "Sentiment + Score"]
    default_sentiment_option = "Sentiment Only"
    sentiment_result = inference(dialogue, default_sentiment_option)
    # print("Sentiment Analysis Results:", sentiment_result)
    return sentiment_result