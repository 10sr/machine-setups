String repo = System.getenv()["P_TXT_REPOSITORY_URL"]

job("mail_p_txt") {
    scm {
        git repo
    }
    triggers {
        scm 'H/5 * * * *'
    }
    steps {
        shell 'cat p.txt'
    }
}
