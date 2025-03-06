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
