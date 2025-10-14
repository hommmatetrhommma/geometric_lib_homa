# Geometric library
The project provides simple functions for calculating the area and perimeter of a circle and square.
## Functions
### The module circle.py
area:calculates the area of a circle with a given radius r
perimeter:calculates the perimeter of a circle with a given radius r
### The module square.py
area:calculates the area of a square on a given side of a
perimeter:calculates the perimeter of a square on a given side of a
## Examples
### The module circle.py
```python
 radius = 5
 print(f"The area of the circle: {area(radius)}") # Output: 25 * Pi
 print(f"Circle length {perimeter(radius)}") # Output: 10 * Pi
```
### The module square.py
```python
 side = 5
 print(f"Square area: {area(side)}") # Output: 25
 print(f"The perimeter of the square: {perimeter(side)}") # Output: 20
```


# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a