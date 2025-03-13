pipeline {
    agent any
    parameters {
        string(name: 'prueba', defaultValue: 'pruebita')
        }
    stages { 
        stage('Build') {
            steps {
                echo 'Building... and go'
                echo "building"                
                echo "${GITHUB_URL}"
                echo "y el estado del repo es ${DEPLOY}"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                }
            }
        }
        stage('Deploy') {
            when {
                allOf {
                    branch 'main'
                    environment name: 'prueba', value: 'pruebita'
                }
            }
            steps {
                echo 'Deploying...failing'
            }
        }
post { 
    success {  echo 'this build was successful' }
    failure { echo 'this build failed' }   
 }
}
