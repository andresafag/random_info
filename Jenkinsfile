pipeline {
    agent {
        label 'andres_label'
    }
    stages { 
        stage('Build') {
            steps {
                withcredentials([string(credentialsId: '95007d8f-9558-40e2-ba29-0d28917757f7')])
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
