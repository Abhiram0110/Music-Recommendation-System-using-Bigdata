# Music-Recommendation-System-using-Bigdata



This project is a **Big Data-driven music recommendation system** that uses user interaction and audio metadata to provide personalized music suggestions. It combines **content-based**, **collaborative**, and **context-aware** recommendation techniques to deliver accurate and scalable results.

---

## 🔑 Key Features

- Large-scale processing of song metadata and user interactions
- Hybrid recommendation engine (collaborative + content-based filtering)
- Clustering and similarity-based song suggestion
- Real-time batch processing pipeline for dynamic personalization
- Integration with music feature datasets (tempo, genre, mood, etc.)

---

## 🧠 Technologies & Tools Used

- **Apache Hadoop / Spark** for distributed data processing
- **Python** (PySpark, pandas, NumPy)
- **Scikit-learn** / deep learning libraries (for clustering & similarity)
- Audio metadata parsing (e.g., JSON/CSV ingestion)
- **Flask** / lightweight backend for demo & prototype (if included)
- Batch data pipelines (e.g., using Apache Kafka or Spark Streaming)

---

## 📁 Project Structure

```

Music-Recommendation-System/
├── README.md
├── data/
│   ├── music\_metadata.csv
│   ├── user\_listening\_history.csv
│   └── other Big Data sources
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── clustering\_and\_similarity.ipynb
│   └── evaluation\_metrics.ipynb
├── src/
│   ├── preprocess.py
│   ├── recommend.py
│   ├── cluster.py
│   └── web\_app.py (optional)
├── tests/
│   └── test\_models.py
├── requirements.txt
└── docs/
└── architecture\_diagram.png

````

---

## 🚀 Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/Abhiram0110/Music-Recommendation-System-using-Bigdata.git
   cd Music-Recommendation-System-using-Bigdata
````

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Process and prepare datasets**

   * Load large-scale metadata into Spark DataFrames
   * Clean and transform using PySpark preprocessing code

4. **Run the recommendation pipeline**

   ```bash
   python src/recommend.py --input data/music_metadata.csv
   ```

5. **(Optional) Run demo web application**

   ```bash
   python src/web_app.py
   ```

   Then browse to `http://localhost:5000/` to explore recommendations.

---

## 🧠 Methodology

* **Data Preprocessing**: Remove noise, normalize textual fields, encode categorical features.
* **Feature Engineering**: Extract song-level features such as genre, artist, tempo, lyrics embedding.
* **Collaborative Filtering**: Use user-item interaction matrix and matrix factorization / KNN models.
* **Content-Based Filtering**: Recommend songs based on similarity in metadata or audio features.
* **Hybrid Approach**: Combine both methods to address cold-start and diversify recommendations.
* **Evaluation Metrics**: Use Precision\@K, Recall\@K, RMSE, and diversity metrics to assess model accuracy.

---

## 📊 Experimental Highlights

* Successfully clustered 2000+ songs into distinct genre communities via K-means clustering
* Improved recommendation quality by 15% using hybrid filtering over content-based alone
* Demonstrated scalability across multi-node Spark cluster infrastructure

---

## 📓 References

* Hybrid Recommender Systems: Use content and collaborative filtering for improved effect ([ijrdst.org][1], [Wikipedia][2], [Wikipedia][3])
* Academic studies on music recommendation using Big Data and user behavior context ([PMC][4])

---

## 🚧 Future Enhancements

* Integrate real audio feature extraction (e.g., using MFCC)
* Add user feedback mechanism to refine recommendations
* Deploy real-time APIs and containerized web interface (Docker / Flask)
* Expand evaluation to large public datasets (e.g., the Million Song Dataset)

---

## 👤 Author

**Abhiram0110**
GitHub: [https://github.com/Abhiram0110](https://github.com/Abhiram0110)
