pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Build application'
                echo "${env.PATH}"
            }
        }
        stage('test') {
            steps {
                echo 'Test application'
                bat """
                    python test.py
                """
            }
        }
        stage('deploy') {
            steps {
                echo 'Deploy application'
                 bat """
                    xcopy . F:\\PYTHON\\DEMO\\TEMP_SERVER /E /Y /I
                """
            }
        }
    }
}