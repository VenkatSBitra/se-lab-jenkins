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
    
    
    post {
        always {
            echo 'Sending Email....'
            
            emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
                to: 'tadrlh3@gmail.com'
            
            echo 'Email Sent.'
        }
    }
}
