# Django Portfolio Website

A free and open source Django-based portfolio website. Easily showcase your projects, skills, and contact info. All content is managed via the Django admin dashboard.

---

## Features

- Modern, responsive design with light and dark theme
- Manage all content (projects, skills, about, contact, etc.) from the admin dashboard
- SEO-friendly
- Media and static file support
- Easy free deployment to PythonAnywhere

---

## Requirements

- Python 3.10+
- Django 5.x
- PythonAnywhere account (for deployment)

---

## Local Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create and activate a virtual environment**

    - **Windows:**
      ```sh
      python -m venv venv
      venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
- (Recommended) Generate a Django `SECRET_KEY` and set it as an environment variable:

    1. **Generate a secret key**  
         Run this Python command in your terminal:
         ```sh
         python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
         ```
         Copy the generated key. (use `ctrl+shift+c` for copy and `ctrl+shift+v` to copy, pest if tradetional method doesn't work)

    2. **Set the `SECRET_KEY` environment variable:**

         - **Windows (Command Prompt):**
             ```sh
             set SECRET_KEY=your_generated_secret_key
             ```
         - **Windows (PowerShell):**
             ```sh
             $env:SECRET_KEY="your_generated_secret_key"
             ```
         - **macOS/Linux:**
             ```sh
             export SECRET_KEY=your_generated_secret_key
             ```

- (Optional) Create a `.env` file in your project root:
    ```
    SECRET_KEY=your_generated_secret_key
    ```

7. **Collect static files**
   ```sh
   python manage.py collectstatic
   ```

8. **Run the server**
   ```sh
   python manage.py runserver
   ```

---

## Deploying to PythonAnywhere

1. **Upload your project**  
   - Zip your project folder (excluding `venv` and unnecessary files) and upload it to your PythonAnywhere account, or use Git.

2. **Set up a virtual environment on PythonAnywhere**  
   - Go to the "Consoles" tab, start a Bash console, and run:
     ```sh
     mkvirtualenv portfolio-venv --python=python3.12
     pip install -r requirements.txt
     ```

3. **Configure your web app**  
   - Go to the "Web" tab and set:
     - **Source code**: Path to your project (where `manage.py` is located)
     - **Virtualenv**: Path to your virtualenv (e.g., `/home/yourusername/.virtualenvs/portfolio-venv`)
     - **WSGI configuration file**: Edit to point to your Django project’s WSGI application:
       ```python
       import sys
       path = '/home/yourusername/portfolio'
       if path not in sys.path:
           sys.path.append(path)
       from portfolio.wsgi import application
       ```

4. **Set environment variables**  
   - In the "Web" tab, add your `SECRET_KEY` as an environment variable.
   - Check Local Installation section to get a `SECRET_KEY`

5. **Set Django settings for production**  
   - In `portfolio/settings.py`:
     - Set `DEBUG = False`
     - Set `ALLOWED_HOSTS = ['your-username.pythonanywhere.com']`
     - Uncomment `STATIC_ROOT = BASE_DIR / 'static'` and comment `STATICFILES_DIRS = [ BASE_DIR / "static", ]`

6. **Collect static files**
   ```sh
   python manage.py collectstatic
   ```

9. **Reload your PythonAnywhere web app**  
   - Click "Reload" in the "Web" tab.

---

## Editing Your Portfolio

- Visit `/admin/` on your deployed site and log in with username: `admin`, password: `password`.
- Edit your profile, projects, skills, and contact info using the admin dashboard.
- Change admin password.
- Changes are reflected instantly on your site.

---

## Customization

- **Templates:** Edit HTML files in `templates/` for layout and content.
- **Static files:** CSS/JS/images in `static/`.
- **Models:** Add or modify models in `core/models.py`.

---

## License

MIT License

---

For issues or feature requests, open an issue on the [GitHub repository](https://github.com/ssshiponu/portfolio).

---

## Contribution

Contributions are welcome! If you have suggestions, bug reports, or want to add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your fork.
5. Open a pull request describing your changes.

Please ensure your code follows the existing style and includes relevant documentation or tests. For major changes, open an issue first to discuss your ideas.

Thank you for helping improve this project!

**Enjoy your new portfolio!**

