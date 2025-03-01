pipeline {
    agent {
        node {
            label 'andres_label'
        }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out...'
                // Add your checkout steps here       
                git credentialsId: '95007d8f-9558-40e2-ba29-0d28917757f7', url: 'https://github.com/andresafag/random_info.git'
            }
        }
    }
        stage('Build') {
            steps {
                echo 'Building...'
                // Add your build steps here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add your deploy steps here
            }
        }
    }
}