pipeline {
    agent any

    environment {
        dockerHubRegistry = 'klksm2'
        dockerHubRegistryCredential = 'docker-hub'
        githubCredential = 'github_cred'
    }

    stages {
        // 1. 소스코드 체크아웃
        stage('Check out application git branch') {
            steps {
                checkout scm
            }
            post {
                failure { echo 'Repository checkout failure' }
                success { echo 'Repository checkout success' }
            }
        }

        // 2. Docker 이미지 빌드
        stage('Docker image build') {
            steps {
                
                    sh "docker build -t ${dockerHubRegistry}/flask-app:${currentBuild.number} ."
                    sh "docker tag ${dockerHubRegistry}/flask-app:${currentBuild.number} ${dockerHubRegistry}/flask-app:latest"
                }
            
            post {
                failure { echo 'Docker image build failure!' }
                success { echo 'Docker image build success!' }
            }
        }

        // 3. Docker 이미지 푸시
        stage('Docker image push') {
            steps {
                withDockerRegistry([credentialsId: dockerHubRegistryCredential, url: "" ]) {
                    sh "docker push ${dockerHubRegistry}/flask-app:${currentBuild.number}"
                    sh "docker push ${dockerHubRegistry}/flask-app:latest"
                }
            }
            post {
                failure {
                    echo 'Docker Image Push failure!'
                    sh "docker rmi ${dockerHubRegistry}/flask-app:${currentBuild.number} || true"
                    sh "docker rmi ${dockerHubRegistry}/flask-app:latest || true"
                }
                success {
                    echo 'Docker image push success!'
                    sh "docker rmi ${dockerHubRegistry}/flask-app:${currentBuild.number} || true"
                    sh "docker rmi ${dockerHubRegistry}/flask-app:latest || true"
                }
            }
        }

        // 4. K8S Manifest Update & Push
        stage('K8S Manifest Update') {
            steps {
                sh "rm -rf gitOpsRepo"
                sh "mkdir -p gitOpsRepo"
                dir("gitOpsRepo") {
                    git branch: "main",
                        credentialsId: githubCredential,
                        url: 'https://github.com/klksm2/manifest.git'

                    sh "git config --global user.email 'klksm99@nate.com'"
                    sh "git config --global user.name 'klksm2'"

                    // flask-deployment.yaml의 image 태그를 최신 빌드번호로 치환
                    sh "sed -i 's|image: ${dockerHubRegistry}/flask-app:.*|image: ${dockerHubRegistry}/flask-app:${currentBuild.number}|g' flask-deployment.yaml"

                    sh "git add flask-deployment.yaml"
                    sh "git commit -m '[UPDATE] flask image version ${currentBuild.number}' || true"

                    withCredentials([gitUsernamePassword(credentialsId: githubCredential, gitToolName: 'git-tool')]) {
                        sh "git remote set-url origin https://github.com/klksm2/manifest.git"
                        sh "git push -u origin main --force"
                    }
                }
            }
            post {
                failure { echo 'K8S Manifest Update failure!' }
                success { echo 'K8S Manifest Update success!' }
            }
        }
    }
}
