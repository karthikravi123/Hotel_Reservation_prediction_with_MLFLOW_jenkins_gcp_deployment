pipeline{
    agent any
    
    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "lithe-bazaar-478509-e1"
        GCLOUD_PATH ="/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages {
        stage('cloning github repo to Jenkins'){
            steps{
                script{
                    echo 'cloning github repo to Jenkins................-->'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/karthikravi123/Hotel_Reservation_prediction_with_MLFLOW_jenkins_gcp_deployment.git']])
            }
        }
        }

        stage('setting up virtual env and install dependenicies '){
            steps{
                script{
                    echo 'setting up virtual env and install dependenicies...............-->'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
            }
        }
        }


        stage('building and pushing docker image to GCR '){
            steps{
                withCredentials([file(credentialsId: 'gcp_key',variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'building and pushing docker image to GCR................'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS} 
                        
                        glcoud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest


                        
                        '''
                    }
                }
        }
        }

    }
}