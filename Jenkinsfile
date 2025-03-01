pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
            }
        }
        stage('Test') {
                agent {
                    label 'andres_label'
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
