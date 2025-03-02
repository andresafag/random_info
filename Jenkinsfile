pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh 'echo "Hello World"'
                sh 'echo %PATH%'
            }
        }
        stage('Test') {
                agent {
                    label 'original'
                }
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
