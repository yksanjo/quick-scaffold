#!/usr/bin/env python3
"""CLI entry point for quick-scaffold."""

import os
import sys
from pathlib import Path
import click
from jinja2 import Template

TEMPLATES_DIR = Path(__file__).parent / "templates"


def get_templates():
    """Get available templates."""
    return {
        "react": {
            "name": "React App",
            "description": "React application with Vite",
        },
        "python-cli": {
            "name": "Python CLI",
            "description": "Python CLI tool with Click",
        },
        "fastapi": {
            "name": "FastAPI",
            "description": "FastAPI web application",
        },
        "nextjs": {
            "name": "Next.js",
            "description": "Next.js application",
        },
        "node-api": {
            "name": "Node.js API",
            "description": "Node.js Express API",
        },
    }


def create_project_structure(project_name, template, docker=False, testing=False, linting=False):
    """Create project structure based on template."""
    project_path = Path(project_name)
    
    if project_path.exists():
        click.echo(f"Error: Directory '{project_name}' already exists!", err=True)
        sys.exit(1)
    
    project_path.mkdir(parents=True)
    
    # Create basic structure
    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "tests").mkdir(exist_ok=True)
    
    # Generate files based on template
    if template == "react":
        create_react_project(project_path, docker, testing, linting)
    elif template == "python-cli":
        create_python_cli_project(project_path, docker, testing, linting)
    elif template == "fastapi":
        create_fastapi_project(project_path, docker, testing, linting)
    elif template == "nextjs":
        create_nextjs_project(project_path, docker, testing, linting)
    elif template == "node-api":
        create_node_api_project(project_path, docker, testing, linting)
    
    click.echo(f"\n✅ Project '{project_name}' created successfully!")
    click.echo(f"\n📁 Location: {project_path.absolute()}")
    click.echo(f"\n🚀 Next steps:")
    click.echo(f"   cd {project_name}")
    if template in ["react", "nextjs", "node-api"]:
        click.echo(f"   npm install")
        click.echo(f"   npm run dev")
    else:
        click.echo(f"   pip install -r requirements.txt")
        click.echo(f"   python -m src.main")


def create_react_project(path, docker, testing, linting):
    """Create React project structure."""
    # package.json
    package_json = """{
  "name": "{{ project_name }}",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.0.0",
    "vite": "^4.4.0"
  }
}
"""
    (path / "package.json").write_text(Template(package_json).render(project_name=path.name))
    
    # vite.config.js
    vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
"""
    (path / "vite.config.js").write_text(vite_config)
    
    # index.html
    index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ project_name }}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""
    (path / "index.html").write_text(Template(index_html).render(project_name=path.name))
    
    # src/main.jsx
    main_jsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""
    (path / "src" / "main.jsx").write_text(main_jsx)
    
    # src/App.jsx
    app_jsx = """import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <h1>{{ project_name }}</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </div>
  )
}

export default App
"""
    (path / "src" / "App.jsx").write_text(Template(app_jsx).render(project_name=path.name))
    
    # src/index.css
    (path / "src" / "index.css").write_text("""* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
}
""")
    
    # src/App.css
    (path / "src" / "App.css").write_text(""".App {
  text-align: center;
  padding: 2rem;
}
""")
    
    # .gitignore
    gitignore = """# Dependencies
node_modules/
dist/

# Build
build/
.vite/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
"""
    (path / ".gitignore").write_text(gitignore)
    
    # README.md
    readme = """# {{ project_name }}

A React application built with Vite.

## Getting Started

