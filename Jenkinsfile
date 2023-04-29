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
        stage('Create .env file') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-key-ocean', keyFileVariable: 'SSH_PRIVATE_KEY')]) {
                    sh "echo 'POSTGRES_USER=root' > .env"
                    sh "echo 'POSTGRES_PASSWORD=root' >> .env"
                    sh "echo 'POSTGRES_HOST=127.0.0.1' >> .env"
                    sh "echo 'POSTGRES_DB=bank_api' >> .env"
                    sh "echo 'POSTGRES_PORT=5432' >> .env"
                    sh "echo 'DB_DRIVER=postgresql+psycopg2' >> .env"
                    sh 'rsync -r --delete --exclude=".git" -e "ssh -i $SSH_PRIVATE_KEY" . root@$IP_DA_DROPLET:/root/app'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'ssh-keyscan -t rsa ${IP_DA_DROPLET} >> ~/.ssh/known_hosts'
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-key-ocean', keyFileVariable: 'SSH_PRIVATE_KEY')]) {
                    sh 'rsync -r --delete --exclude=".git" -e "ssh -i $SSH_PRIVATE_KEY" . root@$IP_DA_DROPLET:/root/app'
                    sh """
                        ssh -i "${SSH_PRIVATE_KEY}" -o StrictHostKeyChecking=no root@${IP_DA_DROPLET} "cd /root/app && docker-compose up -d --build"
                        """
                }
                
            }
        }
    }
}
