pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }
    }
}
