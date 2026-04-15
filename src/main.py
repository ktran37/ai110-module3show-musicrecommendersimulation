"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop", 
        "favorite_mood": "happy", 
        "target_energy": 0.80,
        "target_danceability": 0.80
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n🎧 Top Recommendations for the 'Pop/Happy' Profile:\n" + "="*50)
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"#{index} | 🎵 {song['title']} by {song['artist']}")
        print(f"    📈 Score: {score:.2f} / 5.00")
        print(f"    💡 Why? {explanation}")
        print("-" * 50)


if __name__ == "__main__":
    main()
