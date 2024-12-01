FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app

RUN uv sync --frozen

CMD ["uv", "run", "prod"]

EXPOSE 8080