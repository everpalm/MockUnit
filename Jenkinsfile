pipeline {
    agent {
        label 'test_mock_unit'
    }
    stages {
        stage('Build Docker Image') {
            steps {
                // 构建 Docker 镜像
                sh 'docker build -t mock_unit .'
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
