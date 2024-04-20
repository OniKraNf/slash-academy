# Slash Academy

Slash Academy is a web application built with Django that provides online courses on various topics.

## Features

- Browse and search for courses
- Add courses to cart and proceed to checkout
- User authentication and authorization
- Admin panel for managing courses and users
- Browse webinars
- 

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
