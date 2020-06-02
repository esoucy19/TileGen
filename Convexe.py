"""
Implementation of a simple algorithm to generate convex polyominos.

Algorithm:
1 - Decide on a rectangle. This will be the smallest rectangle bounding the
    polyominos' perimeter.

2 - Pick a point along the left side of the rectangle. This point must not be
    a corner.

3 - Generate a tree of valid paths consisting only of the directions Up and
    Right. All paths must terminate on a point along the top edge of the
    rectangle and can't terminate on a corner.

4 - Repeat with the directions Right and Down, stopping at the right edge, then
    Down and Left, stopping and the bottom edge, then Left and Up, stopping
    at the left edge.

5 - For any paths that terminate on the left side of the rectangle but not at
    the point of origin, append Up directions to them until they do.

6 - Repeat for all points along the left side of the rectangle.

7 - Rewrite all paths so they start at the bottom leftmost point of the
    polyomino.

8 - Eliminate duplicate paths.

Inputs: (int, int): The height and width of the bounding rectangle.
Outputs: {string}: A set of strings representing the paths of the generated
                   polyominos.
"""

class BoundingRectangle:
    def __init__(self, h: int, w: int) -> None:
        self.height = h
        self.width = w
        self.left = tuple((0, y) for y in range(0, h + 1))
        self.top = tuple((x, h) for x in range(0, w + 1))
        self.right = tuple((w, y) for y in range(0, h + 1))
        self.bottom = tuple((x, 0) for x in range(0, w + 1))


rect = BoundingRectangle(3, 4)
print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)
