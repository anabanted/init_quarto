#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pathlib
import os
import shutil

# Read the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n","--project_name", help="Name of the new project")
parser.add_argument("-d","--directory", help="Path to the new project")
parser.add_argument("-e","--existing_dir", help="Use existing directory as a project directory", action="store_true")
parser.add_argument("-t","--template", help="Path to the template")

args = parser.parse_args()

# Create the project directory

# Define the porject name
if args.directory is not None:
    if pathlib.Path(args.directory).is_dir():
        pass
    else:
        print("No such directory")
        exit(1)

if args.existing_dir:
    if args.directory is not None:
        project_name = pathlib.Path(args.directory).name
    else:
        print("--directory must be specified when using --existing_dir")
        exit(1)

if args.project_name:
    project_name=args.project_name
else:
    if args.existing_dir:
        project_name = pathlib.Path(args.directory).name
    else:
        print("Quarto Project Name?")
        project_name= input("> ")

# Define the project directory
if args.existing_dir:
    project_dir = pathlib.Path(args.directory).resolve()
elif args.directory:
    project_dir = pathlib.Path(args.directory, project_name).resolve()
else:
    project_dir = pathlib.Path(pathlib.Path.cwd(), project_name).resolve()

# Define the template
if args.template:
    template = pathlib.Path(args.template).resolve()
else:
    template = pathlib.Path(__file__).parents[1].joinpath("template").resolve()

# Make the project directory
if not args.existing_dir:
    if pathlib.Path(project_dir).exists():
        print("Project directory already exists. Do you want to overwrite it? (y/n)")
        overwrite = input("> ")
        if overwrite == "y":
            pathlib.Path(project_dir).mkdir(parents=True, exist_ok=True)
        else:
            exit(1)

# Copy the template
if pathlib.Path(template).is_file():
    shutil.copy(template, pathlib.Path(project_dir,project_name+".qmd"))
elif pathlib.Path(template).is_dir():
    shutil.copytree(template,project_dir, dirs_exist_ok=True)
    shutil.move(project_dir.joinpath("template.qmd"), project_dir.joinpath(project_name+".qmd"))
else:
    print("No such template")
    exit(1)


