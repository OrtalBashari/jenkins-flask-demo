pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/OrtalBashari/jenkins-flask-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myflaskapp .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f flask_container || true
                    docker run -d --name flask_container -p 80:5000 myflaskapp
                '''
            }
        }
    }
}
