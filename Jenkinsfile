pipeline {
    agent any
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                echo "building"                
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                . env/Scripts/activate
                ls
                python -m pytest 
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
