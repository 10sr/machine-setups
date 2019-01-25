String basePath = 'dowwner'
String repo = '10sr/dowwner'

folder(basePath) {
    description 'Dowwner job folder.'
}

job("$basePath/dowwner-check") {
    scm {
        github repo
    }
    triggers {
        scm 'H/15 * * * *'
    }
    steps {
        shell 'make installdeps check'
    }
}

job("$basePath/dowwner-hoe") {
    parameters {
        stringParam 'host'
    }
    steps {
        shell 'pwd && echo $host'
    }
}
