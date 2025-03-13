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
            }
        }
    
        stage('Deploy') {
            when {
                allOf {
                    environment name: 'DEPLOY_ENV', value: 'staging'
                    expression { params.prueba == 'pruebita'}
                    expression { env.BRANCH_NAME == 'main' }
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
