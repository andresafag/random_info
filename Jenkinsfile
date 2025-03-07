pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh '. env/Scripts/activate'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test/*'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
