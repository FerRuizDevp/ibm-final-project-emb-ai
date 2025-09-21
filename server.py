"""
Flask server for the Emotion Detection App.
"""

from flask import Flask, request, redirect, url_for
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Redirect root route to /emotion_detector with a default text.
    """
    default_text = "I think I am having fun"
    return redirect(url_for("emotion_detector_route", text=default_text))


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle the /emotionDetector route.
    Takes user text input as query parameter,
    calls the emotion_detector function, and returns formatted results.
    """
    text = request.args.get("text", "").strip()

    # Call emotion detection function
    result, status_code = emotion_detector(text)

    # Handle blank or invalid input
    if status_code == 400 or result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    # Format the response
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
    app.run(host="0.0.0.0", port=5000)
