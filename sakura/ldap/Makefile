target_host := sakura
dir := ldap_files

scp:
	ssh "$(target_host)" mkdir -p $(dir)
	rsync -av ./ "$(target_host)":"$(dir)/"
