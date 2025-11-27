pipeline{
    agent any
    
    stages {
        stage('cloning github repo to Jenkins'){
            steps{
                script{
                    echo 'cloning github repo to Jenkins................-->'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/karthikravi123/Hotel_Reservation_prediction_with_MLFLOW_jenkins_gcp_deployment.git']])
            }
        }
        }
    }
}