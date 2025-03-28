from flask import Flask, request, jsonify
import mysql.connector
from sentiment_analysis import analyze_sentiment  # Import existing sentiment analysis function

# Initialize Flask app
app = Flask(__name__)

# MySQL Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ",  # Replace with your MySQL password
        database=" "
    )

@app.route('/analyze', methods=['POST'])
def analyze_review():
    try:
        # Parse the incoming JSON payload
        data = request.get_json()
        if not data or 'review' not in data:
            return jsonify({"error": "Invalid input, 'review' field is required"}), 400
        
        review_text = data['review']
        if not review_text.strip():
            return jsonify({"error": "Review text cannot be empty"}), 400

        # Analyze sentiment using the existing function
        sentiment, polarity = analyze_sentiment(review_text)
        
        # Log to the database (optional)
        db = get_db_connection()
        cursor = db.cursor()
        insert_query = """
            INSERT INTO sentiment_log (review_text, sentiment, polarity)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (review_text, sentiment, polarity))
        db.commit()
        cursor.close()
        db.close()

        # Return response
        return jsonify({
            "review": review_text,
            "sentiment": sentiment,
            "polarity": polarity
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
