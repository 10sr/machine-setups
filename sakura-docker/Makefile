target := sakura

remote_tmp_dir := /tmp/docker-scp-$(shell echo $$$$)

scp:
	echo $(remote_tmp_dir)
	rsync -av --delete ./docker-compose/ "$(target):$(remote_tmp_dir)"
	ssh $(target) sudo -S -u docker cp -pfr $(remote_tmp_dir)/* /home/docker/docker-compose/ <sudo_password.secret
