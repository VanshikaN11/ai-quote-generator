import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random

st.set_page_config(page_title="AI Mood-Based Quote Generator", page_icon="💬", layout="centered")

st.title("🌟 AI Mood-Based Quote Generator")
st.write("Type how you're feeling right now. I'll try to lift your spirits with the right words.")

# Input from user
user_input = st.text_area("💭 How are you feeling? (Example: I’m not feeling good, I’m excited, I feel stressed)")

# Quotes database
quote_database = {
    "Positive": [
        "✨ Believe you can and you're halfway there.",
        "🌞 Stay positive, work hard, and amazing things will happen.",
        "🚀 The best is yet to come—keep going!",
        "🌈 Every day may not be good, but there is something good in every day."
    ],
    "Negative": [
        "🌧 Every storm runs out of rain—this too shall pass.",
        "💪 Tough times never last, but tough people do.",
        "🕯 Darkness cannot drive out darkness; only light can do that.",
        "🌻 It's okay to feel down sometimes—don't give up."
    ],
    "Neutral": [
        "🚶 The journey of a thousand miles begins with a single step.",
        "🌿 A calm mind brings inner strength and confidence.",
        "🕰 Patience and persistence are key to success.",
        "🔄 Focus on the step in front of you, not the whole staircase."
    ]
}

# Sentiment Analysis using VADER
def detect_mood_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    score = sentiment['compound']

    if score >= 0.3:
        return "Positive"
    elif score <= -0.3:
        return "Negative"
    else:
        return "Neutral"

# Display results
if st.button("✨ Get My Quote"):
    if not user_input.strip():
        st.warning("⚠️ Please type something about your mood.")
    else:
        mood = detect_mood_vader(user_input)
        quote = random.choice(quote_database[mood])
        st.subheader(f"📝 Detected Mood: **{mood}**")
        st.success(quote)
