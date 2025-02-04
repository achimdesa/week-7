# week-7
10 acadamy Kifiya AI mastery training program week 7 challenge

Building a Data Warehouse for Ethiopian Medical Businesses Project Overview This project is part of the 10 Academy AI Mastery Week 7 Challenge, aimed at building a robust data warehouse to store and analyze data scraped from Telegram channels focusing on Ethiopian medical businesses. The project involves:

Scraping data from public Telegram channels. Cleaning and transforming the scraped data. Preparing the data for object detection using YOLO (future tasks). Exposing the cleaned data via an API using FastAPI (future tasks). Repository Structure

├── data/ # Folder to store CSV files (raw, cleaned) │ ├── telegram_scrapped_data.csv # Raw data scraped from Telegram channels │ └── telegram_scrapped_data_cleaned.csv # Cleaned data ├── scr/ # Contains scraping scripts │ └── telegram_scraper.py # Script to scrape data using Telethon ├── notebooks/ # Jupyter notebooks for data processing │ └── task-2.ipynb # Data cleaning and transformation ├── models/ # DBT models for data transformations │ └── cleaned_data_transformed.sql # SQL model to aggregate and transform data ├── README.md # This README file └── requirements.txt # List of Python dependencies

Steps to Run the Project

Environment Setup 1.1. Install Dependencies To run the scraping and data cleaning tasks, you need to install the required Python libraries. Use the following command to install them:
pip install -r requirements.txt

Scraping Data from Telegram Channels The first step is to scrape data from the specified Telegram channels. The scraping process uses the Telethon library to extract messages and metadata. The scraped data is stored in a CSV file for further processing.
Script: telegram_scraper.py Output: data/telegram_scrapped_data.csv Ensure you have valid Telegram API credentials before running the scraper. You can place your credentials in a .env file as follows:

python scr/telegram_scraper.py

This will scrape the data and save it to data/telegram_scrapped_data.csv.

Data Cleaning and Transformation 3.1. Task 2: Data Cleaning and Transformation (task-2.ipynb) Once the data is scraped, the next step is to clean and transform the data. The notebook task-2.ipynb handles this task, including:
Removing duplicates. Handling missing values. Standardizing text and date formats. Storing cleaned data into a PostgreSQL database. To run the notebook, open it in Jupyter:

jupyter notebook notebooks/task-2.ipynb 3.2. Configuring PostgreSQL Make sure you have PostgreSQL installed and running. You can configure the connection to PostgreSQL in the notebook using the following format:

engine = create_engine('postgresql://myuser:mypassword@localhost:5432/telegram_data') The cleaned data will be saved in the cleaned_data table of your PostgreSQL database.

DBT for Data Transformation DBT (Data Build Tool) is used to apply further transformations to the cleaned data.
Install DBT:

pip install dbt Initialize a DBT project:

dbt init my_project Create and run DBT models:

Model location: models/cleaned_data_transformed.sql Run the transformations:

dbt run The DBT model aggregates the data by day and channel, counting the number of messages and media shared.


---

### **YOLO Object Detection**

### 4. YOLO Object Detection

#### 4.1. Task 3: Object Detection Using YOLO (`task-3.ipynb`)

In Task 3, we apply object detection using the YOLOv5 model. Run the `task-3.ipynb` notebook to perform object detection on the images scraped from Telegram.

- **Input**: Images from `photos/`
- **Output**: Detected images and CSV results in `detection_results/`

You can execute the notebook as follows:

jupyter notebook notebooks/task-3.ipynb



---

### **Exposing Data via FastAPI and Additional Information**

### 5. Exposing Data via FastAPI

#### 5.1. Task 4: FastAPI for Exposing Data (`main.py`)

The cleaned data and detection results are exposed through an API using **FastAPI**.

- **/messages/**: Fetches cleaned message data.
- **/detections/{image_name}**: Fetches object detection results for a specified image.

Run FastAPI using the following command:

uvicorn main:app --reload



Check FastAPI for Exposing Data in /src/main.py and for object detection in notebooks/task-3.ipynb

