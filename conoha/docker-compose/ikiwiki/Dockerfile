FROM perl

RUN git clone git://git.ikiwiki.info/ /ikiwiki
WORKDIR /ikiwiki

RUN PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("Text::Markdown::Discount")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("URI")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("HTML::Parser")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("CGI")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("HTML::Template")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("YAML::XS")' && \
    PERL5LIB=`pwd` PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'CPAN::Shell->install("HTML::Scrubber")'

RUN apt-get update && apt-get install -y gettext
RUN perl Makefile.PL && make && make install
COPY setup.pl /setup.pl
RUN ikiwiki --setup /setup.pl

