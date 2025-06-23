# Django Portfolio Website

A free and open-source Django-based portfolio website that allows you to easily showcase your projects, skills, and contact information. All content is managed through an intuitive admin dashboard.

## 🚀 Live Demo

Click [here](https://mohinuddinshipon.pythonanywhere.com) to see a demo.

## ✨ Features

- **Modern Design**: Responsive layout with light and dark theme support
- **Easy Content Management**: Manage projects, skills, about section, and contact info from the admin dashboard
- **SEO Optimized**: Built-in SEO features including `robots.txt` and `sitemap.xml`
- **Free Deployment**: Easy deployment to PythonAnywhere
- **Customizable**: Flexible templates and static files for easy customization

## 📋 Requirements

- **Python**: 3.10+ (recommended: 3.12+)
- **Django**: 5.x (recommended: 5.2.x)
- **PythonAnywhere Account**: For free deployment

## 🚀 Quick Start

Choose your preferred installation method:

### Option 1: Direct Deployment
Perfect if you only want to customize content through the admin panel.

### Option 2: Local Installation
Recommended if you want to customize design, models, or backend logic.

---

## 💻 Local Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

### Step 2: Set Up Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

#### Generate Django Secret Key
Run this command to generate a secure secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

> **💡 Tip**: Use `Ctrl+Shift+C` to copy and `Ctrl+Shift+V` to paste if traditional methods don't work.

#### Set Environment Variables

**Windows (Command Prompt):**
```bash
set SECRET_KEY=your_generated_secret_key
```

**Windows (PowerShell):**
```bash
$env:SECRET_KEY="your_generated_secret_key"
```

**macOS/Linux:**
```bash
export SECRET_KEY=your_generated_secret_key
```

#### Alternative: Create .env File
Create a `.env` file in your project root:
```
SECRET_KEY=your_generated_secret_key
DEBUG=True
```

> **⚠️ Important**: Set `DEBUG=False` in production environments.

### Step 5: Set Up Static Files
```bash
python manage.py collectstatic
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

> **📝 Note**: No database migration is needed as a SQLite database with initial data is included.

---

## 🌐 PythonAnywhere Deployment


### Step 1: Upload Your Project
- **Local Installation**: Zip your project folder (exclude `venv` and unnecessary files) and upload
- **Direct Deployment**: Skip to Step 2

### Step 2: Set Up Virtual Environment and Codebase

1. Create a free account at [pythonanywhere.com](https://pythonanywhere.com).

2. Navigate to the **Web** tab and create a new **Web app**. Select `Django`, `python3.12` and name it `portfolio`.

3. Navigate to the **Files** tab and remode the `portfolio/` folder.

4. Now navigate to the **Consoles** tab and start a **Bash console**

5. copy, pest this script and hit enter
   ```bash
    rm -rf portfolio/
    git clone https://github.com/ssshiponu/portfolio
    cd portfolio
   ```
   ```bash
   ./setup.sh
   ```
### Step 7: Deploy
Click **Reload** in the Web tab to deploy your application.

---

## ⚙️ Managing Your Portfolio

### Admin Access
1. Visit `your-username.pythonanywhere.com/admin`
2. **Default credentials**:
   - Username: `admin`
   - Password: `password`

> **🔒 Security**: Change the admin password immediately after first login.

### Content Management
Use the admin dashboard to manage:
- Personal profile and metadata information
- Project portfolio
- Skills and expertise
- Developement process information
- Contact information

Changes are reflected instantly on your live site.

---

## 🎨 Customization

### Templates
- **Location**: `templates/` directory
- **Purpose**: Modify HTML structure and layout

### Static Files
- **Location**: `static/` directory
- **Contents**: CSS styles, JavaScript, and images

### Data Models
- **Location**: `core/models.py`
- **Purpose**: Add or modify database models

### Views and URLs
- **Location**: `core/views.py` and `core/urls.py`
- **Purpose**: Add or modify views and urls

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Getting Started
1. **Fork** the repository
2. **Create** a new branch for your feature: `git checkout -b feature-name`
3. **Make** your changes with clear, descriptive commit messages
4. **Push** your branch: `git push origin feature-name`
5. **Open** a pull request with a detailed description

### Guidelines
- Follow existing code style and conventions
- Include relevant documentation for new features
- Add tests where applicable
- For major changes, open an issue first to discuss

### Bug Reports & Feature Requests
Open an issue on the [GitHub repository](https://github.com/ssshiponu/portfolio) with:
- Clear description of the issue or feature
- Steps to reproduce (for bugs)
- Expected vs actual behavior

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/ssshiponu/portfolio/issues)
- **Documentation**: This README and inline code comments
- **Community**: Contributions and discussions welcome

---

**🎉 Enjoy building your professional portfolio!**