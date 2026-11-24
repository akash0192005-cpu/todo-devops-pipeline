pipeline {
    agent any
    triggers {
        pollSCM('H/2 * * * *')
    }
    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install') {
            steps { sh 'python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt' }
        }
        stage('Test') {
            steps { sh '. .venv/bin/activate && pytest -q --junitxml=junit.xml' }
        }
        stage('Package') {
            steps {
                sh 'mkdir -p dist && tar --exclude=.git --exclude=.venv -czf dist/todo-api-${BUILD_NUMBER}.tar.gz app requirements.txt'
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }
    post {
        always { junit allowEmptyResults: true, testResults: 'junit.xml' }
    }
}
