import mysql.connector
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK data
nltk.download('punkt')
nltk.download('punkt-tab')
nltk.download('stopwords')

# Database connection
db = mysql.connector.connect(
    host="localhost",           # Your MySQL server host (usually 'localhost')
    user="root",                # Your MySQL username
    password="vamsi@2002",   # Your MySQL password
    database="amazon_reviews"   # Your database name
)

cursor = db.cursor()

# Retrieve reviews from the database
cursor.execute("SELECT review_text FROM iphone12_reviews")
reviews = cursor.fetchall()

# Initialize a list to store all words from the reviews
all_words = []

# Define stopwords
stop_words = set(stopwords.words('english'))

# Process each review text
for review in reviews:
    text = review[0]  # Review text from database
    
    if text:  # Check if the review text is not None or empty
        text = text.lower()  # Convert to lowercase to ensure case-insensitivity
        tokens = word_tokenize(text)  # Tokenize the review text
        filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]  # Remove stopwords and non-alphabetical words
        all_words.extend(filtered_tokens)
    else:
        # If the review is None or empty, you can handle it here (skip or log it)
        continue

# Count the frequency of each word
word_counts = Counter(all_words)

# Get the most common (best) and least common (worst) words
best_keywords = word_counts.most_common(10)  # Top 10 most frequent keywords
worst_keywords = word_counts.most_common()[-10:]  # Bottom 10 least frequent keywords

# Print the results
print("Best Keywords (Most Frequent):")
for keyword, count in best_keywords:
    print(f"{keyword}: {count}")

print("\nWorst Keywords (Least Frequent):")
for keyword, count in worst_keywords:
    print(f"{keyword}: {count}")

# Close the connection
cursor.close()
db.close()
