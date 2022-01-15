## word-search-breadth-at-depth

### what?
find out how many words can match a given number of starting letters


### why?
i put this together to dissuade myself from trying to guess ahead while
learning to head-copy morse code.

### usage

```
usage: word-search-breadth-at-depth.py [-h] -f FILENAME -d D [D ...]

Count words at specified character depth

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        path to word dictionary (one word per line)
  -d D [D ...], --depths D [D ...]
                        depth at which to measure word search breadth
```

### example

```
$ ./word-search-breadth-at-depth.py -f dictionary/popular.txt -d 3
{3: {'avg': 12, 'worst_case': 392}}
```
