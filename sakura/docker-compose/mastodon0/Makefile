DC_RUN := docker-compose --verbose run --rm

build-image:
	docker build  -t local/st.3ends.info \
		"https://github.com/10sr/mastodon.git#st.3ends.info"

migrate:
	${DC_RUN} web rails db:migrate

precompile:
	${DC_RUN} web rails assets:precompile

migrate-photo-preview-cards:
	${DC_RUN} web rails mastodon:maintenance:migrate_photo_preview_cards
