target := jenkins01

jobs_xmls := $(wildcard jobs/*.xml)
jobs := $(jobs_xmls:jobs/%.xml=%)

remote_dir := jenkins_jobs

ssh :=  gcloud --project "praxis-practice-289116" beta compute ssh --zone "asia-northeast1-b" $(target) --
scp := gcloud  --project "praxis-practice-289116" beta compute scp --zone "asia-northeast1-b"
jenkins := sudo -u admin ssh admin@localhost -p 2244

.PHONY: scp jobs

scp:
	$(ssh) mkdir -p $(remote_dir)/
	$(scp) --recurse "$(CURDIR)"/* "$(target):$(remote_dir)/"

jobs: $(jobs)

# $(ssh) $(jenkins) create-job --help

$(jobs): scp
	# # Jenkis CLI does not provide `create-or-update-job' command,
	# # so always try to create the job first
	# $(ssh) "cat $(remote_dir)/jobs/$@.xml | $(jenkins) create-job $@ || true" 
	# $(ssh) "cat $(remote_dir)/jobs/$@.xml | $(jenkins) update-job $@"
	$(ssh) sudo install -D $(remote_dir)/jobs/$@.xml /var/lib/jenkins/jobs/$@/config.xml
	# install's -o and -g options do not change owner of parent directory
	$(ssh) sudo chown -R "jenkins:jenkins" /var/lib/jenkins/jobs/$@

help:
	$(ssh) $(jenkins) help

restart:
	$(ssh) $(jenkins) safe-restart

# TODO: Create job to fetch all job XMLs
get-job:
	$(ssh) $(jenkins) get-job env >env.xml
