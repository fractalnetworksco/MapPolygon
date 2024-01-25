
up:
	docker compose up -d --force-recreate

dev:
	docker compose up -d --build --force-recreate

down:
	docker compose down -v
