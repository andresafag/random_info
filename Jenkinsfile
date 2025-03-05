pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                sh 'echo $PATH'
            }
        }
        stage('Test') {
                agent {
                    docker {
                        image 'node:23-alpine3.20'
                    }
                }
            steps {
                node --version
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
