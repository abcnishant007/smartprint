
# smartprint
Save a few seconds and a few keystrokes with every print statement! 😎 
 
- Everytime you want to print something, you lose a few seconds to type in the name of the variable being printed
- Worse still, your IDE helps you autocomplete long variable names but does not autocomplete the print comments

## Your usual print statment: 
```python
print ("veryLongVariableName : ", veryLongVariableName)
```

## Enter smart print:
```python
from smartprint import smartprint as sprint

veryLongVariableName = 25
sprint (veryLongVariableName)
```

#### Output:
```python
veryLongVariableName : 25
```


## Works with multiple variables and all kinds of objects 
```python
from smartprint import smartprint as sprint 
import numpy as np 

a = [1,22,31]
sprint (a, len(a))
sprint (np.random.rand())
```
### Output:
```
a, len(a) : [1, 22, 31] 3
np.random.rand() : 0.649617730484109
```


## Installation 
```
pip install smartprint
```

## Issues
Please feel free to start a pull request/ raise an issue. 
