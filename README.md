# Hugging Face Model Crawler
This is a Django-based web application that fetches and manages the top 100 models from Hugging Face using the official API and the uv package manager.

## Overview
The project consists of a crawler script that retrieves model metadata and a Django administrative interface to view and edit the stored data. It is built with a focus on modern Python tooling using uv for dependency management.

## Tech Stack
- Framework: Django
- Package Manager: uv
- Data Source: Hugging Face API
- Database: SQLite

## Installation

1. Install uv if you have not already:
   curl -sSf https://astral.sh/uv/install.sh | sh
2. Clone the repository:
   git clone <your-repository-url>
   cd <your-repository-name>
3. Sync dependencies:
   uv sync

## Database Configuration
1. Apply migrations to set up the database schema:
   uv run python manage.py migrate
2. Create an admin account to access the dashboard:
   uv run python manage.py createsuperuser

## Usage
1. Run the crawler script to fetch the top 100 models:
   uv run python crawl_data.py
2. Start the development server:
   uv run python manage.py runserver
3. Access the data management interface:
   Open your browser and navigate to http://127.0.0.1:8000/admin/
   Log in with the superuser credentials created during setup.
