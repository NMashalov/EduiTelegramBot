PROJECT_DIR=chat
PORT=5050

.PHONY: install
install:
	@poetry install

.PHONY: install-cloudfare-tunnel
install-cloudfare-tunnel:
	@wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
	@sudo dpkg -i cloudflared-linux-amd64.deb

install-docker:
	source docker-install.sh
	
format:
	ruff format $(PROJECT_DIR)
	@isort $(PROJECT_DIR)

local-start:
	cloudflared tunnel --url http://127.0.0.1:$(PORT)

run:
	@sudo docker compose up