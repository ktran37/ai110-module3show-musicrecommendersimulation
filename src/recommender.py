import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    loaded_songs = []
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
        # reader automatically reads the first row as keys
        reader = csv.DictReader(f)
        
        # Clean up whitespace in header keys
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        
        for row in reader:
            song = {
                "id": int(row["id"].strip()),
                "title": row["title"].strip(),
                "artist": row["artist"].strip(),
                "genre": row["genre"].strip(),
                "mood": row["mood"].strip(),
                "energy": float(row["energy"].strip()),
                "tempo_bpm": float(row["tempo_bpm"].strip()),
                "valence": float(row["valence"].strip()),
                "danceability": float(row["danceability"].strip()),
                "acousticness": float(row["acousticness"].strip())
            }
            loaded_songs.append(song)
            
    return loaded_songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    
    Algorithm Recipe (Scoring Logic):
    - Genre Match: +2.0 points if song.genre == user.favorite_genre
    - Mood Match: +1.0 point if song.mood == user.favorite_mood
    - Energy Proximity: +1.0 point max (1.0 - absolute difference between song.energy and user.target_energy)
    - Danceability Proximity: +1.0 point max (1.0 - absolute difference between song.danceability and user.target_danceability)
    """
    score = 0.0
    reasons = []

    # Genre Match
    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # Mood Match
    if song.get("mood") == user_prefs.get("favorite_mood"):
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # Energy Proximity
    if "energy" in song and "target_energy" in user_prefs:
        energy_diff = abs(song["energy"] - user_prefs["target_energy"])
        energy_points = max(0.0, 1.0 - energy_diff)
        score += energy_points
        reasons.append(f"Energy proximity (+{energy_points:.2f})")

    # Danceability Proximity
    if "danceability" in song and "target_danceability" in user_prefs:
        dance_diff = abs(song["danceability"] - user_prefs["target_danceability"])
        dance_points = max(0.0, 1.0 - dance_diff)
        score += dance_points
        reasons.append(f"Danceability proximity (+{dance_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    
    # The Loop: Judge every individual song
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        # Join the list of reasons into a single readable string
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
        
    # The Ranking: Sort the list of tuples by the score (which is at index 1) in descending order
    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    
    # Return the Top K Results
    return ranked_songs[:k]
