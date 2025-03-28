from textblob import TextBlob
import mysql.connector
import pandas as pd
import pandas as pd
import numpy as np

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vamsi@2002",
    database="amazon_reviews"
)

cursor = db.cursor()

# Retrieve reviews from the database
cursor.execute("SELECT review_text FROM iphone12_reviews")
reviews = cursor.fetchall()

# Perform sentiment analysis
sentiments = []

for review in reviews:
    text = review[0]
    if text:  # Ensure review text is not None
        analysis = TextBlob(text)
        sentiment_score = analysis.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)
        sentiments.append((text, sentiment_score))

# Convert to DataFrame for analysis
df = pd.DataFrame(sentiments, columns=['Review Text', 'Sentiment Score'])

# Classify sentiment as Positive, Negative, or Neutral
df['Sentiment'] = df['Sentiment Score'].apply(
    lambda score: 'Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral'
)

# Display results
print(df.head())

# Save the results to a new CSV file
df.to_csv('sentiment_analysis_results.csv', index=False)
print('CSV file created')
# Close the database connection
cursor.close()
db.close()
