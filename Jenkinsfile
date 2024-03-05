properties([[$class: 'JobLocalConfiguration', changeReasonComment: ''], pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone") {
        git branch: 'master', url: 'https://github.com/avrahamm/devops2024.git'
    }
    stage("show files"){
        sh "ls -l"
    }
}
