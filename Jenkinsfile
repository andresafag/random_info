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
    
        stage('Deploy') {
            when {
                allOf {
                    expression {
                        return params.prueba == 'pruebita'
                    }
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
