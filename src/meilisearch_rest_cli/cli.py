import os
from pathlib import Path
from openapi_cli_gen import build_cli

# Base URL: override via MEILISEARCH_REST_CLI_BASE_URL env var, fall back to spec default
_base_url = os.environ.get("MEILISEARCH_REST_CLI_BASE_URL") or "http://localhost:7700"

app = build_cli(
    spec=Path(__file__).parent / "spec.yaml",
    name="meilisearch-rest-cli",
    base_url=_base_url,
)


def main():
    app()


if __name__ == "__main__":
    main()
