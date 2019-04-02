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
            recipientList('8.slashes@gmail.com')
            defaultSubject('$JOB_NAME')
            // defaultContent('Something broken')
            contentType('text/plain')
            triggers {
                always()
            }
        }
    }}
