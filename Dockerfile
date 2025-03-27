FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_PYTHON_DOWNLOADS=0 UV_LINK_MODE=copy
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-dev

FROM python:3.12-slim-bookworm AS moderation
WORKDIR /app
COPY --from=builder --chown=app:app /app /app
ENV PATH="/app/.venv/bin:$PATH"
COPY app app
COPY models models
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
