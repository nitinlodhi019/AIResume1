# EpochFolio - AI-Powered Resume Screening Platform

A full-stack web application that uses advanced AI, NLP, and BERT models to intelligently screen and rank resumes based on job requirements.

## 🚀 Features

### Frontend
- **Beautiful UI/UX**: Modern, responsive design with smooth animations
- **3-Step Process**: Job Setup → Upload Resumes → View Results
- **Real-time Processing**: Live progress indicators and feedback
- **Advanced Filtering**: Filter candidates by score, category, skills
- **Bulk Operations**: Download filtered or all resumes
- **Authentication**: Complete auth flow with OTP verification

### Backend (AI/ML)
- **BERT Embeddings**: Semantic similarity using Sentence Transformers
- **NLP Processing**: Advanced text preprocessing with NLTK
- **Skill Extraction**: Rule-based skill identification from resumes
- **Resume Categorization**: Automatic categorization into job fields
- **Smart Scoring**: Multi-factor scoring algorithm
- **File Processing**: PDF, DOC, DOCX text extraction

### Database & Infrastructure
- **Supabase Integration**: PostgreSQL database with real-time features
- **Real OTP Emails**: SMTP email verification system
- **Secure Authentication**: Password hashing and session management
- **File Upload**: Secure file handling and storage
- **RESTful API**: Clean API design with proper error handling

## 🛠️ Tech Stack

### Frontend
- **Vanilla JavaScript**: Pure JS with modern ES6+ features
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide Icons**: Beautiful icon library
- **Responsive Design**: Mobile-first approach

### Backend
- **Flask**: Python web framework
- **Supabase**: PostgreSQL database and auth
- **NLTK**: Natural language processing
- **Sentence Transformers**: BERT embeddings
- **scikit-learn**: Machine learning utilities
- **PyPDF2 & python-docx**: Document processing

### AI/ML Libraries
- **sentence-transformers**: BERT-based semantic similarity
- **scikit-learn**: TF-IDF vectorization and cosine similarity
- **NLTK**: Text preprocessing and tokenization
- **numpy**: Numerical computations

## 📋 Prerequisites

- Python 3.8+
- Node.js (for development)
- Supabase account
- Gmail account (for SMTP)

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone <repository-url>
cd epochfolio
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_key

# Email (Gmail SMTP)
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password

# Optional: Hugging Face API
HF_API_KEY=your_hf_api_key
```

### 4. Database Setup (Supabase)

Create a `users` table in Supabase:
```sql
CREATE TABLE users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password_hash TEXT NOT NULL,
    otp TEXT,
    is_verified BOOLEAN DEFAULT FALSE,
    role TEXT,
    hr_id TEXT,
    full_name TEXT,
    position TEXT,
    department TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users can read own data" ON users
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own data" ON users
    FOR UPDATE USING (auth.uid() = id);
```

### 5. Gmail SMTP Setup

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
3. Use this app password in `SMTP_PASS`

### 6. Run Application
```bash
cd backend
python app.py
```

Visit `http://localhost:5000`

## 🎯 Usage

### 1. Authentication
- **Sign Up**: Create account with email verification
- **Sign In**: Login with credentials
- **Forgot Password**: Reset via OTP

### 2. Job Setup
- Define job title and description
- Add required skills and technologies
- Set experience level and job type
- Use quick templates for common roles

### 3. Upload Resumes
- Drag & drop or click to upload
- Supports PDF, DOC, DOCX files
- Bulk upload up to 1000 files
- Real-time processing feedback

### 4. View Results
- AI-powered candidate ranking
- Filter by score, category, skills
- View individual resumes
- Download filtered or all resumes
- Restart process for new screening

## 🧠 AI/ML Pipeline

### 1. Text Extraction
- **PDF**: PyPDF2 for text extraction
- **DOC/DOCX**: python-docx for document parsing
- **Preprocessing**: NLTK for cleaning and tokenization

### 2. Skill Extraction
- Rule-based matching against comprehensive skill database
- 200+ technical and soft skills
- Regex patterns for skill variations
- Deduplication and normalization

