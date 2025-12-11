pipeline {
    // 💡 Agent: הפעלת כל הפייפליין בתוך קונטיינר Python
    agent {
        docker {
            image 'python:3.10-slim' // או כל גרסת Python שתבחרי
            reuseNode true          // שימוש חוזר בקונטיינר לכל השלבים
        }
    }

    stages {
        stage('Initialize Environment') {
            steps {
                // בדיקת סביבה
                echo "Initializing Python environment..."
                sh 'python --version' 
                sh 'pip --version' 
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // 1. התקנת התלויות מ-requirements.txt
                echo "Installing Python packages from requirements.txt..."
                // הפקודה שרצה: pip install -r requirements.txt
                sh 'pip install -r requirements.txt' 
            }
        }
        
        stage('Run Tests (Optional)') {
            steps {
                // 2. הרצת בדיקות (בהנחה שיש לך קובץ בדיקה, לדוגמה)
                echo "Running unit tests (if applicable)..."
                // אם את משתמשת ב-pytest:
                // sh 'pip install pytest'
                // sh 'pytest' 
                
                // אם אין לך בדיקות כרגע, אפשר להשאיר 'echo' או להסיר את ה-Stage
                sh 'echo "No tests configured yet. Skipping."'
            }
        }
        
        stage('Final Build Status') {
            steps {
                echo "Build completed successfully. Ready for Deployment."
            }
        }
    }
}