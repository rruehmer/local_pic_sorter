"""
Main CLI interface for local_pic_sorter using Click.

This module defines the command-line interface for the photo sorting application.
"""

import logging
import sys
from pathlib import Path
import click

logging.basicConfig(level=logging.INFO)

@click.group()
def app():
    """A local-first photo sorting tool for organizing images on disk."""
    pass


@app.command()
@click.argument("source", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.argument("destination", type=click.Path(file_okay=False, dir_okay=True))
@click.option(
    "--dry-run",
    is_flag=True,
    default=True,
    help="Simulate the sorting process without actually moving files",
)
def sort_photos(source: str, destination: str, dry_run: bool):
    """
    Sort photos from source to destination folder based on EXIF date and optional face recognition.
    
    This command will:
    - Scan the source folder for image files (JPG, JPEG, PNG, HEIC)
    - Detect and remove duplicates
    - Extract EXIF metadata to determine capture dates
    - Organize photos into a structured folder hierarchy (Year/Month_Name/)
    
    Use --dry-run to preview changes without modifying your hard drive.
    """
    
    # Convert to Path objects and resolve to absolute paths
    source_path = Path(source).resolve()
    destination_path = Path(destination).resolve()
    
    # Validate source path exists
    if not source_path.is_dir():
        click.secho(
            f"❌ Error: Source path is not a folder: {source_path}",
            fg="red",
            bold=True,
        )
        sys.exit(1)
    
    if dry_run:
        click.secho(
            "🏜️  DRY RUN MODE ACTIVE",
            fg="yellow",
            bold=True,
        )
        click.echo()
        click.echo(
            "In this mode, the script will simulate all operations and show you "
            "what would happen WITHOUT actually moving or modifying any files on your hard drive."
        )
        click.echo()
        click.secho(
            "Reasons why dry-run is essential:",
            fg="cyan",
            bold=True,
        )
        click.echo("  1. Protection against programming errors (bugs)")
        click.echo("  2. Trust in AI sorting decisions (once implemented)")
        click.echo("  3. Preview folder structure before committing changes")
        click.echo()
    
    click.echo(f"Source folder: {source_path}")
    click.echo(f"Destination folder: {destination_path}")
    click.echo(f"Dry-run mode: {'ON' if dry_run else 'OFF'}")
    click.echo()
    
    if dry_run:
        click.secho(
            "This is a DRY RUN. No files will be moved.",
            fg="yellow",
        )
    else:
        click.secho(
            "LIVE MODE: Files will be processed and moved.",
            fg="red",
        )
    
    click.echo()
    click.echo("✨ Photo sorting CLI skeleton ready for implementation.")
    click.echo("The actual sorting logic will be added in the next sprint.")


if __name__ == "__main__":
    app()
