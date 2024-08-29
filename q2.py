def print_spiral(n):
    # Initialize a 2D list with zeros
    spiral = [[0] * n for _ in range(n)]
    
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1
    
    while num <= n * n:
        # Fill the top row
        for i in range(left, right + 1):
            spiral[top][i] = num
            num += 1
        top += 1
        
        # Fill the right column
        for i in range(top, bottom + 1):
            spiral[i][right] = num
            num += 1
        right -= 1
        
        # Fill the bottom row
        for i in range(right, left - 1, -1):
            spiral[bottom][i] = num
            num += 1
        bottom -= 1
        
        # Fill the left column
        for i in range(bottom, top - 1, -1):
            spiral[i][left] = num
            num += 1
        left += 1
    
    # Print the spiral
    for row in spiral:
        print(" ".join(f"{cell:2d}" for cell in row))


size = 5
print_spiral(size)
