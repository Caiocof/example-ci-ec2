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
                sh "ssh -i $SSH_PRIVATE_KEY root@$EC2_INSTANCE_ID 'cd /root/app && docker-compose up -d"
            }
        }
    }
}
