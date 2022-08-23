
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


#### 2. Now, `smartprint` includes pretty print (through `pprint` module) for lists and dicts as shown below:
##### 2 (a) List example
```python
a = [1, 4, 5, 3, 4, "This", "is", \
     ["fun; The inspect module is"], \
     "really powerful","What",["do", [9, 8, 6],"you", "think?", 5]]
sprint (a)
```
##### Output:
```
List: a
[1,
 4,
 5,
 3,
 4,
 'This',
 'is',
 ['fun; The inspect module is'],
 'really powerful',
 'What',
 ['do', [9, 8, 6], 'you', 'think?', 5]]
```
##### 2 (b) Dict example
```python
a = {1:2, 3:"Kumar",31:"Nishant", \
     2.5:{1:2, 3:"Kumar",31:"Nishant", 0:"NK"}, 0:"NK"}
sprint (a)
```
##### Output:
```
Dict: a
Key: Value
{0: 'NK',
 1: 2,
 2.5: {0: 'NK', 1: 2, 3: 'Kumar', 31: 'Nishant'},
 3: 'Kumar',
 31: 'Nishant'}
 ```


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
