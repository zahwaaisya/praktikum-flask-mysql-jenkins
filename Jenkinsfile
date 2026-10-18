
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Mengambil source code dari GitHub'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Membangun Docker image Flask'
                bat 'docker build -t praktikum-flask-mysql:latest .'
            }
        }

        stage('Test Docker Image') {
            steps {
                echo 'Memeriksa image yang berhasil dibuat'
                bat 'docker image inspect praktikum-flask-mysql:latest'
            }
        }

        stage('Test Database Stack') {
            steps {
                echo 'Menjalankan aplikasi Flask dan MySQL'
                bat 'docker compose up -d --build'
                bat 'docker compose ps'
            }
        }
    }

    post {
        always {
            echo 'Pipeline selesai. Periksa hasil setiap stage.'
        }
    }
}