### 3. Resume Categorization
- Keyword-based categorization
- 15+ job categories (Tech, Marketing, Design, etc.)
- Hierarchical classification system
- Fallback to "Other" or "Uncategorized"

### 4. Semantic Similarity
- **Primary**: BERT embeddings via Sentence Transformers
- **Fallback**: TF-IDF vectorization with cosine similarity
- Normalized scoring (0-1 range)
- Context-aware matching

### 5. Scoring Algorithm
```python
# Weighted scoring components
WEIGHT_SEMANTIC = 0.35    # BERT/TF-IDF similarity
WEIGHT_SKILL_MATCH = 0.45 # Required skills matching
WEIGHT_EXPERIENCE = 0.20  # Experience level matching

final_score = (
    (semantic_similarity * WEIGHT_SEMANTIC) +
    (skill_match_percentage * WEIGHT_SKILL_MATCH) +
    (experience_score * WEIGHT_EXPERIENCE)
) * 100
```

## 📊 API Endpoints

### Authentication
- `POST /api/signup` - User registration
- `POST /api/login` - User login
- `POST /api/verify_otp` - OTP verification
- `POST /api/forgot_password` - Password reset request
- `POST /api/reset_password` - Password reset

### User Management
- `POST /api/select_role` - Set user role and HR info

### Job & Resume Processing
- `POST /api/job_requirements` - Save job requirements
- `POST /api/upload_resumes` - Upload resume files
- `POST /api/screen_resumes` - Process and score resumes
- `GET /api/dashboard_data` - Get screening results

### File Operations
- `GET /api/resume_raw_text/<id>` - Get resume text
- `GET /api/download_resume/<id>` - Download single resume
- `POST /api/download_all_filtered_resumes` - Download filtered resumes

## 🔧 Configuration

### Scoring Weights
Adjust in `backend/resume_matcher.py`:
```python
WEIGHT_SEMANTIC = 0.35    # Semantic similarity importance
WEIGHT_SKILL_MATCH = 0.45 # Skill matching importance  
WEIGHT_EXPERIENCE = 0.20  # Experience matching importance
```

### Skill Database
Extend in `backend/text_processor.py`:
```python
common_skills = [
    "python", "javascript", "react", "node.js",
    # Add more skills...
]
```

### Categories
Modify in `backend/text_processor.py`:
```python
categories = {
    "Tech": ["software", "developer", "engineer", ...],
    "Marketing": ["marketing", "seo", "content", ...],
    # Add more categories...
}
```

## 🚀 Deployment

### Render.com (Recommended)
1. Connect GitHub repository
2. Set environment variables
3. Deploy with auto-scaling

### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
heroku config:set SUPABASE_URL=your_url
heroku config:set SUPABASE_KEY=your_key
# ... set other env vars
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🔒 Security Features

- **Password Hashing**: Werkzeug secure password hashing
- **OTP Verification**: Time-limited email verification
- **Input Validation**: Comprehensive form validation
- **File Security**: Secure file upload and storage
- **SQL Injection Protection**: Parameterized queries
- **CORS Configuration**: Proper cross-origin setup

## 🧪 Testing

### Manual Testing
1. **Authentication Flow**: Sign up → OTP → Login
2. **Job Setup**: Create job with skills
3. **File Upload**: Upload various file types
4. **AI Processing**: Verify scoring accuracy
5. **Filtering**: Test all filter options
6. **Downloads**: Test bulk download features

### Demo Credentials
- **Email**: demo@example.com
- **Password**: password123
- **OTP**: 123456 (for testing)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support, email support@epochfolio.com or create an issue on GitHub.

## 🙏 Acknowledgments

- **Sentence Transformers** for BERT embeddings
- **NLTK** for natural language processing
- **Supabase** for backend infrastructure
- **Tailwind CSS** for beautiful styling
- **Lucide** for clean icons

---

**EpochFolio** - Revolutionizing recruitment with AI-powered resume screening. 🚀
