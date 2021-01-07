occ := docker-compose exec --user www-data app php occ

db-add-missing-indices:
	$(occ) "db:add-missing-indices"

db-convert-filecache-bigint:
	$(occ) "db:convert-filecache-bigint"
