import mysql.connector
import pandas as pd

# Database connection
db = mysql.connector.connect(
    host="localhost",           # Your MySQL server host (usually 'localhost')
    user="root",                # Your MySQL username
    password=" ",   # Your MySQL password
    database=" "   # The database you created
)

cursor = db.cursor()

# Read the CSV file
csv_file = 'iphone_reviews.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Loop through the DataFrame and insert data into the MySQL table
for index, row in df.iterrows():
    # Prepare the insert statement
    insert_query = """
        INSERT INTO iphone12_reviews (review_title, review_text, style_name, colour, verified_purchase)
        VALUES (%s, %s, %s, %s, %s)
    """
    
    # Collect data from each row
    data = (
        row['Review_Title'], 
        row['Review_Text'], 
        row['Style_Name'], 
        row['Colour'], 
        row['Verified_Purchase']
    )
    
    # Execute the insert statement
    cursor.execute(insert_query, data)

# Commit the transaction
db.commit()

# Close the connection
cursor.close()
db.close()

print("Data inserted successfully!")
