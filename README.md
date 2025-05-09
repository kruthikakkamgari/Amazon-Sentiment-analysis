Amazon Sentiment Analysis
This project analyzes Amazon product reviews using AI-driven sentiment classification. It leverages natural language processing to classify customer feedback effectively.

Features
Sentiment Classification: Classifies customer reviews into positive, negative, or neutral sentiment.

Multi-language Support: Translates reviews into English and analyzes sentiment for reviews in any language.

CSV File Integration: Upload and analyze reviews from CSV files or Amazon product IDs.

Word Cloud Generation: Visual representation of frequently mentioned words in the reviews.

Data Files Included: Sample CSV files with customer reviews for testing.

Files in the Repository
app.py: The main application file that runs the sentiment analysis service.

requirements.txt: Lists the dependencies required to run the project.

sample_reviews.csv: Sample CSV file with product reviews to test the functionality.

final_reviews_2200_with_telugu.csv: A larger dataset of Amazon reviews, including Telugu reviews.

templates/debug_response.html: HTML template for displaying debug information.

templates/no_reviews_found.html: HTML template for displaying a message when no reviews are found.

How to Run
Clone the repository:
git clone https://github.com/kruthikakkamgari/Amazon-Sentiment-analysis.git
cd Amazon-Sentiment-analysis

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open your browser and navigate to:
http://localhost:5000 to access the sentiment analysis tool.

Prerequisites
Python 3.x

pip (for managing Python dependencies)

Required libraries listed in requirements.txt

Contributing
Feel free to fork this repository and submit pull requests if you have suggestions for improvements or new features. If you find any bugs, please open an issue in the "Issues" section.

License
This project is open-source and available under the MIT License.

