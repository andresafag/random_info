pipeline {
    agent any
    environment {
        STATUS = ""
    }
    parameters {
        string(name: 'GITHUB_URL', defaultValue: 'la direccion de github es https://github.com/andresafag/random_info', description: 'URL of the repository')
        booleanParam(name: 'DEPLOY', defaultValue: true, description: 'Deploy after build?')
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
                script {
                    try {
                        sh '''
                            . env/Scripts/activate
                            ls
                            python -m pytest 
                            which python
                        '''
                    } catch (Exception e) {
                        env.STATUS="FAILURE"
                    }
                }
                
            }
        }
        stage('Deploy') {
            when {
                expression {  env.STATUS == "FAILURE" }
            }
            steps {
                echo 'Deploying...successfully'
            }
        }
    }
post { 
    success { echo 'this build was successful' }
    failure { echo 'this build failed' }   
 }
}
