
# Smart print
Save a few seconds with every print statement 

- Everytime you want to print something, you lose a few seconds to type in the name of the variable being printed
- Worse still, your IDE helps you autocomplete long variable names but does not autocomplete the print comments
```

```

## Enter smart print:
```
from smartprint import smartprint as sprint
veryLongVariableName = 25
sprint (veryLongVariableName)
```

## Output:
```
veryLongVariableName : 25
```

## Installation 
```
pip install smartprint
```

## Issues
Please feel free to start a pull request/ raise an issue. 
