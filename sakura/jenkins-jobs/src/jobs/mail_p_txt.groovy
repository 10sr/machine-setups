String repo = P_TXT_REPOSITORY_URL

job("mail_p_txt") {
    scm {
        git repo
    }
    triggers {
        scm 'H H * * *'
    }
    steps {
        shell 'cat p.txt'
    }
    publishers {
        extendedEmail {
            // TODO: Set global sender address
            recipientList('8.slashes@gmail.com')
            // TODO: Fix encoding
            defaultContent('''$DEFAULT_CONTENT

$BUILD_LOG''')
            contentType('text/plain')
            triggers {
                always {
                    sendTo {
                        recipientList()
                    }
                }
            }
        }
    }}
