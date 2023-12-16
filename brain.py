from time import sleep

from flask import Flask, render_template, request, jsonify
from graphsOfwebsite import create_dash_application
from loan import loan_vis
from promt.chat import chatbot

app = Flask(__name__)
create_dash_application(app)
loan_vis(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prompt/", methods=['POST', 'GET'])
def prompt():
    return render_template("prompt.html")


@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']

    # Replace this with your chatbot logic
    # In a real-world scenario, you might call a function that interacts with your chatbot
    ai_response = chatbot(user_message)
    print(ai_response)
    # Simulate a delayed response for demonstration purposes
    sleep(1)

    return jsonify({'response': f"{ai_response}"})


if __name__ == "__main__":
    app.run()
