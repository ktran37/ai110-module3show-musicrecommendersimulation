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

    # Diverse test profiles
    profiles = {
        "High-Energy Pop (The Gym Hero)": {
            "prefs": {
                "favorite_genre": "pop", 
                "favorite_mood": "intense", 
                "target_energy": 0.95,
                "target_danceability": 0.85,
                "target_popularity": 90,
                "preferred_decade": 2020
            },
            "mode": "energy_focused"
        },
        "Deep Intense Rock (The Headbanger)": {
            "prefs": {
                "favorite_genre": "rock", 
                "favorite_mood": "intense", 
                "target_energy": 0.90,
                "target_danceability": 0.40,
                "target_popularity": 60,
                "preferred_decade": 2010
            },
            "mode": "genre_first"
        },
        "Adversarial Edge Case (Hyper-Danceable Sad Classical)": {
            "prefs": {
                "favorite_genre": "classical", 
                "favorite_mood": "sad", 
                "target_energy": 0.95,        
                "target_danceability": 0.95,
                "target_popularity": 50,
                "preferred_decade": 1800
            },
            "mode": "default"
        }
    }

    # Format the output using ASCII table approach for better readability
    for profile_name, data in profiles.items():
        user_prefs = data["prefs"]
        mode = data["mode"]
        recommendations = recommend_songs(user_prefs, songs, k=5, mode=mode)

        print(f"\n🎧 Top Recommendations for the '{profile_name}' Profile (Mode: {mode}):")
        print("=" * 110)
        print(f"{'#':<3} | {'Title & Artist':<30} | {'Score':<6} | {'Reasons'}")
        print("-" * 110)
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            title_artist = f"{song['title']} by {song['artist']}"
            # Truncate explanation if too long, or let it wrap (assume wide terminal)
            print(f"{index:<3} | {title_artist:<30} | {score:<6.2f} | {explanation}")
        print("=" * 110)


if __name__ == "__main__":
    main()
