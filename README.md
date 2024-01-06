# Python Jinja2 renderer
This `render.py` script intakes a YAML file containing variables and a Jinja2 template and returns a rendered output in the console.  
There are also samples for both files showing some options for templating.

Tested with: Python 3.10

## Usage
Show all available options:
``` bash
./render.py -h
```

Render the sample files:
``` bash
./render.py -y sample.yml -j sample.j2
```
