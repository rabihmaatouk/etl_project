# ETL Project

## Overview
This project is an ETL (Extract, Transform, Load) solution built using Python/Django. It processes client and transaction data from CSV and Excel files, stores it in a PostgreSQL database, and exposes a secure API for retrieving transaction details.

## Features
1. **Data Extraction**: 
   - Extracts client data from `clients.csv`.
   - Extracts transaction data from `transactions.xlsx`.

2. **Data Transformation**:
   - Cleans and validates the extracted data.
   - Transforms the data into a format suitable for PostgreSQL.

3. **Data Loading**:
   - Loads the transformed data into PostgreSQL tables.

4. **Secure API**:
   - Provides a secure API endpoint to retrieve transactions by client ID and date.

5. **Dockerization**:
   - The project is containerized using Docker for easier deployment and environment consistency.

## Project Structure
- `etl_project/`: Main Django project folder.
- `transactions/`: Contains Django app and ETL logic.
  - `management/commands/run_etl.py`: Script to run the ETL process.
- `clients.csv`: Sample client data file.
- `transactions.xlsx`: Sample transaction data file.

## Requirements
- Python 3.12
- Django
- PostgreSQL
- Docker

## Setup and Usage

1. **Clone the repository**:

