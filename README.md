

---

# 🛍️ Amazon Sentiment Analysis

A sentiment analysis web app that processes Amazon product reviews to determine whether they are **positive**, **negative**, or **neutral**. It supports CSV upload, multilingual input, and product ID-based review extraction.

## 🔍 Features

* 💬 Analyze single or multiple reviews
* 🌐 Translate reviews in any language before analysis
* 📦 Upload CSV files with bulk reviews
* 🔎 Extract and analyze reviews using Amazon Product ID
* ☁️ Generate keyword word clouds for insights

## 🗂️ File Structure

```
Amazon-Sentiment-analysis/
├── app.py
├── requirements.txt
├── templates/
│   ├── landing.html
│   ├── multiple_reviews.html
│   ├── review.html
│   └── review_productid.html
├── sample_reviews.csv
├── sample_reviews_final_1140.csv
├── final_reviews_2200_with_telugu.csv
├── no_reviews_found.html
├── debug_response.html
├── __pycache__/
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository:

```bash
git clone https://github.com/kruthikakkamgari/Amazon-Sentiment-analysis.git
cd Amazon-Sentiment-analysis
```

### 2. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the application:

```bash
python app.py
```

### 4. Open your browser and go to:

```
http://localhost:5000
```

to start using the sentiment analysis tool.

## 🔧 Prerequisites

* Python 3.x
* pip (Python package manager)
* Required libraries (listed in `requirements.txt`)

## 📊 Sample Data

* `sample_reviews.csv` – Basic input data
* `multilingual_reviews_full_dataset.csv` – Reviews with multilingual content
* `sample_reviews_extended.csv` – Optimized dataset for testing

## 🤝 Contributing

Feel free to fork this repository and submit pull requests if you have suggestions for improvements or new features.
If you find any bugs, please open an issue in the [Issues section](https://github.com/kruthikakkamgari/Amazon-Sentiment-analysis/issues).

## 📄 License

© 2025 Kruthika Akkamgari. All rights reserved.
This project is not currently licensed for open-source use. Contact the author for permission to reuse or modify.

---
