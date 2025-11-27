pipeline{
    agent any
    
    environment {
        VENV_DIR = 'venv'
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
    }
}