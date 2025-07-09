import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="AI Mood-Based Quote Generator", page_icon="🌈", layout="centered")

st.title("🌟 AI Mood-Based Quote Generator")
st.write("Type a sentence about how you're feeling right now, and I'll try to lift your spirits with the right words.")

# User input
user_input = st.text_area("💭 How are you feeling today? Share anything that's on your mind...")

# Expanded quotes library
quote_database = {
    "Positive": [
        "✨ Believe you can and you're halfway there.",
        "🌞 Stay positive, work hard, and amazing things will happen.",
        "🌈 Success is not in what you have, but who you are.",
        "🚀 The best is yet to come—keep going!"
    ],
    "Negative": [
        "🌧 Every storm runs out of rain—this too shall pass.",
        "💪 Tough times never last, but tough people do.",
        "🌻 Sometimes you win, sometimes you learn. Never give up.",
        "🕯 Darkness cannot drive out darkness; only light can do that."
    ],
    "Angry": [
        "😌 Speak when you are calm, not when you are angry.",
        "⏳ For every minute you remain angry, you lose 60 seconds of peace.",
        "🕊 Let go of anger—it doesn’t serve you.",
        "💭 Take a deep breath. You control how you respond."
    ],
    "Anxious": [
        "🌿 You don’t have to control your thoughts, just stop letting them control you.",
        "🧘 Worrying won’t stop the bad from happening, it just steals your joy.",
        "☀ Trust yourself—you’ve survived 100% of your worst days.",
        "🌙 Just breathe. You're stronger than you think."
    ],
    "Lonely": [
        "🤗 You are enough just as you are. You're not alone.",
        "🌸 Sometimes being alone allows you to rediscover yourself.",
        "💫 The night is darkest just before dawn.",
        "👥 Reach out. You’re always connected in ways you may not see."
    ],
    "Hopeful": [
        "🌟 Even the darkest night will end and the sun will rise.",
        "🌱 Hope is the thing with feathers that perches in the soul.",
        "🌞 Let your hopes, not your hurts, shape your future.",
        "✨ Every day is a new beginning—full of endless possibilities."
    ],
    "Neutral": [
        "🚶 The journey of a thousand miles begins with a single step.",
        "🌿 A calm mind brings inner strength and self-confidence.",
        "🕰 Patience and persistence are key to all success.",
        "🔄 Life is a balance of holding on and letting go."
    ]
}

# Expanded mood detection
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    if any(word in text_lower for word in ["angry", "mad", "furious", "irritated", "annoyed", "upset", "frustrated"]):
        return "Angry"
    elif any(word in text_lower for word in ["anxious", "worried", "scared", "nervous", "stressed", "tense", "panic"]):
        return "Anxious"
    elif any(word in text_lower for word in ["lonely", "alone", "isolated", "abandoned", "left out"]):
        return "Lonely"
    elif any(word in text_lower for word in ["hopeful", "optimistic", "excited", "eager", "looking forward"]):
        return "Hopeful"
    elif polarity > 0.3:
        return "Positive"
    elif polarity < -0.3:
        return "Negative"
    else:
        return "Neutral"

# Main logic
if st.button("✨ Get My Quote"):
    if user_input.strip() == "":
        st.warning("⚠️ Please type something about your feelings.")
    else:
        mood = detect_mood(user_input)
        quote = random.choice(quote_database[mood])
        st.subheader(f"📝 Detected Mood: **{mood}**")
        st.success(quote)


