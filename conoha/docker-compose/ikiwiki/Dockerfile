FROM perl

RUN git clone git://git.ikiwiki.info/ /ikiwiki
WORKDIR /ikiwiki

RUN PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("Text::Markdown::Discount")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("URI")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("HTML::Parser")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("CGI")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("CGI::Session")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("HTML::Template")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("YAML::XS")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("HTML::Scrubber")'

RUN PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("CGI::FormBuilder")'

RUN apt-get update && apt-get install -y gettext
RUN perl Makefile.PL && make && make install
COPY setup.pl /setup.pl
RUN ikiwiki --setup /setup.pl

RUN apt-get install -y spawn-fcgi fcgiwrap
RUN mkdir -p /tmp/ikiwiki

#RUN mkdir -p /var/ikiwiki_src /var/ikiwiki

CMD ["/usr/bin/spawn-fcgi", "-s", "/tmp/ikiwiki/fcgi.socket", "-M", "777", "-n", "--", "/usr/sbin/fcgiwrap"]
