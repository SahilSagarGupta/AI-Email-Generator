from flask import Flask, render_template, request, session, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv
import os
import secrets

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


@app.route("/", methods=["GET", "POST"])
def home():
    generated_email = ""

    if request.method == "POST":
        topic = request.form["topic"]
        tone = request.form["tone"]
        recipient = request.form["recipient"]
        length = request.form["length"]
        language = request.form["language"]

        length_map = {
            "Short": "Keep it concise, under 100 words.",
            "Medium": "Keep it around 150-200 words.",
            "Long": "Write a detailed email, around 300+ words."
        }

        prompt = f"""
Write a {tone} email about '{topic}'.
Recipient: {recipient}
Length: {length_map[length]}
Write the email in {language}.
Include subject line at top.
Address recipient professionally.
"""

        response = model.generate_content(prompt)
        generated_email = response.text

        # Save History
        if "history" not in session:
            session["history"] = []

        session["history"] = ([{
            "topic": topic,
            "tone": tone,
            "recipient": recipient,
            "length": length,
            "language": language,
            "email": generated_email
        }] + session["history"])[:5]

        session.modified = True

    history = session.get("history", [])

    return render_template(
        "index.html",
        email=generated_email,
        history=history
    )


@app.route("/clear_history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)