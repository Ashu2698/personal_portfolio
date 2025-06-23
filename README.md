# Django Portfolio Website

A professional, open-source Django portfolio website with admin-managed content and modern responsive design. Perfect for developers, designers, and creative professionals looking to showcase their work.

## 🌟 Features
- **Effortless Setup**: Designed for non-developers also with a simple, guided installation process
- **Responsive Design**: Modern, mobile-first layout with light/dark theme support
- **Content Management**: Intuitive admin dashboard for managing projects, skills, and personal information
- **SEO Ready**: Built-in SEO optimization with robots.txt and sitemap.xml
- **Free Hosting**: Designed for easy deployment on PythonAnywhere
- **Customizable**: Flexible template system and modular design

## 🎯 Live Demo

View the live demo at: [mohinuddinshipon.pythonanywhere.com](https://mohinuddinshipon.pythonanywhere.com)

## 🛠️ Technology Stack

- **Backend**: Django 5.x
- **Frontend**: HTML5, CSS3, TailwindCSS, JavaScript
- **Database**: SQLite (It is more than enough)
- **Hosting**: PythonAnywhere (free)
- **Python**: 3.10+ (recommended: 3.12+)

## 🚀 Quick Start

Choose your deployment method:

### Option A: Direct Deployment (Recommended for beginners or None developers)
Deploy directly to PythonAnywhere without local setup - perfect for content-only customization.

### Option B: Local Development
Set up locally for design customization and advanced features.

---

## 🌐 PythonAnywhere Deployment

### Prerequisites
- Free PythonAnywhere account ([signup here](https://pythonanywhere.com))
- Your username will determine your domain: `username.pythonanywhere.com`

### Deployment Steps

1. **Create Web App**
   - Go to **Web** tab → **Add a new web app**
   - Select: **Django** → **Python 3.12** → Name: `portfolio`

2. **Install via Console**
   - Navigate to **Consoles** tab → **Start Bash console**
   - Run the following commands:
   ```bash
   rm -rf portfolio/
   git clone https://github.com/ssshiponu/portfolio
   cd portfolio
   ./setup.sh
   ```

3. **Activate Your Site**
   - Return to **Web** tab → Click **Reload**
   - Your site is now live at `username.pythonanywhere.com`

### First-Time Setup
1. Visit `username.pythonanywhere.com/admin`
2. Login with default credentials:
   - **Username**: `admin`
   - **Password**: `password`
3. **⚠️ Important**: Change your password immediately after first login

---

## 📊 Content Management

### Admin Dashboard
Access your admin panel at `/admin` to manage:
- **Hide Section**: from the `Sections`, you can hide any section.
- **Personal Profile**: Bio, contact info, social links
- **Projects**: Portfolio items with descriptions, images, and links
- **Skills**: Technical skills with proficiency levels
- **Development Process**: Your workflow and methodologies
- **Site Metadata**: SEO settings and site information

### Content Guidelines
- **Images**: Use high-quality images (recommended aspect-ratio 4:3 and minimum height 320px for projects)
- **Descriptions**: You can add html formate in description.
- **Links**: Ensure all external links are working and use HTTPS
- **Skills**: Organize skills by categories for better presentation

---

## 💻 Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/ssshiponu/portfolio.git
cd portfolio
```

### 2. Create Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

#### Generate Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### Set Environment Variables

**Option 1: Environment Variables**

Windows (CMD):
```cmd
set SECRET_KEY=your_generated_secret_key_here
```

Windows (PowerShell):
```powershell
$env:SECRET_KEY="your_generated_secret_key_here"
```

macOS/Linux:
```bash
export SECRET_KEY=your_generated_secret_key_here
```

**Option 2: .env File (Recommended)**
Create `.env` in project root:
```env
SECRET_KEY=your_generated_secret_key_here
DEBUG=True
```

### 5. Prepare Static Files
```bash
python manage.py collectstatic
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view your site.

---



## 🎨 Customization Guide

### Template Structure
```
templates/
├── base.html              # Main layout
├── index.html            # Homepage
├── components/           # Reusable components
└── admin/               # Admin customizations
```

### Static Files Organization
```
static/
├── css/                 # Stylesheets
├── js/                  # JavaScript files
├── images/              # Site images
└── vendor/              # Third-party libraries
```

### Key Customization Points

**Colors & Themes:**
- Edit `static/css/main.css` for color schemes
- Modify CSS variables for consistent theming

**Layout Changes:**
- Update `templates/base.html` for site-wide changes
- Modify individual templates for page-specific layouts

**Functionality:**
- Add new models in `core/models.py`
- Create views in `core/views.py`
- Define URLs in `core/urls.py`

---

## 🔧 Advanced Configuration

### Database Migration
If you modify models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Superuser
```bash
python manage.py createsuperuser
```

### Production Settings
For production deployment:
1. Set `DEBUG=False` in environment
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL for better performance
4. Enable HTTPS

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

### Reporting Issues
Open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

---

## 📚 Resources

- **Repository**: [GitHub](https://github.com/ssshiponu/portfolio)
- **Issues**: [Bug Reports & Feature Requests](https://github.com/ssshiponu/portfolio/issues)
- **Django Documentation**: [djangoproject.com](https://docs.djangoproject.com/)
- **PythonAnywhere Help**: [pythonanywhere.com/help](https://help.pythonanywhere.com/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Ready to Build Your Portfolio?

Start showcasing your work professionally with this Django portfolio website. Whether you're a developer, designer, or creative professional, this platform provides everything you need to create an impressive online presence.

**Questions?** Open an issue or reach out through the repository discussions.

---

*Built with ❤️ using Django*