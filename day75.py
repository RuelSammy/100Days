#Build a recommendation system.
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# 1. Load Sample Data
# We'll create a simple movie rating dataset with users and movie ratings
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4],
    'movie': ['Inception', 'Titanic', 'Avengers', 'Titanic', 'Avengers',
              'Inception', 'Avengers', 'Inception', 'Titanic'],
    'rating': [5, 4, 5, 5, 3, 4, 4, 2, 5]
}

df = pd.DataFrame(data)

# 2. Create a user-item matrix
# This matrix shows how each user rated each movie
user_movie_matrix = df.pivot_table(index='user_id', columns='movie', values='rating').fillna(0)

# 3. Compute cosine similarity between movies (items)
# Transpose the matrix so each row represents a movie and columns represent users
movie_similarity = cosine_similarity(user_movie_matrix.T)

# Turn the similarity matrix into a DataFrame for easier handling
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# 4. Build a recommendation function
def recommend_similar_movies(movie_name, similarity_matrix, n=2):
    """
    Recommend top `n` movies similar to the given `movie_name`.
    """
    if movie_name not in similarity_matrix.columns:
        return f"Movie '{movie_name}' not found in dataset."
    
    # Sort the similar movies by similarity score, ignore the movie itself
    similar_scores = similarity_matrix[movie_name].sort_values(ascending=False)
    recommended = similar_scores[1:n+1]  # skip the first one (it's the same movie)
    return recommended

# 5. Test the recommender
print("Movies similar to 'Titanic':\n")
print(recommend_similar_movies('Titanic', movie_similarity_df))
