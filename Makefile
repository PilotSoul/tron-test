.DEFAULT_GOAL := help
include .env

DOCKER_COMP    = docker compose -f docker-compose.yml
EXEC 		   = $(DOCKER_COMP) exec python
UV             = $(EXEC) uv
DEFAULT_IMAGES = tron-python


# ---------- Docker Compose ----------
build:
	@$(DOCKER_COMP) build --pull --no-cache

up:
	@$(DOCKER_COMP) up --detach --wait

up-debug:
	@$(DOCKER_COMP) up

down:
	@$(DOCKER_COMP) down --remove-orphans

full-restart: down up

clean:
	@$(DOCKER_COMP) down
	@docker rmi $(DEFAULT_IMAGES) || exit 0;

full-clean:
	@$(DOCKER_COMP) down --volumes
	@docker rmi $(DEFAULT_IMAGES) || exit 0;

rebuild: clean build

update: rebuild up

# ---------- Docker containers ----------


# ---------- Database management ----------
makemigrations:
	@$(EXEC) alembic revision --autogenerate -m "$(name)"

migrate:
	@$(EXEC) alembic upgrade head
# ---------- Database management ----------


# ---------- Linters ----------
linters:
	@echo "-------- running black --------"
	@$(EXEC) black .
	@echo "-------- running isort --------"
	@$(EXEC) isort .

black:
	@$(EXEC) black .
isort:
	@$(EXEC) isort .
# ---------- Linters ----------


# ---------- Tests ----------
test:
	@echo "Setting MODE=TEST and running pytest..."
	MODE=TEST PYTHONPATH=./app pytest -v
# ---------- Tests ----------