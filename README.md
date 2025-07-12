# 🎧 AI Mood-Based Playlist Generator
This project uses AI to detect your mood and generate a personalized playlist using Spotify.

## 🔥 Features
- Emotion detection using Hugging Face transformer (`distilroberta-base`)
- Spotify Web API integration for real-time playlist suggestions
- Streamlit frontend for interactive user experience
## 🔑 Spotify API Setup 
To use the Spotify Web API , follow these steps to get your credentiails:
  1. Visit the Spotify Developer Dashboard and log in.
  2. Click "Create an App" , and provide a name and a despcription.
  3. After creating thra app, you'll get :
     Cliend ID and Client Secret
  4. In the code , find where Spotify credentials are initialized and replace the placeholder with your credentials.

## 📦 Requirements
  Before running the app make sure you install the following Python packages:
    pip install pandas streamlit
    pip install transformers spotipy
## 🚀 How to Run

### Clone the repository
```bash
git clone https://github.com/rai-harshit01/ai-mood-playlist-generator.git
cd ai-mood-playlist-generator


