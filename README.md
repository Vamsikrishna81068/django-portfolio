# Django Portfolio

## Features
- Responsive design
- User authentication
- Portfolio showcasing projects
- Admin panel management
- Easy to customize and extend

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Vamsikrishna81068/django-portfolio.git
   cd django-portfolio
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- To run the development server:
  ```bash
  python manage.py runserver
  ```
- Access the application at `http://127.0.0.1:8000/`

## Configuration
- Configure your database settings in `settings.py`.
- Set up environment variables for sensitive data (e.g., secret keys) using a `.env` file.

## Deployment
- To deploy to production, consider using platforms like Heroku, DigitalOcean, or AWS.
- Ensure you set `DEBUG = False` in `settings.py` for production.

## Customization
- Modify templates in the `templates` directory for UI changes.
- Add or remove apps as needed and adjust the `INSTALLED_APPS` list in `settings.py`.

## License
This project is licensed under the MIT License.