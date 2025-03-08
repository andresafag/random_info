pipeline {
    agent any
        environment {
        NEXT_STAGE = ""
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
                        currentBuild.result = 'SUCCESS'
//                        env.STATUS = "SUCCESS"
//                        echo "este es el status actual ${env.STATUS}"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        echo "este es el error ${e}"

//                        env.STATUS = "FAILURE"
//                        echo "este es el status actual ${env.STATUS}"
                    }
                }
            }
        }
        stage('Deploy') {
            when {
                expression {  currentBuild.result == "FAILURE" }
            }
            steps {
                echo 'Deploying...successfully'
            }
        }
            stage('Deploysuccess') {
            when {
                expression {  currentBuild.result == "SUCCESS" }
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
