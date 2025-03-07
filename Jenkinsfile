pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh '. env/Scripts/activate'
                sh 'cd test && pytest test_page.py'
                sh 'ls'
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
