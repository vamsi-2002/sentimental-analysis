[Amazon_Review_Analysis_Documentation.pdf.pdf](https://github.com/user-attachments/files/19507342/Amazon_Review_Analysis_Documentation.pdf.pdf)

Project Documentation: Amazon Review Analysis System 
Main Objective:   This document outlines the step-by-step process for building a system that 
automates web scraping, stores data in a MySQL database, and performs keyword 
extraction and sentiment analysis on product reviews from Amazon. The system focuses on 
reviews for the iPhone 12 and leverages Python-based tools for automation and analysis. 
1. Technology Stack 
Python: Core programming language. 
Libraries and Tools: - Selenium: Automates browser interactions. - BeautifulSoup: Parses static HTML. - Pandas: Manages data processing. - MySQL: Stores structured data. - NLTK: Performs keyword extraction. - Transformers (Hugging Face): For sentiment analysis. 
2. Detailed Step-by-Step Procedure 
Step 1: Web Scraping with Selenium 
Objective: Extract iPhone 12 reviews from Amazon dynamically. 
1.1. Install Required Packages -Ensure the following libraries are installed: 
pip install selenium beautifulsoup4 pandas mysql-connector-python nltk transformers 
1.2. Set Up Selenium WebDriver - Download and install the appropriate WebDriver for your browser (e.g., ChromeDriver for 
Chrome). - Use the WebDriver to launch the browser and navigate to the Amazon product page. 
Step 2: Automating Login Process  
Objective: Access reviews behind a login wall. 
2.1. Navigate to Login Page -Identify and interact with the "Sign In" button using Selenium. 
2.2. Input Credentials and Submit -Enter login credentials and submit the form. 
Step 3: Product Review’s Data Acquisition  
Objective:   Scrape the data in the given format and store in Database 
3.1. Navigate to the product page  -Re-navigate to the product page after login.  
3.2. Automate Review Extraction - Identify the HTML structure of the reviews section. - Use Selenium’s `find_elements_by_*` methods to locate review titles, text, and other details. 
3.3 Automate to navigate to next page. - Automate the next page icon to fetch more reviews. 
Step 4: Saving Data to MySQL 
Objective: Store extracted reviews for analysis. 
4.1. Set Up MySQL Database and Table 
SQL Commands: 
CREATE DATABASE amazon_reviews; 
USE amazon_reviews; 
CREATE TABLE iphone12_reviews ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
review_title TEXT, 
review_text TEXT, 
style_name TEXT, 
colour VARCHAR(20), 
verified_purchase VARCHAR(15) 
); 
4.2. Insert Data into MySQL 
Use Python’s MySQL Connector to insert data row by row. 
Step 5: Keyword Extraction 
Objective: Extract frequent keywords from review texts. 
5.1. Preprocess Text Data - Convert reviews to lowercase. 
- Tokenize text into individual words. - Remove stopwords. 
Step 6: Sentiment Analysis 
Objective: Determine the sentiment of each review (positive, negative, or neutral). 
6.1. Use Pre-trained Sentiment Models 
Utilize sentiment-analysis from Textblob 
3. Challenges and Solutions 
1. Dynamic Web Content - Challenge: Reviews are loaded dynamically. - Solution: Use Selenium to simulate user interactions and capture dynamically loaded data. 
2. Pagination - Challenge: Reviews are spread across multiple pages. - Solution: Automate the "Next" button clicks until the last page. 
3. Data Quality - Challenge: Inconsistent or incomplete review data. - Solution: Implement data cleaning and validation processes before storage. 
4. Sentiment Accuracy - Challenge: Generic models may misclassify context-specific sentiments. - Solution: Use Textblob library for sentimental analysis. 
4. Testing and Validation 
Objective: Ensure system reliability and accuracy. 
Testing Steps: - Verify data extraction by manually checking sample scraped reviews. - Validate MySQL storage by querying data directly from the database. - Test sentiment predictions against known review sentiments
