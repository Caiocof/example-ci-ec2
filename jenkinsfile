pipeline {
    agent any
    environment {
        APP_NAME = 'bank-app'
        INSTANCE_HOST= '159.89.238.236'
        SSH_PRIVATE_KEY = credentials('ssh-private-key-ocean')
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/Caiocof/example-ci-ec2.git'
            }
        }
        stage('Setup virtual environment') {
            steps {
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Create .env file') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-key-ocean', keyFileVariable: 'SSH_PRIVATE_KEY')]) {
                    sh "echo 'POSTGRES_USER=root' > .env"
                    sh "echo 'POSTGRES_PASSWORD=root' >> .env"
                    sh "echo 'POSTGRES_HOST=bank_api_database' >> .env"
                    sh "echo 'POSTGRES_DB=bank_api' >> .env"
                    sh "echo 'POSTGRES_PORT=5432' >> .env"
                    sh "echo 'DB_DRIVER=postgresql+psycopg2' >> .env"
                    sh 'rsync -r --delete --exclude=".git" -e "ssh -i $SSH_PRIVATE_KEY" . root@$INSTANCE_HOST:/root/$APP_NAME'
                    sh "ssh -i $SSH_PRIVATE_KEY root@$INSTANCE_HOST 'cd /root/$APP_NAME && docker-compose pull && docker-compose up -d'"
                }
            }
        }
        stage('Deploy to Droplet instance') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-key-ocean', keyFileVariable: 'SSH_PRIVATE_KEY')]) {
                    sh 'rsync -r --delete --exclude=".git" -e "ssh -i $SSH_PRIVATE_KEY" . root@$INSTANCE_HOST:/root/$APP_NAME'
                    sh "ssh -i $SSH_PRIVATE_KEY root@$INSTANCE_HOST 'cd /root/$APP_NAME && docker-compose up -d --build'"
                    
                }
            }
        }
    }
}
