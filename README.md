# pytest_practice

Small sample project demonstrating pytest usage.

## Setup (macOS / Linux)

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Activate it:

```bash
source .venv/bin/activate
```

3. Install development requirements:

```bash
python -m pip install -U pip
python -m pip install -r requirements-dev.txt
```

## Run tests

```bash
python -m pytest -q
```

## VS Code

- Select the workspace interpreter: `Cmd+Shift+P` → **Python: Select Interpreter** → choose `.venv/bin/python`.
- Tests are configured in `.vscode/settings.json` to use pytest and the `tests` folder.

---

If you'd like, I can also add a GitHub Actions workflow to run tests on push/pull requests.