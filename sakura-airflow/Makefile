target := sakura

remote_tmp_dir := /tmp/airflow-scp-$(shell echo $$$$)

scp:
	echo $(remote_tmp_dir)
	rsync -av ./dags/ "$(target):$(remote_tmp_dir)"
	ssh $(target) sudo -S -u docker cp -pfr $(remote_tmp_dir)/* /home/docker/docker-compose/airflow0/dags/ <sudo_password.secret


restart:
	ssh $(target) sudo -S -i -u docker /home/docker/pm2 restart airflow0 <sudo_password.secret
