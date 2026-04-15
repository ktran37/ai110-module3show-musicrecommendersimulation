# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

In the real world, music recommendation systems (like Spotify or Apple Music) use complex machine learning models, collaborative filtering (looking at what similar users listen to), and enormous datasets to predict what you want to hear next. They prioritize maximizing user engagement and listening time. **Our simulated version** uses a streamlined, content-based approach. It focuses on the intrinsic characteristics of the songs (like energy, genre, and mood) and matches them directly against a user's stated taste profile using a weighted scoring algorithm to recommend the closest matches.

### Features Used

**Song Objects** will use these specific features:
- `genre` (categorical)
- `mood` (categorical)
- `energy` (numerical, 0.0 - 1.0)
- `danceability` (numerical, 0.0 - 1.0)

**UserProfile Objects** will store matching preference criteria:
- `preferred_genre`
- `preferred_mood`
- `preferred_energy`
- `preferred_danceability`

### Scoring and Ranking

- **Scoring Rule:** For a given song, the system calculates a match score. Categorical matches (genre, mood) grant flat points if they match exactly. Numerical matches (energy, danceability) grant points based on proximity—the closer the song's value is to the user's preferred value, the higher the points.
- **Weights:** Attributes are weighted differently (e.g., Genre might be worth more than Mood) to reflect that some preferences are stronger dealbreakers than others.
- **Ranking Rule:** After scoring every song in the database, the recommender sorts them from highest score to lowest, returning the top results to the user.

### Algorithm Recipe

The finalized scoring logic assigns points to each song based on the following rules (Maximum score: 5.0):
1. **Genre Match:** `+2.0` points if `song.genre` perfectly matches the user's `favorite_genre`.
2. **Mood Match:** `+1.0` point if `song.mood` perfectly matches the user's `favorite_mood`.
3. **Energy Proximity:** Up to `+1.0` point total, calculated as `1.0 - |song.energy - user.target_energy|`.
4. **Danceability Proximity:** Up to `+1.0` point total, calculated as `1.0 - |song.danceability - user.target_danceability|`.

### Potential Biases & Limitations
Because this algorithm recipe heavily weights the genre match (+2.0 points) compared to other features, it might over-prioritize genre. This means the system could completely ignore great songs that perfectly match the user's desired mood, energy, and danceability simply because they fall under a different, un-preferred genre. It is a strictly content-based filter, meaning it does not capture more complex, emergent preferences over time or utilize collaborative community data.

---

## CLI Verification (Terminal Screenshot Example)

Running `python3 src/main.py` yields our neatly formatted recommendations, testing the system with both traditional and adversarial profiles to evaluate how the algorithm handles extreme edge cases.

```text
Loading songs from data/songs.csv...
Loaded songs: 17

🎧 Top Recommendations for the 'High-Energy Pop (The Gym Hero)' Profile:
==================================================
#1 | 🎵 Gym Hero by Max Pulse
    📈 Score: 4.95 / 5.00
    💡 Why? Genre match (+2.0), Mood match (+1.0), Energy proximity (+0.98), Danceability proximity (+0.97)
--------------------------------------------------
#2 | 🎵 Sunrise City by Neon Echo
    📈 Score: 3.81 / 5.00
    💡 Why? Genre match (+2.0), Energy proximity (+0.87), Danceability proximity (+0.94)
--------------------------------------------------
#3 | 🎵 Storm Runner by Voltline
    📈 Score: 2.77 / 5.00
    💡 Why? Mood match (+1.0), Energy proximity (+0.96), Danceability proximity (+0.81)
--------------------------------------------------

🎧 Top Recommendations for the 'Chill Lofi (The Study Session)' Profile:
==================================================
#1 | 🎵 Library Rain by Paper Lanterns
    📈 Score: 4.97 / 5.00
    💡 Why? Genre match (+2.0), Mood match (+1.0), Energy proximity (+1.00), Danceability proximity (+0.97)
--------------------------------------------------
#2 | 🎵 Midnight Coding by LoRoom
    📈 Score: 4.86 / 5.00
    💡 Why? Genre match (+2.0), Mood match (+1.0), Energy proximity (+0.93), Danceability proximity (+0.93)
--------------------------------------------------
#3 | 🎵 Focus Flow by LoRoom
    📈 Score: 3.90 / 5.00
    💡 Why? Genre match (+2.0), Energy proximity (+0.95), Danceability proximity (+0.95)
--------------------------------------------------

🎧 Top Recommendations for the 'Deep Intense Rock (The Headbanger)' Profile:
==================================================
#1 | 🎵 Storm Runner by Voltline
    📈 Score: 4.73 / 5.00
    💡 Why? Genre match (+2.0), Mood match (+1.0), Energy proximity (+0.99), Danceability proximity (+0.74)
--------------------------------------------------
#2 | 🎵 Gym Hero by Max Pulse
    📈 Score: 2.49 / 5.00
    💡 Why? Mood match (+1.0), Energy proximity (+0.97), Danceability proximity (+0.52)
--------------------------------------------------

🎧 Top Recommendations for the 'Adversarial Edge Case (Hyper-Danceable Sad Classical)' Profile:
==================================================
#1 | 🎵 Moonlit Sonata by Clara Bow
    📈 Score: 3.45 / 5.00
    💡 Why? Genre match (+2.0), Mood match (+1.0), Energy proximity (+0.20), Danceability proximity (+0.25)
--------------------------------------------------
#2 | 🎵 Gym Hero by Max Pulse
    📈 Score: 1.91 / 5.00
    💡 Why? Energy proximity (+0.98), Danceability proximity (+0.93)
--------------------------------------------------
#3 | 🎵 Neon Nights by DJ Spark
    📈 Score: 1.83 / 5.00
    💡 Why? Energy proximity (+0.93), Danceability proximity (+0.90)
--------------------------------------------------
```

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

