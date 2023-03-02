#!/bin/bash
ln -s ./quarto-template template
pyinstaller init_quarto.py --onefile --add-data ./template:./template
