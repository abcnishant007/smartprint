
[![Python application](https://github.com/abcnishant007/smartprint/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/abcnishant007/smartprint/actions/workflows/python-app.yml)  [![Upload Python Package](https://github.com/abcnishant007/smartprint/actions/workflows/python-publish.yml/badge.svg)](https://github.com/abcnishant007/smartprint/actions/workflows/python-publish.yml)  [![codecov](https://codecov.io/gh/abcnishant007/smartprint/branch/main/graph/badge.svg?token=JW8K38C2QR)](https://codecov.io/gh/abcnishant007/smartprint) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Downloads](https://static.pepy.tech/personalized-badge/smartprint?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/smartprint)
## smartprint
Save a few seconds and a few keystrokes with every print statement! 😎 

#### Usual print statment: 
```python
print ("veryLongVariableName : ", veryLongVariableName)
```

#### Enter smart print:
```python
from smartprint import smartprint as sprint

veryLongVariableName = 25
sprint (veryLongVariableName) 
```

##### Output:
```python
veryLongVariableName : 25
```

## Examples:
#### 1. smartprint works with multiple variables and different kinds of objects 
```python
from smartprint import smartprint as sprint 
import numpy as np 

a = [1,22,31]
sprint (a, len(a))
sprint (np.random.rand())
```
##### Output:
```
a, len(a) : [1, 22, 31] 3
np.random.rand() : 0.649617730484109
```


#### 2. `smartprint` includes pretty print (through `pprint` module and colored prints through [`rich`](https://github.com/Textualize/rich) module) for lists and dicts as shown below:
##### 2 (a) List example
```python

d = {-1:"dictionaries", 0: "are", 100:"keys", "boolean":[True, False],
     6:"printed", 50:" with sorted", "Nishant":"Kumar", \
     "numbers":[1,100,-2000,12]}
sprint (d)
```
##### Output:
<img src="https://user-images.githubusercontent.com/9101260/196955542-4b6a97b8-92fa-42af-ad13-d7afbba86112.png" alt="drawing" width="320"/>


## In place print replacement
As suggested by user @nickdelgrosso in [Issue 7](https://github.com/abcnishant007/smartprint/issues/7),
if 
```python
from smartprint import smartprint as print
```
is used, smartprint can be used as an in-place print replacement. 
Alternatively, it can be used to override the existing print statements without touching any other parts of the code. 

#### Installation 
```
pip install smartprint
```

#### Issues
Please feel free to start a pull request/ raise an issue. 

#### Code coverage plot
<img src="https://codecov.io/gh/abcnishant007/smartprint/branch/main/graphs/tree.svg?token=JW8K38C2QR" alt="drawing" width="120"/>
