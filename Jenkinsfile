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
                        image 'maven:3-alpine'
                    }
                }
            steps {
                mvn --version
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
