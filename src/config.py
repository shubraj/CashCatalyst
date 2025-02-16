import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '..', 'instance', 'cash_flow.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "dfab546a7e1f33bf4d2dc39224c985f3eda46d1678f1dc3f25"
    # if os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").lower() == "production":
    #     SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASS')}@{os.environ.get('DATABASE_HOST')}/{os.environ.get('DATABASE_NAME')}"
    # else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    UPLOAD_FOLDER = os.path.join(basedir, '..', 'uploads')
    
    # Print the Anthropic API key status for debugging
    print(f"Database: {SQLALCHEMY_DATABASE_URI}")
    print(f"Anthropic API Key status: {'Set' if ANTHROPIC_API_KEY else 'Not set'}")