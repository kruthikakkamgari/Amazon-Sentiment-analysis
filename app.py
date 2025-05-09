from flask import Flask, render_template, request, jsonify
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot
import matplotlib.pyplot as plt
import io
import base64
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import threading

# Load environment variables
load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Add ZenRows API configuration
ZENROWS_API_KEY = os.getenv('ZENROWS_API_KEY')
ZENROWS_API_URL = 'https://ecommerce.api.zenrows.com/v1/targets/amazon/products'

# Create a lock for thread-safe operations
matplotlib_lock = threading.Lock()

def generate_wordcloud(text):
    # Use a lock to ensure thread safety when generating word clouds
    with matplotlib_lock:
        # Create and generate a word cloud image
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Convert the image to a base64 string for HTML display
        img = io.BytesIO()
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(img, format='png', bbox_inches='tight')
        plt.close()
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode()

def analyze_sentiment(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a sentiment analyzer. Analyze the following review and respond with only one word: POSITIVE, NEGATIVE, or NEUTRAL."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return str(e)


@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/single-review')
def single_review():
    return render_template('review.html')

@app.route('/product')
def product():
    return render_template('review_productid.html')

@app.route('/multiple-reviews')
def multiple_reviews():
    return render_template('multiple_reviews.html')

@app.route('/analyze_product', methods=['POST'])
def analyze_product():
    if request.method == 'POST':
        product_id = request.form['product_id']
        print(product_id , "product_id")
        # Call ZenRows API directly with product ID
        params = {
            'apikey': ZENROWS_API_KEY,
            'country': 'in',
            'tld': '.in'
        }
        
        try:
            response = requests.get(f'{ZENROWS_API_URL}/{product_id}', params=params)
            product_data = response.json()
            
            # Extract reviews from the response
            print("product_data",product_data)
            review = product_data['ai_generated_review_summary'] ;
            
            sentiment = analyze_sentiment(review)
            # Generate combined text for word cloud
            
            # Generate word cloud
            wordcloud_image = generate_wordcloud(review)
            
            print("review",review)
            
            return jsonify({
                'brand': product_data['brand'],
                'product_name': product_data['product_name'],
                'product_description': product_data['product_description'],
                'ai_generated_review_summary': product_data['ai_generated_review_summary'],
                'product_top_review': product_data['product_top_review'],
                'wordcloud': wordcloud_image,
                'overall_sentiment': sentiment,
                
            })
            
        except Exception as e:
            return jsonify({'error': f'Error analyzing product: {str(e)}'}), 500

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        review_text = request.form['review']
        
        # Generate word cloud
        wordcloud_image = generate_wordcloud(review_text)
        
        # Get sentiment
        sentiment = analyze_sentiment(review_text)
        
        return jsonify({
            'wordcloud': wordcloud_image,
            'sentiment': sentiment
        })

@app.route('/analyze_batch', methods=['POST'])
def analyze_batch():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File must be a CSV'}), 400
        
        try:
            # Read the CSV file
            df = pd.read_csv(file)
            
            # Check if the required column exists
            if 'review' not in df.columns and 'text' not in df.columns:
                return jsonify({'error': 'CSV must contain a column named "review" or "text"'}), 400
            
            # Get the review column
            review_col = 'review' if 'review' in df.columns else 'text'
            reviews = df[review_col].dropna().tolist()
            
            if not reviews:
                return jsonify({'error': 'No reviews found in the CSV file'}), 400
            
            # Process each review
            results = []
            for review in reviews:
                sentiment = analyze_sentiment(review)
                results.append({
                    'review': review,
                    'sentiment': sentiment
                })
            
            # Count sentiments
            positive_count = sum(1 for r in results if r['sentiment'] == 'POSITIVE')
            neutral_count = sum(1 for r in results if r['sentiment'] == 'NEUTRAL')
            negative_count = sum(1 for r in results if r['sentiment'] == 'NEGATIVE')
            
            return jsonify({
                'results': results,
                'stats': {
                    'total': len(results),
                    'positive': positive_count,
                    'neutral': neutral_count,
                    'negative': negative_count
                }
            })
            
        except Exception as e:
            return jsonify({'error': f'Error processing CSV: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True) 