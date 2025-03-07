pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh '. env/Scripts/activate'
                sh 'pip list'
                sh 'pytest test/test_page.py'
            }
        }
        stage('Test') {
            steps {
                sh 'ls'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
