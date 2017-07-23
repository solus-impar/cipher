# cipher

## Installation
```
$ pip3 install git+https://github.com/solus-impar/cipher.git@master
```
If you are not in a [virtualenv] you may need to use `pip3` with `sudo` or
`--user`.

## Usage
```
$ cipher -i INPUT [-k KEY] i-o OUTPUT]
```
* `KEY` is a string
* `OUTPUT` is a path to a file.
* `INPUT` can be either a string or path to a file.

For the web server
```
$ export FLASK_APP="path/to/cipher/server.py"
$ flask run
 * Running on http://127.0.0.1:5000/
```

[virtualenv]: https://virtualenv.pypa.io/en/stable/
