from future import annotations

import logging
from dataclasses import dataclass

LOGGER = logging.getLogger(name)

@dataclass(frozen=True)
class Config:
  """Immutable application configuration."""

name: str = "my-project"
debug: bool = False

def configure_logging(config: Config) -> None:
  """Configure application logging based on the given configuration."""
  logging.basicConfig(
  level=logging.DEBUG if config.debug else logging.INFO,
  format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
  )

def run(config: Config) -> int:
  """Execute the core application logic and return an exit code."""
  LOGGER.info("Starting %s", config.name)
  print(f"{config.name} is running successfully.")
  return 0

def main() -> int:
  """Application entry point."""
  config = Config()
  configure_logging(config)
  return run(config)

if name == "main":
  raise SystemExit(main())
  
