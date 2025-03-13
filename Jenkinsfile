pipeline {
    agent any
        environment {
        DEPLOY_ENV = 'staging'
    }
    parameters {
        string(name: 'prueba', defaultValue: 'pruebita')
        }

    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                echo "building"                
                echo "y el estado del repo es ${DEPLOY}"
            }
        }
    
        stage('Deploy') {
            when {
                allOf {
                    environment name: 'DEPLOY_ENV', value: 'staging'
                    expression { params.prueba == 'pruebita'}
                }
            }
            steps {
                echo 'Deploying...failing'
            }
        }
    }
post { 
    success {  echo 'this build was successful' }
    failure { echo 'this build failed' }   
 }
}
