# init_quarto
## Install
Use pyinstaler to install. If you have not installed pyinstaller, install it by

```
pip install pyinstaller
```

Clone this repository by
```
git clone https://github.com/anabanted/init_quarto
```
or just download this repository.

Enter this repository by
```
cd init_quarto
```

Then build by
```
sh build.sh
```

Copy dist/init_quarto to a directory under PATH (e.g. /usr/bin for Linux).

## Usage
### define project name by option.
```
init_quarto -n PROJECT_NAME
```
### define project name in interactive
```
init_quarto
# Quarto Project Name?
> PROJECT_NAME
```
### specify template
You can use your favorite template with init_quarto by
```
init_quarto -t path/to/template
```
The template should be a qmd(quarto) file or a directory which include 'template.qmd'. Rmd and ipynb files are not used.

Default template is [quarto-template](https://github.com/anabanted/quarto-template).
