#!/bin/sh
set -eux

# echo 'config.force_ssl = true' \
    #      >>./config/environments/production.rb
patch -p1 </secure_cookie.patch

# ?
# For error:
# 0|instiki0 | instiki0 | /usr/local/lib/ruby/site_ruby/2.6.0/bundler/source/git.rb:221:in `rescue in load_spec_files': https://github.com/distler/maruku.git (at nokogiri@d56b03f) is not yet checked out. Run `bundle install` first. (Bundler::GitError)
# https://stackoverflow.com/questions/6648870/is-not-checked-out-bundle-install-does-not-fix-help
bundle install --deployment

exec "$@"
