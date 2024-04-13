# Django-TestProject

1. Clone the repository: `git clone https://github.com/InsideRaptor/Django-TestProject.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the MySQL database:
   - Create a MySQL database.
   - Update the database settings in `settings.py` file with your MySQL database credentials.
4. Create superuser: `python manage.py createsuperuser`
5. Run database migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

## Usage

1. Access the application by visiting `http://localhost:8000` in your web browser.
2. Now in the page you can access the first tab, upload data, and see it on the screen.
3. Same steps apply to the other tabs.
