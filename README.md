# Portfolio Website

Welcome to my portfolio website! This project showcases my work and provides a way for visitors to get in touch. Below is a detailed overview of the features and functionality included in this project.

## Features

### 1. Template Inheritance

The website uses Django's template inheritance to maintain a consistent design across all pages. Common elements like headers, footers, and navigation bars are included in base templates and inherited by other pages.

### 2. Contact Page

The contact page allows visitors to send messages through the website. Required information includes:

- **Email**: The visitor's email address.
- **Full Name**: The visitor's full name.
- **Subject**: The subject of the message.
- **Message**: The content of the message.

### 3. Project Views

#### a. List View

The list view provides a summary of each project with the following details:

- **Image**: A representative image of the project.
- **Truncated Description**: A brief description of the project.
- **Date Posted**: The date when the project was posted.

#### b. Detail View

The detail view offers a comprehensive look at each project, including:

- **Carousel Images**: A carousel showcasing multiple images of the project.
- **Description**: A detailed description of the project.
- **Button Redirect**: A button linking to the project's website.

### 4. CRUD Functionality for Website Owner

The website owner has exclusive access to create, update, and delete projects. This functionality ensures that the project portfolio can be easily managed.

### 5. Inquiry Dashboard

A dashboard is provided for the website owner to view and manage inquiries submitted through the contact page. This dashboard displays all inquiries for efficient review and response.

### 6. Own Repository

The project is hosted in a dedicated repository with detailed documentation, including:

- **Installation Instructions**: Steps to set up the project.
- **Usage Guide**: How to use the website's features.
- **Contributing Guidelines**: Instructions for contributing to the project.
- **License Information**: Details about the project's license.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

   (INCOMPLETE AS PILLOW WONT INSTALL AT ALL)


  

