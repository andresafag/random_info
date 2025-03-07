pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh '. env/Scripts/activate'
                sh 'pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
