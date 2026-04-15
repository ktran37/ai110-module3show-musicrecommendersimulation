# 🎵 Music Recommender Simulation

## Project Summary

In this project, I built a highly modular, content-based music recommender simulator using Python. It successfully transforms complex song data (like tempo, acousticness, and popularity metrics) and a user's defined "taste profile" into a perfectly ranked and mathematically explained list of top tracks. 

It surpasses the core requirements by supporting sophisticated real-world recommendation concepts like dynamic Scoring Modes (The Strategy Pattern), Live Diversity Penalities (to prevent artists from flooding a user's feed), and adversarial edge-case bias testing.

---

## How The System Works

In the real world, music recommendation systems (like Spotify or Apple Music) use complex machine learning models, collaborative filtering (looking at what similar users listen to), and enormous datasets to predict what you want to hear next. They prioritize maximizing user engagement and listening time. **Our simulated version** uses a streamlined, content-based approach. It focuses on the intrinsic characteristics of the songs (like energy, genre, and mood) and matches them directly against a user's stated taste profile using a weighted scoring algorithm to recommend the closest matches.

### Features Used

**Song objects** utilize basic metadata and advanced numerical traits perfectly mapping to Spotify API aesthetics:
- `genre` and `mood` (categorical strings)
- `energy` and `danceability` (numerical, 0.0 - 1.0)
- `popularity` (numerical index out of 100)
- `release_year` (simulating release eras / decades)

**UserProfile Objects** store matching preference targets:
- `preferred_genre` & `preferred_mood`
- `target_energy` & `target_danceability`
- `target_popularity` (mainstream vs indie taste)
- `preferred_decade` (e.g. 2010s vs 1980s)

### The Recommendation Data Flow

1. **Scoring Rule (+ Strategy Pattern):** For every song, the system calculates a match score. Depending on the `mode` configured (`default`, `genre_first`, or `energy_focused`), weights shift dynamically. Categorical matches grant flat points, while numerical matches grant proximity points—the closer the song's value is to the user's preferred value, the higher the mathematical yield.
2. **Ranking Rule:** After scoring every song, the recommender sorts them from highest score to lowest.
3. **Diversity Penalty Logic:** As it parses the top recommendations, if the system detects an artist has already placed a track securely in a user's top pool, any subsequent tracks by that identical artist take an immediate `x0.5` score penalty! 
4. **Output formatting:** The sorted lists are converted into a crisp ASCII Terminal table explaining exactly *why* points were awarded.

### Potential Biases & Limitations
Because algorithms rely purely on predetermined weights, heavily weighting string matches can cause massive "filter bubbles" or "categorical exclusion". The system could completely ignore great songs that perfectly match the user's desired mood and energy simply because they fall under an adjacent, non-matching genre label (e.g. "Soul" vs "R&B"). We proved this numerically during edge-case testing, leading to the creation of the dynamic Strategy Modes to allow users to force the math to respect their true numbers over arbitrary genre tags.

---

## CLI Verification & Challenge Results

Running `python3 src/main.py` yields our neatly structured ASCII recommendation tables detailing exactly how the four advanced challenges were implemented!

```text
Loading songs from data/songs.csv...
Loaded songs: 17

🎧 Top Recommendations for the 'High-Energy Pop (The Gym Hero)' Profile (Mode: energy_focused):
==============================================================================================================
#   | Title & Artist                 | Score  | Reasons
--------------------------------------------------------------------------------------------------------------
1   | Gym Hero by Max Pulse          | 7.85   | Genre match (+1.0), Mood match (+0.5), Energy proximity (+2.94), Danceability proximity (+1.46), Popularity proximity (+0.95), Decade match (+1.0)
2   | Sunrise City by Neon Echo      | 6.97   | Genre match (+1.0), Energy proximity (+2.61), Danceability proximity (+1.41), Popularity proximity (+0.95), Decade match (+1.0)
3   | City Pulse by Metro Beats      | 5.71   | Energy proximity (+2.25), Danceability proximity (+1.46), Popularity proximity (+1.00), Decade match (+1.0)

🎧 Top Recommendations for the 'Deep Intense Rock (The Headbanger)' Profile (Mode: genre_first):
==============================================================================================================
#   | Title & Artist                 | Score  | Reasons
--------------------------------------------------------------------------------------------------------------
1   | Storm Runner by Voltline       | 7.23   | Genre match (+3.0), Mood match (+0.5), Energy proximity (+0.99), Danceability proximity (+0.74), Popularity proximity (+1.00), Decade match (+1.0)
2   | Neon Nights by DJ Spark        | 3.43   | Energy proximity (+0.98), Danceability proximity (+0.55), Popularity proximity (+0.90), Decade match (+1.0)

🎧 Top Recommendations for the 'Adversarial Edge Case (Hyper-Danceable Sad Classical)' Profile (Mode: default):
==============================================================================================================
#   | Title & Artist                 | Score  | Reasons
--------------------------------------------------------------------------------------------------------------
1   | Moonlit Sonata by Clara Bow    | 4.60   | Genre match (+1.0), Mood match (+1.0), Energy proximity (+0.40), Danceability proximity (+0.25), Popularity proximity (+0.95), Decade match (+1.0)
2   | Neon Nights by DJ Spark        | 3.56   | Energy proximity (+1.86), Danceability proximity (+0.90), Popularity proximity (+0.80)
3   | Storm Runner by Voltline       | 3.53   | Energy proximity (+1.92), Danceability proximity (+0.71), Popularity proximity (+0.90)
```

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app directly targeting the CLI file:

   ```bash
   python3 src/main.py
   ```

---

## Documentation & Reflection

Detailed evaluation documentation, dataset weaknesses, and reflections mapping this simulation to the behaviors of real-world recommendation ecosystems like Spotify can be found fully filled out here:
* [**Model Card**](model_card.md)
* [**Profile Evaluation & Reflection Comparisons**](reflection.md)

---
*Created as part of the AI-110 Music Recommender Simulation project.*

