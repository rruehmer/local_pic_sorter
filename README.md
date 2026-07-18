# local_pic_sorter

Local Pic Sorter is a privacy-first Python project for organizing photos stored on a local hard drive. The goal is to process image files directly on the machine, remove duplicates, sort them by capture date, and eventually group them by recognized people using local face recognition.

## What this project does

This project is designed to help users bring order to large photo collections without relying on cloud services. It will:

- scan a source folder for image files
- detect and handle duplicate files early
- read EXIF metadata to determine the original capture date
- sort photos into a clear folder structure such as year/month
- optionally use local face recognition to place photos into person-specific folders
- support a dry-run mode for safe testing before moving files

## Project goals

- keep everything local and private
- work well with common photo formats including JPG, JPEG, PNG, and HEIC
- provide a simple command-line interface for everyday use
- build the project in a structured, sprint-based way

## Planned development roadmap

The project is being developed in stages:

1. Sprint 1: project foundation and CLI setup
2. Sprint 2: preprocessing, duplicate handling, and EXIF-based sorting
3. Sprint 3: local face recognition integration
4. Sprint 4: robustness, logging, and edge-case handling

## Current status

The repository has been initialized with the base structure for the project, including a Python package layout and a starter documentation foundation. The next steps will focus on setting up the CLI and the core sorting logic.

## Repository structure

- src/shutter_sorter/: Python package for the sorter logic
- tests/: test suite for future validation
- docs/: documentation and notes

## Poetry setup

This project uses Poetry for dependency management and virtual environments.

### Install Poetry

To install Poetry, use the following command in your PowerShell:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

For further information, refer to https://python-poetry.org/docs/

### Initialize the project

From the repository root, run:

```bash
poetry install
```

### Activate the virtual environment

```PowerShell
Invoke-Expression (poetry env activate)
```
INFO: You might have to set the execution policy with the following command in order for the environment to activate:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Create a new dependency

If you want to add dependencies later, use:

```bash
poetry add <package-name>
```

## CLI Usage

The project includes a command-line interface for sorting photos. Once the environment is set up, you can use the `sort-photos` command.

### Basic Usage

```bash
local-pic-sorter sort-photos <source> <destination> [OPTIONS]
```

### Examples

**Sort photos in dry-run mode (preview without changes):**

```bash
local-pic-sorter sort-photos /path/to/photos /path/to/sorted --dry-run
```

**Actually sort photos (moves files):**

```bash
local-pic-sorter sort-photos /path/to/photos /path/to/sorted
```

### CLI Parameters

- `source` (required): Path to the folder containing photos to sort (must exist)
- `destination` (required): Path to the folder where sorted photos will be placed
- `--dry-run` (optional): Preview changes without modifying files (default: False)

### Why Dry-Run Mode is Essential

The `--dry-run` flag is crucial for safe photo organization:

1. **Protection against programming errors**: Catch typos or logic bugs before they affect your photos
2. **Trust in AI sorting decisions**: Preview how the AI classifier will organize photos before running live
3. **Preview folder structure**: See exactly how your folder hierarchy will look before committing

Always use `--dry-run` first to review the planned changes!

## Notes

This project is intended for personal use and local processing. It is not yet a finished product, but it is being built as a practical tool for organizing photo libraries safely and efficiently.
