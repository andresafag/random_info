pipeline {
    agent any
        environment {
        DEPLOY_ENV = 'staging'
        BRANCH_NAME = 'main'
        AWS_DEFAULT_REGION= 'us-east-2'
    }
    parameters {
        string(name: 'prueba', defaultValue: 'pruebita')
        }

    stages { 
        stage('Build') {
            steps {
                echo "building...${env.BRANCH_NAME}"                 
            }
        }
    
        stage('Deploy') {
            when {
                anyOf {
                    environment name: 'DEPLOY_ENV', value: 'staging'
                    expression { params.prueba == 'pruebita'}
                    environment name: 'BRANCH_NAME', value: 'main'
                    environment name: 'BUILD_NUMBER', value: '156'
                }
            }
            steps {
                echo 'Deploying...succeding'
                sh '''
                  aws rds describe-db-instances --region $AWS_DEFAULT_REGION --profile danielitosso 
                '''
            }
        }
    }
post { 
    success {  echo 'this build was successful' }
    failure { echo 'this build failed' }   
 }
}
