"""Tests for CLI functionality."""

import pytest
from pathlib import Path
import tempfile
import os
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.cli import get_templates, create_project_structure


def test_get_templates():
    """Test that templates are returned correctly."""
    templates = get_templates()
    assert "react" in templates
    assert "python-cli" in templates
    assert "fastapi" in templates


def test_create_python_cli_project():
    """Test creating a Python CLI project."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        project_name = "test-cli"
        create_project_structure(project_name, "python-cli", docker=False, testing=True, linting=False)
        
        project_path = Path(tmpdir) / project_name
        assert project_path.exists()
        assert (project_path / "src" / "main.py").exists()
        assert (project_path / "requirements.txt").exists()
        assert (project_path / "README.md").exists()
        assert (project_path / ".gitignore").exists()
        assert (project_path / "tests" / "test_main.py").exists()


def test_create_fastapi_project():
    """Test creating a FastAPI project."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        project_name = "test-api"
        create_project_structure(project_name, "fastapi", docker=True, testing=True, linting=False)
        
        project_path = Path(tmpdir) / project_name
        assert project_path.exists()
        assert (project_path / "src" / "main.py").exists()
        assert (project_path / "Dockerfile").exists()
        assert (project_path / "docker-compose.yml").exists()

