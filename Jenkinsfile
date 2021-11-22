pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/chandrahassai77/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x ts.py"
                sh "./ts.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}