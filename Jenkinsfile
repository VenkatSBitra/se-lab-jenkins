pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    extensions: [], 
                    userRemoteConfigs: [[url: 'https://github.com/VenkatSBitra/se-lab-jenkins.git']]
                ])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/VenkatSBitra/se-lab-jenkins.git'
                sh 'python3 prog.py'
            }
        }
        stage('Test') {
            steps {
                git branch: 'main', url: 'https://github.com/VenkatSBitra/se-lab-jenkins.git'
                sh 'python3 test.py'
            }
        }
    }
}
