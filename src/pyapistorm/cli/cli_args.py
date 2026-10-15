import argparse
import pathlib as Paths

import structlog


class CLIArgs:
    logger = structlog.get_logger()

    def __init__(self, config: Paths.Path | None):
        self.config = config

    def parse(self):
        # Implement argument parsing logic here
        pass

    @classmethod
    def build(cls) -> argparse.ArgumentParser:

        parser = argparse.ArgumentParser(description="PyAPIStorm CLI")
        # Add your CLI arguments here
        parser.add_argument(
            "--config", type=Paths.Path, help="Path to configuration file"
        )
        cls.logger.debug("CLI parser built", parser=parser)
        return parser
