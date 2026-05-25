"""Gemini API configuration file.

Only paste your Gemini API key below.

Important:
- Do not commit real secrets to source control if this repository is shared.
- Replace only the API key placeholder with your real key.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class APIConfig:
    api_key: str = ""
    base_url: str = "https://api.gemini.example.com/v1"
    model_name: str = "gemini-1"
    timeout: int = 30
    additional_headers: dict[str, str] = None

    def __post_init__(self) -> None:
        if self.additional_headers is None:
            self.additional_headers = {}

    def is_valid(self) -> bool:
        return bool(self.api_key and self.base_url and self.model_name and not self.api_key.startswith("<"))


# Fill in your API configuration here.
# Only replace api_key with your real Gemini API key.
API_CONFIG = APIConfig(
    api_key="",
)
