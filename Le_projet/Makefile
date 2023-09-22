CMD            := $(shell command -v docker-compose || echo "docker compose")

all: down up log

dev: down
	${CMD} up --build -d

log:
	${CMD} logs -f db server front

front:
	${CMD} logs -f front

up:
	${CMD} up --build -d

down:
	${CMD} kill && ${CMD} down

purge:
	docker-compose kill
	docker-compose down -v
	docker builder prune --all
	docker system prune -a -f --volumes