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
  4. In the code main.oy , find where Spotify credentials are initialized and replace the placeholder with your credentials.

## 📦 Requirements
  Before running the app make sure you install the following Python packages:
  ```bash
  - pip install pandas streamlit
  - pip install transformers spotipy
```
## 🚀 How to Run

### 1.Clone the repository
```bash
git clone https://github.com/rai-harshit01/ai-mood-playlist-generator.git
cd ai-mood-playlist-generator
```
### 2.Install Required Packages
Make sure Python 3.7 or higher is installed. Then install the dependencies given under Requirements

### 3.Set Up Spotipy Credentials 
Follow the instrucions given under Spotify API Setup

### 4.Run the APP
use the command below to start the Streamlit app:
```bash
streamlit run app.py
```
### 5.Use the APP
- A browser tab will open at http://localhost:8501

- Enter a sentence describing your mood (e.g., "I feel so happy today!")

- Click 🎶 Generate Playlist

- The app will:

  - Detect your emotion using Hugging Face
  
  - Suggest a matching Spotify playlist
  
  - Show a link you can open directly in Spotify
  
  - Not happy with the playlist? Click "Don't like it? Show another"




