# quick-scaffold

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![GitHub](https://img.shields.io/github/stars/yksanjo/quick-scaffold?style=social)

A powerful CLI tool to quickly scaffold new projects with common configurations. Save hours of boilerplate setup and start coding faster.

## Features

- 🚀 Multiple project templates (React, Python CLI, FastAPI, Next.js, Node.js API)
- 📝 Interactive prompts to customize your project
- 🔧 Auto-generates README, .gitignore, package.json/requirements.txt
- 🐳 Optional Docker setup
- ✅ Testing framework integration
- 🎨 Linting configuration included

## Installation

```bash
pip install -e .
```

Or install globally:
```bash
pip install .
```

## Usage

### Basic Usage

```bash
quick-scaffold
# or
qs
```

This will start an interactive prompt where you can:
1. Select a project template
2. Enter project name
3. Choose optional features (Docker, testing, linting)

### Quick Start

```bash
qs my-new-project
```

### Available Templates

- **react** - React application with Vite
- **python-cli** - Python CLI tool with Click
- **fastapi** - FastAPI web application
- **nextjs** - Next.js application
- **node-api** - Node.js Express API

## Examples

### Create a React project

```bash
qs my-react-app --template react
```

### Create a Python CLI tool

```bash
qs my-cli-tool --template python-cli
```

### Create a FastAPI project with Docker

```bash
qs my-api --template fastapi --docker
```

## Project Structure

After scaffolding, you'll get:

```
my-project/
├── README.md
├── .gitignore
├── requirements.txt  # or package.json
├── src/              # or app/
│   └── main.py       # or index.js
├── tests/
└── Dockerfile        # if --docker flag used
```

## License

MIT License - see LICENSE file for details

## Contributing

Contributions welcome! Please open an issue or submit a pull request.


