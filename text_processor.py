# text_processor.py
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK data if not already present
try:
    stopwords.words('english')
except LookupError:
    import nltk

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove special characters and numbers (keep only letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stop words and lemmatize
    processed_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(processed_tokens)


def extract_skills_from_text(text):
    # This is a very basic rule-based skill extraction.
    # For a real application, you'd use a pre-trained NER model (e.g., SpaCy's 'en_core_web_lg' or a custom one)
    # or a comprehensive skill dictionary.

    # Example common skills (expand this list significantly)
    common_skills = [
        "python", "java", "javascript", "react", "node.js", "sql", "aws", "docker",
        "kubernetes", "machine learning", "data analysis", "project management",
        "agile", "scrum", "communication", "leadership", "figma", "photoshop",
        "seo", "marketing", "finance", "hr", "sales", "engineering", "design"
    ]

    found_skills = []
    processed_text = text.lower()  # Ensure text is lowercased for matching

    for skill in common_skills:
        if skill in processed_text:
            found_skills.append(skill.replace('.', ''))  # Clean up for display

    return list(set(found_skills))  # Return unique skills
