## word-count.py

### why?
i put this together to dissuade myself from trying to guess ahead while
learning to head-copy morse code.

### usage

```
usage: word-count.py [-h] --filename FILENAME --depths D [D ...]

Count words at specified character depth

optional arguments:
  -h, --help           show this help message and exit
  --filename FILENAME
  --depths D [D ...]   char depth to traverse word list
```

### example

```
$ ./word-count.py --filename dictionary/popular.txt --depths 2 3 4
{2: {'min': 1, 'avg': 101, 'max': 1029}, 3: {'min': 1, 'avg': 12, 'max': 392}, 4: {'min': 1, 'avg': 4, 'max': 105}}
```
