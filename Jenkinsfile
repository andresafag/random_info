pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install selenium'
            }
        }
        stage('Test') {
            steps {
                sh 'python testing_page.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
