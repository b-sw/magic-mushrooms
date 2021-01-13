<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Authors](#authors)
* [Description of the Problem](#description)
* [Run guide](#run-guide)

## Authors
Piotr Frątczak

Bartosz Świtalski

## Description
Przewidywanie czy [grzyb](https://archive.ics.uci.edu/ml/datasets/mushroom) jest jadalny przy użyciu własnej implementacji algorytmu ID3. Testy binarne. Przed rozpoczęciem realizacji projektu proszę zapoznać się z zawartością [strony](http://staff.elka.pw.edu.pl/~rbiedrzy/PSZT/index.html).

## Run guide
```
/magic-mushrooms

cd magic-mushrooms/
python3 main.py <file> <index> <separator> 
<k> <runs>
```
**file** - file to read data from (inside data/ directory)  
**index** - position of the classifier in the attributes  
**separator** - separator used in the file  
**k** - value of k for k-fold cross-validation  
**runs** - number of test runs, average outcome of all the test runs will be displayed  
