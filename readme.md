# Django Sales Application

This Django project enables users to upload product-related files, process the data to calculate total costs, and display detailed sales data. It includes file upload forms, Excel file processing, and user-specific data visualization.

Technologies Used
Backend: Django (Python Web Framework)
Excel File Handling: Pandas, Openpyxl
Frontend: HTML, CSS, JavaScript (with optional graphing library such as Chart.js)
Database: SQLite (for development)
Form Handling: Django forms for file uploads


## Requirements

- Python 3.8+
- Django 3.x+
- pandas
- openpyxl

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/8851962638/sales.git
    cd sales-project
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

    Your application will be available at `http://127.0.0.1:8000/`.

---

## Codebase Overview

### `sales/views.py`

This file contains the views for uploading and processing the Excel files, displaying user data, and rendering templates.

#### 1. File Upload (Page 1) - Referral Fee Upload

- **View**: `upload_referral_fee`
- **Description**: Handles the upload of an Excel file containing product names and their corresponding referral fees.
- **File Format**: Excel with columns `Product Name` and `Referral Fee`.
- **Flow**:
  - The user uploads the file.
  - The backend reads the file, validates the format, and stores the data in the session for later use.
  - On success, the user is redirected to the next step (upload cost page).
  
```python

Project Structure:
sales-management-system/
│
├── sales/
│   ├── migrations/            # Django migrations
│   ├── static/                # Static files (CSS, JS, images)
│   ├── templates/             # HTML templates
│   │   ├── upload_referral_fee.html
│   │   ├── upload_cost.html
│   │   └── user_data.html
│   ├── __init__.py
│   ├── admin.py               # Admin panel configuration
│   ├── apps.py
│   ├── models.py              # Data models
│   ├── views.py               # Views handling user requests
│   ├── forms.py               # Forms for file uploads
│   ├── urls.py                # URL routing
│   └── tests.py               # Test cases for the app
│
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── db.sqlite3                 # Database file (SQLite for development)



---

Functionality Overview
File Upload (Page 1 - Referral Fee Upload)
File Upload: Users upload an Excel file containing Product Name and Referral Fee.
File Processing: The file is read using pandas, and the data is saved in the session for further processing.
Error Handling: The system checks if the uploaded file contains the required columns and provides feedback to the user if the file format is incorrect.

File Upload (Page 2 - Cost File Upload)
File Upload: Users upload an Excel file containing Product Name and Cost.
File Processing: The file is read using pandas, and data is merged with the referral fee data stored in the session.
Calculation: The total cost for each product is calculated using the formula Total Cost = Cost × Referral Fee.
Excel Generation: A new Excel file containing the original data with the added Total Cost column is generated for download.

User Data (Frontend Page)
Total Sales: Displays the sum of the Total Cost column for all products.
Product Sales: Displays the total sales for each product, and users can click on product buttons to view the individual total sales.
Graph: A graphical representation of total sales per product is displayed using a bar chart or pie chart.




### Key Sections in `README.md`:

1. **Project Overview**: A brief description of what the project does and its purpose.
2. **Project Structure**: A directory tree that shows the structure of your codebase.
3. **Setup Instructions**: A step-by-step guide for setting up the project, including creating a virtual environment, installing dependencies, running migrations, and starting the development server.
4. **File Upload Formats**: Instructions on how to structure the files for referral fees and costs.
5. **Testing**: Details on how to test the project and whether there are example files available for testing.
6. **License**: Information about the project’s licensing (if applicable).

---
