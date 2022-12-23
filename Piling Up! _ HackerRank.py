# Enter your code here. Read input from STDIN. Print output to STDOUT
def cube(blocks):
    left = 0
    right = len(blocks) - 1
    current_cube_value = float("inf")
    while left < right:
        if blocks[left] >= blocks[right] and  blocks[left] <= current_cube_value:
            current_cube_value = blocks[left]
            left += 1
        elif blocks[right] >= blocks[left] and  blocks[right] <= current_cube_value:
            current_cube_value = blocks[right]
            right -= 1
        else:
            return "No"
    return "Yes"

T = int(input())
for i in range(T):
    n = int(input())
    blocks = [int(l) for l in input().split()]
    print(cube(blocks))
