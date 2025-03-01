pipeline {
    agent {
        node {
            label 'andres_label'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out...'
                // Add your checkout steps here
                
                git credentialsId: 'b5612281-71cc-4d12-8268-75b4105117d2', url: 'https://github.com/andresafag/random_info.git'
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