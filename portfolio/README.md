# Portfolio Website - Rishikesh Deshetty

A modern, responsive portfolio website built with **React**, **TypeScript**, **TailwindCSS**, and **FastAPI**. This project showcases professional experience, education, skills, and projects with a clean, interactive UI.

## 🚀 Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Dynamic Content**: All data fetched from REST API endpoints
- **Interactive UI**: Smooth animations and transitions using Framer Motion
- **Contact Form**: Stores submissions in SQLite database
- **Project Filtering**: Filter projects by technology stack
- **Modern Stack**: React 18, TypeScript, TailwindCSS, FastAPI
- **Type-Safe**: Full TypeScript support on frontend
- **RESTful API**: Clean API design with FastAPI

## 📁 Project Structure

```
portfolio/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI app and routes
│   │   ├── models.py       # SQLAlchemy models
│   │   ├── schemas.py      # Pydantic schemas
│   │   └── database.py     # Database configuration
│   ├── init_db.py          # Database initialization script
│   ├── requirements.txt    # Python dependencies
│   └── portfolio.db        # SQLite database (created on first run)
├── frontend/                # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/     # Reusable React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API service layer
│   │   ├── App.tsx         # Main app component
│   │   ├── main.tsx        # Entry point
│   │   └── index.css       # Global styles
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── tailwind.config.js
└── README.md               # This file
```

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **TailwindCSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **React Router** - Client-side routing
- **Axios** - HTTP client

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **SQLite** - Lightweight database
- **Uvicorn** - ASGI server

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **Python** (3.8 or higher) - [Download](https://www.python.org/)
- **npm** or **yarn** - Comes with Node.js
- **pip** - Comes with Python

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd portfolio
```

### 2. Backend Setup

#### Step 1: Navigate to backend directory
```bash
cd backend
```

#### Step 2: Create virtual environment (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Initialize the database with sample data
```bash
python init_db.py
```

This will create a `portfolio.db` file and populate it with your resume data.

#### Step 5: Start the backend server
```bash
# Option 1: Using Python directly
python -m app.main

# Option 2: Using Uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### 3. Frontend Setup

#### Step 1: Open a new terminal and navigate to frontend directory
```bash
cd frontend
```

#### Step 2: Install dependencies
```bash
npm install
```

#### Step 3: Start the development server
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

### 4. Access the Application

Open your browser and navigate to:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Swagger UI)

## 📡 API Endpoints

### Experiences
- `GET /api/experiences` - Get all work experiences
- `POST /api/experiences` - Create new experience

### Projects
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Create new project

### Skills
- `GET /api/skills` - Get all skills
- `POST /api/skills` - Create new skill

### Education
- `GET /api/education` - Get all education records
- `POST /api/education` - Create new education record

### Contact
- `POST /api/contact` - Submit contact form
- `GET /api/contact` - Get all contact messages

## 🎨 Customization

### Update Your Information

1. **Edit Database Initialization**:
   - Open `backend/init_db.py`
   - Update the data arrays with your information
   - Run `python init_db.py` to reinitialize the database

2. **Update Colors**:
   - Edit `frontend/tailwind.config.js`
   - Modify the `colors` section in the `theme.extend` object

3. **Update Contact Information**:
   - Edit `frontend/src/components/Footer.tsx`
   - Edit `frontend/src/pages/ContactPage.tsx`

### Add Your Resume PDF

1. Place your resume PDF in `frontend/public/` directory
2. Name it `Rishikesh_Deshetty_Resume.pdf` or update the links in:
   - `frontend/src/components/Navbar.tsx`
   - `frontend/src/pages/Home.tsx`

## 🏗️ Building for Production

### Frontend

```bash
cd frontend
npm run build
```

The production build will be in the `frontend/dist` directory.

### Backend

The FastAPI backend can be deployed to:
- **Render** - Free tier available
- **Heroku** - Easy deployment
- **Railway** - Modern platform
- **DigitalOcean** - VPS hosting
- **AWS/GCP/Azure** - Cloud platforms

For production, consider:
1. Using PostgreSQL instead of SQLite
2. Setting up environment variables
3. Enabling HTTPS
4. Adding authentication if needed

## 🧪 Development Commands

### Backend

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run development server
uvicorn app.main:app --reload

# Initialize/Reset database
python init_db.py

# Install new package
pip install <package-name>
pip freeze > requirements.txt
```

### Frontend

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Install new package
npm install <package-name>
```

## 📝 Environment Variables

### Backend (.env)

Create a `.env` file in the `backend` directory:

```env
DATABASE_URL=sqlite:///./portfolio.db
SECRET_KEY=your-secret-key-here
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Frontend

Create a `.env` file in the `frontend` directory:

```env
VITE_API_URL=http://localhost:8000
```

## 🐛 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError`
```bash
# Solution: Ensure virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

**Problem**: Database errors
```bash
# Solution: Reinitialize the database
python init_db.py
```

### Frontend Issues

**Problem**: `Cannot find module` errors
```bash
# Solution: Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**Problem**: Port already in use
```bash
# Solution: Kill the process or use a different port
npm run dev -- --port 3000
```

## 📦 Deployment

### Deploy Frontend to Vercel

```bash
cd frontend
npm install -g vercel
vercel
```

### Deploy Backend to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Contact

**Rishikesh Deshetty**
- Email: rishikesh.d1020@gmail.com
- Phone: +1 (818) 930-4585
- Location: Minneapolis, MN 55417

## 🙏 Acknowledgments

- React Team for the amazing framework
- FastAPI for the modern Python web framework
- TailwindCSS for the utility-first CSS framework
- Framer Motion for smooth animations

---

**Made with ❤️ by Rishikesh Deshetty**
