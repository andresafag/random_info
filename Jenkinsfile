pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh '. env/Scripts/activate'
                sh 'python -m pytest --junitxml=report.xml'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
