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
                echo "building...${env.BRANCH_NAME}"                 
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
                sh 'printenv'
            }
        }
    }
post { 
    success {  echo 'this build was successful' }
    failure { echo 'this build failed' }   
 }
}
