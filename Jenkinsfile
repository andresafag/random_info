pipeline {
    agent {
        label 'andres_label'
    }
    stages { 
        stage('Build') {
            steps {
                echo 'Building...'
                //hola
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            agent {
            label 'andres_label'
            }
            steps {
                echo 'Deploying...'
            }
        }
    }
}
