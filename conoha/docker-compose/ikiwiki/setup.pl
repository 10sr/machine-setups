require IkiWiki::Setup::Automator;

our $wikiname = "10sr ikiwiki test";
our $wikiname_short=IkiWiki::Setup::Automator::sanitize_wikiname($wikiname);
our $rcs = "git";
our $admin = "10sr";
our $domain = "3ends.info";

IkiWiki::Setup::Automator->import(
  wikiname => $wikiname,
  adminuser => [$admin],
  rcs => $rcs,
  srcdir => "/var/ikiwiki_src",
  destdir => "/var/ikiwiki",
  repository => "$ENV{HOME}/$wikiname_short.".($rcs eq "monotone" ? "mtn" : $rcs),
  dumpsetup => "$ENV{HOME}/$wikiname_short.setup",
  url => "http://$domain/ikiwiki",
  cgiurl => "http://$domain/ikiwiki/ikiwiki.cgi",
  cgi_wrapper => "/var/ikiwiki/ikiwiki.cgi",
  adminemail => "$ENV{USER}\@$domain",
  add_plugins => [qw{goodstuff websetup}],
  disable_plugins => [qw{}],
  libdir => "$ENV{HOME}/.ikiwiki",
  rss => 1,
  atom => 1,
  syslog => 0
    )
