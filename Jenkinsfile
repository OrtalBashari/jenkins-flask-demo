pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'
            reuseNode true
        }
    }

    stages {
        stage('Initialize Environment') {
            steps {
                echo "Initializing Python environment..."
                sh 'python --version' 
                sh 'pip --version' 
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo "Installing Python packages from requirements.txt..."
                // 💡 תיקון: הוספת הדגל להתקנה בתוך סביבת המשתמש (ללא צורך ב-root)
                sh 'pip install -r requirements.txt --break-system-packages' 
            }
        }
        
        stage('Run Tests (Optional)') {
            steps {
                sh '''
                echo "Running unit tests (if applicable)..."
                echo "No tests configured yet. Skipping."
                '''
            }
        }
        
        stage('Final Build Status') {
            steps {
                echo "Build completed successfully. Ready for Deployment."
            }
        }
    }
}