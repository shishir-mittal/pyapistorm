import asyncio


def build_cli_parser():
    """
    Build the command-line interface parser.
    """
    import argparse

    parser = argparse.ArgumentParser(description="PyAPIStorm CLI")
    # Add your CLI arguments here
    parser.add_argument("--config", type=str, help="Path to configuration file")
    return parser


async def run(args):
    """
    Run the main logic of the CLI application.
    """
    # Implement your async logic here
    if args.config:
        print(f"Using configuration file: {args.config}")
    else:
        print("No configuration file provided.")


def main() -> None:
    """
    Entry point for the CLI application.
    """
    print("Welcome to PyAPIStorm CLI!")
    # Add your CLI logic here
    args = build_cli_parser().parse_args()
    try:
        raise SystemExit(asyncio.run(run(args)))
    except Exception as e:
        raise SystemExit(f"Configuration error: {e}") from e


if __name__ == "__main__":
    main()
