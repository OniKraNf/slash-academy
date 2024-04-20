# Slash Academy

Slash Academy is a web application built with Django that provides online courses on various topics.

## Features

- Browse and search for courses on various topics
- Access course materials, including videos and text content
- Take quizzes to test your knowledge and track your progress
- Add courses to your cart and proceed to checkout for enrollment

### Course Content

- **Videos**: Access high-quality video content covering course topics.
- **Text Content**: Read detailed text materials providing additional context and information.
- **Quizzes**: Take quizzes to assess your understanding of course material and track your progress.

### User Management

- **User Authentication**: Sign up for an account or log in to access course content and track progress.
- **User Profiles**: View and manage your profile information, including course enrollment and progress tracking.

### Admin Panel

- **Course Management**: Add, edit, or delete courses from the admin panel.
- **User Management**: View and manage user accounts, including enrollment and progress tracking.

## Screenshots

### Main Page
![Main Page](/for_readme/main_page.png)

### Search
![Search Courses](/for_readme/search_courses.png)

### Cart
![Cart](/for_readme/cart.png)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/slash-academy.git
   
2. Navigate to the project directory:

   ```bash
   cd slash-academy

3. Run Docker Compose to build and start the containers:

   ```bash
   docker-compose up --build
   
4. Apply migrations to create the database schema:

   ```bash
   docker-compose exec web python manage.py migrate
