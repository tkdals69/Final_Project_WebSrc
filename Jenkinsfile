pipeline {
    agent any

    environment {
        IMAGE_NAME = "klksm2/flask-app"   // Docker Hub repo
        IMAGE_TAG  = "latest"
    }

    stages {
        stage('Clone repository') {
            steps {
                git url: 'https://github.com/tkdals69/Final_Project_WebSrc', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'klksm2',   
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }
    }
}
