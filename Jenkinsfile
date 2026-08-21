pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'echo "Deployment successful!"'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
