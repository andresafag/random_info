pipeline {
    agent {
        label 'andres_label'
    }
    parameters{
        credentials(name: '95007d8f-9558-40e2-ba29-0d28917757f7', credentialType: 'Secret text')
    }
    stages { 
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
