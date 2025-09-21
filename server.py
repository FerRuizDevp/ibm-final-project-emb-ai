from flask import Flask, request, jsonify, redirect, url_for
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Redirect home route to /emotionDetector with a default text
@app.route("/")
def home():
    default_text = "I think I am having fun"
    return redirect(url_for('emotionDetector', text=default_text))

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get("text", "").strip()
    if not text:
        text = "I think I am having fun"  # default sentence

    # Call your emotion detection function
    result = emotion_detector(text)

    # Format the response as requested
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted_response

if __name__ == "__main__":
    # Run the app on all network interfaces on port 5000
    app.run(host="0.0.0.0", port=5000)
