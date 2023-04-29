pipeline {
    agent any
    environment {
        IP_DA_DROPLET = '159.89.238.236'
        SSH_PRIVATE_KEY= credentials('ssh-private-key-ocean')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/test-jenkins']], 
                doGenerateSubmoduleConfigurations: false, 
                extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Caiocof/example-ci-ec2.git']]])
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-key-ocean', keyFileVariable: 'SSH_PRIVATE_KEY')]) {
                    sh 'rsync -r --delete --exclude=".git" -e "ssh -i $SSH_PRIVATE_KEY" . root@$IP_DA_DROPLET:/root/app'
                    sh "ssh -i $SSH_PRIVATE_KEY root@$IP_DA_DROPLET 'cd /root/app && docker-compose up -d --build'"
                }
                
            }
        }
    }
}
