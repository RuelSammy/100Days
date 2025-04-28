import argparse

def main():
    parser = argparse.ArgumentParser(
        description="A simple greeting tool."
    )

    parser.add_argument(
        "name", 
        help="Name of the person to greet"
    )

    parser.add_argument(
        "-t", "--times",
        type=int,
        default=1,
        help="Number of times to print the greeting"
    )

    parser.add_argument(
        "-u", "--uppercase",
        action="store_true",
        help="Print the greeting in uppercase"
    )

    args = parser.parse_args()

    greeting = f"Hello, {args.name}!"

    if args.uppercase:
        greeting = greeting.upper()

    for _ in range(args.times):
        print(greeting)

if __name__ == "__main__":
    main()
