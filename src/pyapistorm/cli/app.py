import asyncio

import structlog

from pyapistorm.cli.cli_args import CLIArgs


class CLIApp:
    logger = structlog.get_logger()

    def __init__(self):
        self.args = None

    def parse_args(self):
        parser = CLIArgs.build()
        self.args = parser.parse_args()

    async def run(self):
        if self.args.config:
            self.logger.info("Using configuration file", config_file=self.args.config)
        else:
            self.logger.warning("No configuration file provided.")

    def main(self) -> None:
        self.logger.info("Starting PyAPIStorm CLI")
        self.parse_args()
        # try:
        raise SystemExit(asyncio.run(self.run()))
        # except Exception as e:
        #    self.logger.error("An error occurred", error=e)
        #    raise SystemExit(1)


# if __name__ == "__main__":
CLIApp().main()
