import streamlit as st
from transformers import pipeline
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Initialize Spotify API with client credentials for playlist access
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="INSERT YOUR SPOTIFY CLIENT ID HERE",
    client_secret="INSERT YOUR CLIENT SECRET HERE"
))

# Load the emotion classification model from Hugging Face with caching
@st.cache_resource
def load_pipeline():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        device=-1,
        return_all_scores=True
    )

emotion_pipeline = load_pipeline()

# Analyze the input text and return the most confident emotion label
def analyze_emotion(text):
    result = emotion_pipeline(text)[0]
    sorted_result = sorted(result, key=lambda x: x['score'], reverse=True)
    return sorted_result[0]['label'], sorted_result

# Search for Spotify playlists based on the detected emotion
def search_playlists(emotion):
    try:
        results = sp.search(q=emotion + " playlist", type='playlist', limit=10)
        playlists = []

        if results and 'playlists' in results and 'items' in results['playlists']:
            for item in results['playlists']['items']:
                if item and 'name' in item and 'external_urls' in item:
                    playlists.append({
                        'name': item['name'],
                        'url': item['external_urls']['spotify']
                    })

        if not playlists:
            playlists.append({
                'name': 'No playlist found 😢',
                'url': 'https://open.spotify.com/'
            })

        random.shuffle(playlists)
        return playlists

    except Exception as e:
        return [{
            'name': f'Error fetching playlist: {e}',
            'url': 'https://open.spotify.com/'
        }]

# Map detected emotions to corresponding emojis for better visual feedback
emotion_emojis = {
    "joy": "😊",
    "anger": "😠",
    "sadness": "😢",
    "love": "❤️",
    "fear": "😨",
    "surprise": "😲"
}

# Configure Streamlit UI and initialize session state variables
st.set_page_config(page_title="AI Mood-Based Playlist Generator", page_icon="🎧")
st.markdown("""
    <h1 style='text-align: center; color: #1DB954;'>🎧 AI Mood-Based Playlist Generator</h1>
""", unsafe_allow_html=True)

if 'emotion' not in st.session_state:
    st.session_state.emotion = None
if 'playlists' not in st.session_state:
    st.session_state.playlists = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Styled input box
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

user_input = st.text_input("Describe your mood or how you're feeling:")

# Styled generate button
if st.button("🎶 Generate Playlist"):
    if not user_input.strip():
        st.warning("Please enter something about your mood.")
    else:
        emotion, scores = analyze_emotion(user_input)
        playlists = search_playlists(emotion)

        st.session_state.emotion = emotion
        st.session_state.playlists = playlists
        st.session_state.current_index = 0

# Display detected emotion and current playlist in styled format
if st.session_state.playlists:
    current = st.session_state.playlists[st.session_state.current_index]
    emoji = emotion_emojis.get(st.session_state.emotion.lower(), "🎶")

    st.markdown(f"""
        <div style='text-align: center; padding: 10px;'>
            <span style='font-size: 22px;'>Detected Emotion:</span><br>
            <span style='font-size: 32px; font-weight: bold; color: #1DB954;'>{emoji} {st.session_state.emotion}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style='background-color: #f4f4f4; border-radius: 10px; padding: 20px; margin: 20px 0; box-shadow: 0px 2px 8px rgba(0,0,0,0.1); text-align: center;'>
            <a href="{current['url']}" target="_blank" style="text-decoration: none; color: #000; font-size: 20px;">
                🎵 {current['name']}
            </a>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Don't like it? Show another"):
        st.session_state.current_index += 1
        if st.session_state.current_index >= len(st.session_state.playlists):
            st.session_state.current_index = 0

# Footer section centered and with smaller font
st.markdown("""
    <hr style='margin-top: 50px;'>
    <div style='text-align: center; font-size: 0.75rem;'>
        Made with ❤️ using <a href='https://huggingface.co/transformers/' target='_blank'>Transformers</a> and <a href='https://developer.spotify.com/documentation/web-api/' target='_blank'>Spotify</a>.
    </div>
""", unsafe_allow_html=True)
