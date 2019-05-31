# Word Combination
Produces a list of words consisting of every combination of characters. 
Longer combinations will take more time. Run with python3. 

# Usage
```
$ python3 wordcomb.py [-h] [-p POOL] [-pA] [-pN] [-pL] [-pU] [-pP] [-s SUBCHAR]
                      [-v] [-o OUT]
                      input
```

# Examples
Simple 3 characters words:
```
$ python3 wordcomb.py ???
... (omitted)
```
Alphabeticals only:
```
$ python3 wordcomb.py ??? -pA
... (omitted)
```
Numericals only:
```
$ python3 wordcomb.py ??? -pN
... (omitted)
```
Words start with "abc" and end with any character:
```
$ python3 wordcomb.py abc?
... (omitted)
```
Words ending with "1234" and start with any 3 characters:
```
$ python3 wordcomb.py ???1234
... (omitted)
```
Words starting with "xyz" and ending with "[]", with 10 characters in middle:
```
$ python3 wordcomb.py xyz??????????[]
... (omitted)
```
Use other substitution characters instead of "?":
```
$ python3 wordcomb.py !!! -s !
... (omitted)
```
Use custom character pool:
```
$ python3 wordcomb.py ??? -p abc
bbb
cbb
abb
bcb
ccb
acb
bab
cab
aab
bbc
cbc
abc
bcc
ccc
acc
bac
cac
aac
bba
cba
aba
bca
cca
aca
baa
caa
aaa
```
Have verbose output:
```
$ python3 wordcomb.py ??? -v
... (omitted)
[+] Total time taken: 0:00:06.078104
[+] Total words:      830584
[+] Pool size:        94
```
Save to output file:
```
$ python3 wordcomb.py ??? -o output.txt
```

