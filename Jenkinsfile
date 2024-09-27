pipeline {
    agent {
        label 'test_mock_unit'
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                            sh('echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin')
                            sh """
                            docker build -t mock_unit .
                            """
                        }
                    } catch (e) {
                        echo "An error occurred during the docker-build process: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Run Tests in Docker Container') {
            steps {
                // 运行 Docker 容器并执行测试
                sh '''
                    docker run --name mock_unit_container --privileged -v /dev/mem:/dev/mem mock_unit
                '''
            }
        }
    }
    post {
        always {
            // 清理容器和镜像
            sh '''
                docker stop mock_unit_container || true
                docker rm mock_unit_container || true
            '''
        }
    }
}
