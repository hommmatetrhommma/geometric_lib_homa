# Geometric library
- The project provides simple functions for calculating the area and perimeter of a circle and square.
## Functions
### The module circle.py
- area:calculates the area of a circle with a given radius r
- perimeter:calculates the perimeter of a circle with a given radius r
### The module square.py
- area:calculates the area of a square on a given side of a
- perimeter:calculates the perimeter of a square on a given side of a
### The module triangle.py
- area:calculates the area of a triangle with a given footing a and height h
- perimeter:calculates the perimeter of a triangle with a given side a,b and c
### The module rectangle.py
- area:calculates the area of a rectangle on a given side a and b
- perimeter:calculates the perimeter of a rectangle on a given side a and b
## Examples
### The module circle.py
```python
 radius = 5 
 print(f"The area of the circle: {area(radius)}") # Output: 25 * Pi
 print(f"Circle length {perimeter(radius)}") # Output: 10 * Pi
```
### The module square.py
```python
 print(f"Square area: {area(side)}") # Output: 25
 print(f"The perimeter of the square: {perimeter(side)}") # Output: 20
```
### The module triangle.py
```python
 a=5
 h=5
 b=5
 c=5
 print(area(a,h))
 print(perimeter(a,b,c))
```
### The module rectangle.py
```python
 a=5
 b=5
 print(area(a,b))
 print(perimeter(a,b))
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

## commit history
- 44b4568 - adding documentation for area and perimeter counting functions
- 4e6b786 - adding function descriptions and calling examples to the readme