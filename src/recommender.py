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
                "acousticness": float(row["acousticness"].strip()),
                "popularity": int(row["popularity"].strip()),
                "release_year": int(row["release_year"].strip())
            }
            loaded_songs.append(song)
            
    return loaded_songs

def score_song(user_prefs: Dict, song: Dict, mode: str = "default") -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences using different modes.
    Modes available: "default", "genre_first", "energy_focused"
    """
    score = 0.0
    reasons = []

    # Configure Strategy Weights
    if mode == "genre_first":
        genre_w = 3.0
        mood_w = 0.5
        energy_w = 1.0
        dance_w = 1.0
    elif mode == "energy_focused":
        genre_w = 1.0
        mood_w = 0.5
        energy_w = 3.0
        dance_w = 1.5
    else: # default
        genre_w = 1.0
        mood_w = 1.0
        energy_w = 2.0
        dance_w = 1.0

    # Genre Match
    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += genre_w
        reasons.append(f"Genre match (+{genre_w:.1f})")

    # Mood Match
    if song.get("mood") == user_prefs.get("favorite_mood"):
        score += mood_w
        reasons.append(f"Mood match (+{mood_w:.1f})")

    # Energy Proximity
    if "energy" in song and "target_energy" in user_prefs:
        energy_diff = abs(song["energy"] - user_prefs["target_energy"])
        energy_points = max(0.0, 1.0 - energy_diff) * energy_w
        score += energy_points
        reasons.append(f"Energy proximity (+{energy_points:.2f})")

    # Danceability Proximity
    if "danceability" in song and "target_danceability" in user_prefs:
        dance_diff = abs(song["danceability"] - user_prefs["target_danceability"])
        dance_points = max(0.0, 1.0 - dance_diff) * dance_w
        score += dance_points
        reasons.append(f"Danceability proximity (+{dance_points:.2f})")

    # Popularity Bonus
    if "target_popularity" in user_prefs and "popularity" in song:
        pop_diff = abs(song["popularity"] - user_prefs["target_popularity"]) / 100.0
        pop_points = max(0.0, 1.0 - pop_diff) * 1.0
        score += pop_points
        reasons.append(f"Popularity proximity (+{pop_points:.2f})")

    # Release Decade Bonus
    if "preferred_decade" in user_prefs and "release_year" in song:
        decade = (song["release_year"] // 10) * 10
        if decade == user_prefs["preferred_decade"]:
            score += 1.0
            reasons.append("Decade match (+1.0)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5, mode: str = "default") -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Applies a diversity penalty to ensure variety.
    """
    scored_songs = []
    
    for song in songs:
        score, reasons = score_song(user_prefs, song, mode=mode)
        scored_songs.append({"song": song, "score": score, "reasons": reasons})
        
    # Sort initially
    scored_songs.sort(key=lambda item: item["score"], reverse=True)
    
    final_recommendations = []
    seen_artists = set()
    
    for item in scored_songs:
        song = item["song"]
        score = item["score"]
        reasons = item["reasons"]
        
        # Diversity Penalty: Apply a harsh penalty if artist is already recommended
        if song["artist"] in seen_artists:
            score *= 0.5
            reasons.append("Diversity penalty applied (x0.5 score)")
        
        # After checking penalty, if we still want it (we shouldn't resort live for a simple list, 
        # but let's just accept the penalty and append. Wait, if we penalize we should ideally re-sort.
        # Alternatively, for simplicity, we just penalize and format)
        # Actually a true re-sort strategy is better, but maybe just appending with the reason is enough,
        # or we skip taking more than 2 from the same artist.
        # Let's say if it's already in seen_artists, we just don't add to final list if we want strict diversity,
        # but the prompt says: "penalize a song's score if its artist is already present".
        # Re-sorting approach:
        pass
        
    # A proper way to do diversity penalty on the fly:
    ranked_songs = []
    for _ in range(min(k, len(scored_songs))):
        if not scored_songs:
            break
        # Sort current pool to find the true max
        scored_songs.sort(key=lambda item: item["score"], reverse=True)
        best = scored_songs.pop(0)
        
        # Format the explanation
        explanation = ", ".join(best["reasons"])
        ranked_songs.append((best["song"], best["score"], explanation))
        
        # Apply penalty to remaining songs from the same artist
        artist = best["song"]["artist"]
        for other in scored_songs:
            if other["song"]["artist"] == artist and "Diversity penalty applied" not in other["reasons"]:
                other["score"] *= 0.5
                other["reasons"].append("Diversity penalty (x0.5)")
                
    return ranked_songs
