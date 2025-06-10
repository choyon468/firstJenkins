// pipeline {
//     agent any
//     stages {
//         stage('build') {
//             steps {
//                 echo 'Build application'
//                 echo "${env.PATH}"
//             }
//         }
//         stage('test') {
//             steps {
//                 echo 'Test application'
//                 bat """
//                     python test.py
//                 """
//             }
//         }
//         stage('deploy') {
//             steps {
//                 echo 'Deploy application'
//                  bat """
//                     xcopy . F:\\PYTHON\\DEMO\\TEMP_SERVER /E /Y /I
//                 """
//             }
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build Application'
            }
        }
         stage('Test') {
            steps {
                echo 'Test Application'
                bat"""
                    "C:\\Users\\choyo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" "C:\\Assignment Python\\rest_api\\DEMO\\CICD\\test.py"
                """
            }
        }
         stage('Deploy') {
            steps {
                echo 'Deploy Application'
                bat"""
                    copy "C:\\Assignment Python\\rest_api\\DEMO\\CICD\\test.py" "C:\\Assignment Python\\rest_api\\DEMO\\TEMP_SERVER\\"
                """
            }
        }
    }
}