\`\`\`bash
npm install
npm run dev
\`\`\`

## Build

\`\`\`bash
npm run build
\`\`\`
"""
    (path / "README.md").write_text(Template(readme).render(project_name=path.name))


def create_python_cli_project(path, docker, testing, linting):
    """Create Python CLI project structure."""
    # requirements.txt
    reqs = ["click>=8.1.0"]
    if testing:
        reqs.append("pytest>=7.0.0")
    if linting:
        reqs.extend(["ruff>=0.1.0", "black>=23.0.0"])
    (path / "requirements.txt").write_text("\n".join(reqs) + "\n")
    
    # src/main.py
    main_py = """#!/usr/bin/env python3
\"\"\"{{ project_name }} - CLI tool.\"\"\"

import click


@click.command()
@click.option('--name', default='World', help='Name to greet')
def main(name):
    \"\"\"Simple CLI tool.\"\"\"
    click.echo(f'Hello, {name}!')


if __name__ == '__main__':
    main()
"""
    (path / "src" / "main.py").write_text(Template(main_py).render(project_name=path.name))
    
    # src/__init__.py
    (path / "src" / "__init__.py").write_text(f'"""{{ project_name }} package."""\n')
    
    # tests/test_main.py
    if testing:
        test_main = """import pytest
from src.main import main


def test_main():
    # Add your tests here
    assert True
"""
        (path / "tests" / "test_main.py").write_text(test_main)
        (path / "tests" / "__init__.py").write_text("")
    
    # .gitignore
    gitignore = """# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
dist/
*.egg-info/
.venv/
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
"""
    (path / ".gitignore").write_text(gitignore)
    
    # README.md
    readme = """# {{ project_name }}

A Python CLI tool built with Click.

## Installation

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

\`\`\`bash
python -m src.main --name "Your Name"
\`\`\`
"""
    (path / "README.md").write_text(Template(readme).render(project_name=path.name))


def create_fastapi_project(path, docker, testing, linting):
    """Create FastAPI project structure."""
    # requirements.txt
    reqs = ["fastapi>=0.100.0", "uvicorn[standard]>=0.23.0"]
    if testing:
        reqs.extend(["pytest>=7.0.0", "httpx>=0.24.0"])
    if linting:
        reqs.extend(["ruff>=0.1.0", "black>=23.0.0"])
    (path / "requirements.txt").write_text("\n".join(reqs) + "\n")
    
    # src/main.py
    main_py = """from fastapi import FastAPI

app = FastAPI(title="{{ project_name }}")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
"""
    (path / "src" / "main.py").write_text(Template(main_py).render(project_name=path.name))
    
    # src/__init__.py
    (path / "src" / "__init__.py").write_text("")
    
    # tests/test_main.py
    if testing:
        test_main = """from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
"""
        (path / "tests" / "test_main.py").write_text(test_main)
        (path / "tests" / "__init__.py").write_text("")
    
    # .gitignore
    gitignore = """# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
dist/
*.egg-info/
.venv/
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
"""
    (path / ".gitignore").write_text(gitignore)
    
    # README.md
    readme = """# {{ project_name }}

A FastAPI web application.

## Installation

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

\`\`\`bash
uvicorn src.main:app --reload
\`\`\`

Visit http://localhost:8000/docs for API documentation.
"""
    (path / "README.md").write_text(Template(readme).render(project_name=path.name))
    
    if docker:
        # Dockerfile
        dockerfile = """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
        (path / "Dockerfile").write_text(dockerfile)
        
        # .dockerignore
        (path / ".dockerignore").write_text("""__pycache__
*.pyc
.venv
venv
.git
.gitignore
README.md
""")
    
    # docker-compose.yml
    if docker:
        docker_compose = """version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
"""
        (path / "docker-compose.yml").write_text(docker_compose)


def create_nextjs_project(path, docker, testing, linting):
    """Create Next.js project structure."""
    # package.json
    package_json = """{
  "name": "{{ project_name }}",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "next": "^13.5.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "typescript": "^5.0.0"
  }
}
"""
    (path / "package.json").write_text(Template(package_json).render(project_name=path.name))
    
    # next.config.js
    (path / "next.config.js").write_text("""/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig
""")
    
    # tsconfig.json
    (path / "tsconfig.json").write_text("""{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
""")
    
    # app/layout.tsx
    (path / "app").mkdir(exist_ok=True)
    layout_tsx = """export const metadata = {
  title: '{{ project_name }}',
  description: 'Generated by quick-scaffold',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
"""
    (path / "app" / "layout.tsx").write_text(Template(layout_tsx).render(project_name=path.name))
    
    # app/page.tsx
    page_tsx = """export default function Home() {
  return (
    <main>
      <h1>{{ project_name }}</h1>
      <p>Welcome to your Next.js app!</p>
    </main>
  )
}
"""
    (path / "app" / "page.tsx").write_text(Template(page_tsx).render(project_name=path.name))
    
    # app/globals.css
    (path / "app" / "globals.css").write_text("""* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
}
""")
    
    # .gitignore
    gitignore = """# Dependencies
node_modules/
.next/
out/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
"""
    (path / ".gitignore").write_text(gitignore)
    
    # README.md
    readme = """# {{ project_name }}

A Next.js application.

## Getting Started

\`\`\`bash
npm install
npm run dev
\`\`\`

Open [http://localhost:3000](http://localhost:3000) in your browser.
"""
    (path / "README.md").write_text(Template(readme).render(project_name=path.name))


def create_node_api_project(path, docker, testing, linting):
    """Create Node.js API project structure."""
    # package.json
    package_json = """{
  "name": "{{ project_name }}",
  "version": "0.1.0",
  "type": "module",
  "main": "src/index.js",
  "scripts": {
    "dev": "node --watch src/index.js",
    "start": "node src/index.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {}
}
"""
    (path / "package.json").write_text(Template(package_json).render(project_name=path.name))
    
    # src/index.js
    index_js = """import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Hello, World!' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
"""
    (path / "src" / "index.js").write_text(index_js)
    
    # .gitignore
    gitignore = """# Dependencies
node_modules/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
"""
    (path / ".gitignore").write_text(gitignore)
    
    # README.md
    readme = """# {{ project_name }}

A Node.js Express API.

## Installation

\`\`\`bash
npm install
\`\`\`

## Usage

\`\`\`bash
npm run dev
\`\`\`

Server will run on http://localhost:3000
"""
    (path / "README.md").write_text(Template(readme).render(project_name=path.name))


@click.command()
@click.argument('project_name', required=False)
@click.option('--template', '-t', type=click.Choice(['react', 'python-cli', 'fastapi', 'nextjs', 'node-api']), help='Project template')
@click.option('--docker', is_flag=True, help='Include Docker setup')
@click.option('--testing', is_flag=True, help='Include testing framework')
@click.option('--linting', is_flag=True, help='Include linting configuration')
def main(project_name, template, docker, testing, linting):
    """Quick Scaffold - Generate project templates quickly."""
    
    templates = get_templates()
    
    # Interactive mode if project_name not provided
    if not project_name:
        click.echo("🚀 Quick Scaffold - Project Template Generator\n")
        click.echo("Available templates:")
        for key, info in templates.items():
            click.echo(f"  {key:12} - {info['name']}: {info['description']}")
        click.echo()
        
        project_name = click.prompt("Project name", type=str)
        if not template:
            template = click.prompt(
                "Template",
                type=click.Choice(list(templates.keys())),
                default="python-cli"
            )
        if not docker:
            docker = click.confirm("Include Docker setup?", default=False)
        if not testing:
            testing = click.confirm("Include testing framework?", default=False)
        if not linting:
            linting = click.confirm("Include linting configuration?", default=False)
    
    # Default template if not specified
    if not template:
        template = "python-cli"
    
    create_project_structure(project_name, template, docker, testing, linting)


if __name__ == '__main__':
    main()


