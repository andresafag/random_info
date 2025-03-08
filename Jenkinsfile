pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                // Activate the virtual environment
                sh 'python3 -m venv env'
                sh 'env/Scripts/activate'
                sh "pip list"
                sh 'which python'
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
