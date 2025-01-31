# week-7
10 acadamy Kifiya AI mastery training program week 7 challenge

Building a Data Warehouse for Ethiopian Medical Businesses Project Overview This project is part of the 10 Academy AI Mastery Week 7 Challenge, aimed at building a robust data warehouse to store and analyze data scraped from Telegram channels focusing on Ethiopian medical businesses. The project involves:

Scraping data from public Telegram channels. Cleaning and transforming the scraped data. Preparing the data for object detection using YOLO (future tasks). Exposing the cleaned data via an API using FastAPI (future tasks). Repository Structure

├── data/ # Folder to store CSV files (raw, cleaned) │ ├── telegram_scrapped_data.csv # Raw data scraped from Telegram channels │ └── telegram_scrapped_data_cleaned.csv # Cleaned data ├── scr/ # Contains scraping scripts │ └── telegram_scraper.py # Script to scrape data using Telethon ├── notebooks/ # Jupyter notebooks for data processing │ └── task-2.ipynb # Data cleaning and transformation ├── models/ # DBT models for data transformations │ └── cleaned_data_transformed.sql # SQL model to aggregate and transform data ├── README.md # This README file └── requirements.txt # List of Python dependencies