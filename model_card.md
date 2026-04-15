# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender tries to suggest the best songs for a user based on their specific taste profile. It assumes the user knows exactly what genre, mood, energy level, and danceability they want. This tool is designed for classroom exploration and simulation purposes to understand how recommendation algorithms work. It should **not** be used for real-worid commercial music streaming, as it lacks user history, collaborative filtering, and a massive song database.

---

## 3. How the Model Works  

VibeFinder uses a content-based scoring rule. It looks at a song's genre and mood (words) and its energy and danceability levels (numbers). If the song's genre or mood matches the user's preference exactly, it gets bonus points. For the numbers (energy and danceability), the closer the song's score is to the user's preferred number, the more proximity points it earns. All these points are added up into a final score, and the songs with the highest scores are ranked at the top of the recommendation list.

---

## 4. Data  

The dataset contains a small catalog of 17 songs. Each song has features like title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. I added 7 new songs to the original 10 to include genres like EDM, classical, country, R&B, metal, soul, and hip hop. However, the catalog is still very small and missing millions of songs and sub-genres that exist in the real world.

---

## 5. Strengths  

The system works very well for users who want standard, popular genres that are well-represented in the dataset, like "Pop" or "Lofi". It successfully captures the core vibe of a request, reliably giving fast, upbeat songs to users who ask for high energy, and slow, calm songs to users who ask for low energy. The recommendations make intuitive sense for straightforward profiles.

---

## 6. Limitations and Bias 

One significant limitation discovered during the experiments is that the system strictly requires exact string matching for categorical features like genre or mood. If a user likes "R&B", but a song is labeled "soul", they receive zero categorical points despite the genres being musically adjacent. Furthermore, because our catalogue is incredibly small (17 songs) and slightly skewed towards Pop and Lofi, users who prefer niche genres (like classical or metal) have very limited options. Additionally, the algorithm calculates absolute differences for numerical features like Energy; this penalizes a song equally for being "too high" or "too low" in energy, which might not align with real human psychology (a user might tolerate *more* energy than their target, but strongly dislike *less*). Finally, by aggressively rewarding numerical proximity, the system can create a "filter bubble" where a user asking for 0.95 energy simply loops through the exact same 3 upbeat tracks, completely blocking out slower songs they might actually enjoy for variety.

---

## 7. Evaluation  

To ensure the model behaved properly, I tested four distinct user profiles: "High-Energy Pop," "Chill Lofi," "Deep Intense Rock," and an "Adversarial Edge Case" (asking for sad classical music but with extreme energy and danceability). I looked to see if the top recommended songs correctly aligned with the requested genres and numerical targets. The most surprising result happened with the adversarial profile: initially, a slow, low-energy classical piano song took the #1 spot simply because its genre and mood tags matched the text the user entered, completely overriding the user's mathematical desire for a danceable beat! To test this further, I ran a strict "weight shift" experiment where I doubled the value of the energy score and halved the value of a genre match. Instantly, the rankings fixed themselves, pushing an upbeat pop song to the top of the classical profile because the numerical math finally outweighed the text tags.

---

## 8. Future Work  

If I kept developing this, I would add sub-genre matching to give partial points (e.g., matching "pop" with "indie pop"). I would also include a diversity rule that prevents the system from recommending 5 songs from the exact same artist or identical genre, ensuring a better mix for discovery. Lastly, expanding the dataset from a CSV to an API with thousands of real songs would make testing far more accurate.

---

## 9. Personal Reflection  

My biggest learning moment during this project was realizing that recommendation systems are not magic, but rather simple math formulas relying on weighted scores. I was genuinely surprised by how quickly a basic algorithm—just adding points for matched strings and calculating numerical distance—can "feel" like a highly personalized, intelligent recommendation. 

Using AI tools like Copilot was incredibly helpful for quickly generating boilerplate code, expanding the CSV dataset with plausible mock data, and brainstorming algorithm weight strategies. However, I constantly had to double-check the AI's logic when dealing with edge cases—like ensuring the scoring math actually aligned with human intuition (like the sad classical vs. gym pop test) rather than just blindly trusting the code. 

If I were to extend this project further, I would want to integrate a real-world dataset via an API (like Spotify's) and add a collaborative filtering layer to see how community data changes the results compared to this purely content-based approach.  
