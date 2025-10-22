# Mini Content-Based Food Recommendation System – Python + Visualization

## Project Overview
This is a **content-based food recommendation system** built from scratch using Python.  
It suggests **top 5 dishes** based on user preferences for **Spice Level** and **Popularity Score**.  
All recommendations are calculated using **Euclidean distance**, and results are visualized using **Matplotlib scatter plots**.

---

## Features
- Accepts **user preferences** for Spice Level and Popularity Score.
- Calculates similarity between user input and all dishes using **Euclidean distance**.
- Returns **top 5 recommended dishes** based on closest distance.
- **Visualizes** dishes and user input on a 2D plot.
- Fully built **from scratch without using ML libraries**.

---

## Dataset
A small sample dataset is included in the code:

| Dish                  | Spice_Level | Popularity_Score |
|-----------------------|------------|----------------|
| Chicken Chettinad      | 9          | 85             |
| Hyderabadi Biryani     | 8          | 95             |
| Andhra Chilli Chicken  | 10         | 80             |
| Kerala Chicken Roast   | 7          | 75             |
| Paneer Dosa            | 6          | 91             |
| ...                   | ...        | ...            |

You can **add more dishes** by updating the `data` dictionary in the code.

---

## How It Works
1. Represent each dish as a **vector** `[Spice_Level, Popularity_Score]`.
2. Take **user input** as a vector `[user_spice_level, user_popularity_score]`.
3. Calculate **Euclidean distance** between user vector and all dish vectors.
4. Sort distances and select **top 5 closest dishes**.
5. Optionally, **plot all dishes** and user point for visualization.

---

## Usage
1. Clone the repository or download the code.
2. Run the Python script:

```bash
python recommend_food.py
