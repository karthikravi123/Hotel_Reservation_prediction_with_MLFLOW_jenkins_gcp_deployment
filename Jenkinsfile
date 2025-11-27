pipeline {
    agent any

    environment {
        GCP_PROJECT = "lithe-bazaar-478509-e1"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages {

        stage('Cloning GitHub Repo') {
            steps {
                script {
                    echo 'Cloning GitHub repository...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/karthikravi123/Hotel_Reservation_prediction_with_MLFLOW_jenkins_gcp_deployment.git'
                        ]]
                    )
                }
            }
        }

        stage('Install Dependencies in Jenkins Container') {
            steps {
                script {
                    echo 'Installing Python dependencies...'
                    sh '''
                        python3 -m pip install --upgrade pip
                        python3 -m pip install -e .
                    '''
                }
            }
        }

        stage('Build and Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp_key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing Docker image to GCR...'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}

                            echo "Authenticating with GCP..."
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                            gcloud config set project ${GCP_PROJECT}

                            echo "Enabling Docker auth..."
                            gcloud auth configure-docker --quiet

                            echo "Building Docker image..."
                            docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                            echo "Pushing Docker image..."
                            docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }
    }
}
