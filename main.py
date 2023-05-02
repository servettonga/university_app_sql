#!python3
# University Management System

from src.app import App


def main() -> None:
    app = App()
    while True:
        app.greet()

if __name__ == '__main__':
    main()
