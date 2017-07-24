# cipher

## Installation
```
$ pip3 install git+https://github.com/solus-impar/cipher.git@master
```
If you are not in a [virtualenv] you may need to use `pip3` with `sudo` or
`--user`.

If you'd rather clone the repository.
```
$ git clone https://github.com/solus-impar/cipher.git
$ cd cipher
$ pip3 install .
$ python3 -m cipher
```

## Usage
```
$ cipher [-h] [-i INPUT] [-k KEY TYPE] [-o OUTPUT] [-s HOST PORT]
```
* `INPUT` can be either a string or path to a file.
* `KEY` can have a `TYPE` of `[shift]` or `[sub]stitution`.
* `OUTPUT` is a path to a file. If not set, output is printed to screen.
* `SERVER` option is mutually exclusive with other options.

[virtualenv]: https://virtualenv.pypa.io/en/stable/
