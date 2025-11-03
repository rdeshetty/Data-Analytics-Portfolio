"""
Script to initialize the database with sample data from Rishikesh Deshetty's resume
"""
from app.database import SessionLocal, engine
from app import models

def init_database():
    # Create all tables
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(models.Experience).delete()
        db.query(models.Project).delete()
        db.query(models.Skill).delete()
        db.query(models.Education).delete()
        
        # Add Experiences
        experiences = [
            models.Experience(
                company="Coder's data LLC (Pacific Sunwear)",
                position="Data Analyst",
                duration="Dec 2023 - Present",
                description="""• Partner with cross-functional and offshore teams to maintain and validate provider and vendor data across systems, ensuring 99% data accuracy.
• Translate business requirements into analytical reports using Excel and SQL, enabling leadership to monitor key operational metrics.
• Performed advanced data cleaning, deduplication, and validation across multiple data sources to strengthen contract data governance.
• Automated recurring reporting processes in Python, reducing manual reporting time by 25% and improving efficiency.
• Collaborated with engineers to deploy analytical models and automate workflows in AWS Lambda environments.
• Delivered actionable insights to management through dashboards and presentations, influencing decision-making on data integrity and compliance.
• Led code reviews and ensured production-ready standards for Python-based data pipelines and analytics workflows.""",
                is_current=True
            ),
            models.Experience(
                company="Ayant Software Pvt. Ltd",
                position="Jr. Data Analyst",
                duration="Jan 2021 - Nov 2022",
                description="""• Processed large-scale provider and claim datasets with precision, ensuring compliance with business and data governance standards.
• Conducted data mapping and validation before system uploads, improving accuracy of provider records by 30%.
• Developed and maintained Excel dashboards to track contract KPIs and identify discrepancies in data submissions.
• Collaborated with senior analysts to automate repetitive data-cleaning processes using SQL and Python.
• Supported cloud data migration projects involving AWS S3 and GCP BigQuery environments.
• Supported automation and efficiency improvements through Python and SQL scripts for data processing.""",
                is_current=False
            )
        ]
        
        for exp in experiences:
            db.add(exp)
        
        # Add Projects
        projects = [
            models.Project(
                title="Air Quality Index Prediction",
                description="Predicted and evaluated the Air Quality Index using Machine Learning, applied machine learning techniques to forecast PM2.5 levels based on daily weather and traffic data. Simplified the problem to a binary classification of 'High' or 'Low' PM2.5 levels, using a threshold of 115 µg/m³ for mild pollution. Ensured model accuracy through rigorous testing and validation.",
                technologies="Python, Pandas, Scikit-learn, Machine Learning, Data Analysis",
                github_url="https://github.com/yourusername/air-quality-prediction"
            ),
            models.Project(
                title="Loan Default Prediction using ANN",
                description="Performed EDA, Feature Engineered data, Preprocessed Data, predicted and evaluated whether or not a borrower will pay back their loan, which also helps to assess based on a new potential customer in the future, using Artificial Neural Networks (ANN) model. Used data from Lending Club with information on whether or not the borrower defaulted (charge-off).",
                technologies="Python, TensorFlow, Keras, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn",
                github_url="https://github.com/yourusername/loan-default-prediction"
            ),
            models.Project(
                title="Text Summarization System",
                description="Designed and implemented a text summarization system with key features including sentence segmentation, tokenization, and stop word removal using NLTK. Created a user-friendly web application using Flask and Python, allowing users to paste URLs and obtain summarized content with essential points. Conducted extensive testing to ensure accurate summarization and user interface functionality.",
                technologies="Python, NLTK, Flask, HTML/CSS, Natural Language Processing",
                github_url="https://github.com/yourusername/text-summarization"
            )
        ]
        
        for proj in projects:
            db.add(proj)
        
        # Add Skills
        skills = [
            # Analytics Tools
            models.Skill(name="Excel", category="Analytics Tools", proficiency=95),
            models.Skill(name="Power BI", category="Analytics Tools", proficiency=85),
            models.Skill(name="Tableau", category="Analytics Tools", proficiency=85),
            models.Skill(name="Alteryx", category="Analytics Tools", proficiency=70),
            models.Skill(name="Google Sheets", category="Analytics Tools", proficiency=90),
            
            # Databases
            models.Skill(name="SQL", category="Databases", proficiency=90),
            models.Skill(name="PL/SQL", category="Databases", proficiency=80),
            models.Skill(name="PostgreSQL", category="Databases", proficiency=85),
            models.Skill(name="MySQL", category="Databases", proficiency=85),
            
            # Programming
            models.Skill(name="Python", category="Programming", proficiency=90),
            models.Skill(name="Pandas", category="Programming", proficiency=90),
            models.Skill(name="NumPy", category="Programming", proficiency=85),
            models.Skill(name="Matplotlib", category="Programming", proficiency=85),
            models.Skill(name="R", category="Programming", proficiency=70),
            
            # Platforms
            models.Skill(name="AWS", category="Platforms", proficiency=75),
            models.Skill(name="GCP", category="Platforms", proficiency=70),
            models.Skill(name="SharePoint", category="Platforms", proficiency=80),
            
            # Soft Skills
            models.Skill(name="Analytical Thinking", category="Soft Skills", proficiency=95),
            models.Skill(name="Problem Solving", category="Soft Skills", proficiency=95),
            models.Skill(name="Data Storytelling", category="Soft Skills", proficiency=90),
            models.Skill(name="Global Communication", category="Soft Skills", proficiency=90),
            models.Skill(name="Stakeholder Management", category="Soft Skills", proficiency=85),
        ]
        
        for skill in skills:
            db.add(skill)
        
        # Add Education
        education = [
            models.Education(
                institution="Concordia University, St Paul",
                degree="Master of Science",
                field_of_study="Information Technology Management",
                gpa="4.0/4.0",
                graduation_date="Aug 2024",
                location="Minnesota, USA"
            ),
            models.Education(
                institution="Jawaharlal Nehru Technological University",
                degree="Bachelor of Technology",
                field_of_study="Information Technology",
                gpa="3.7/4.0",
                graduation_date="Aug 2022",
                location="Hyderabad, India"
            )
        ]
        
        for edu in education:
            db.add(edu)
        
        db.commit()
        print("✅ Database initialized successfully with sample data!")
        print("📊 Added:")
        print("   - 2 Work Experiences")
        print("   - 3 Projects")
        print("   - 23 Skills across 5 categories")
        print("   - 2 Education records")
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
