import click
from pathlib import Path
from .core import create_project, build_project, run_project

@click.group()
def cli():
    """AutoA2A - Automated A2A Multi-Agent System Builder"""
    pass

@cli.command()
@click.argument("project_name")
def create(project_name):
    """Create a new A2A project"""
    project_path = Path.cwd() / project_name
    create_project(project_path)
    click.echo(f"Project '{project_name}' created successfully at {project_path}")

@cli.command()
def build():
    """Build the A2A multi-agent system"""
    project_path = Path.cwd()
    build_project(project_path)
    click.echo("A2A system built successfully")

@cli.command()
def run():
    """Run the A2A system"""
    project_path = Path.cwd()
    run_project(project_path)
    click.echo("A2A system running")

if __name__ == "__main__":
    cli()