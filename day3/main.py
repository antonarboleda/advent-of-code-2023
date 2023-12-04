def part_one():
    mat = []
    with open("input.txt") as f:
        for l in f.readlines():
            line = l.strip()
            chars = []
            for char in line:
                chars.append(char)
            mat.append(chars)
    
    rows = len(mat)
    cols = len(mat[0])   
    result = 0 
    DIRS = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,1], [1,-1],[-1,-1]]

    for r in range(rows):
        c = 0
        while c < cols:
            if mat[r][c].isdigit():
                left_bound = c
                while c < cols and mat[r][c].isdigit():
                    c += 1
                found_symbol = False
                for cc in range(left_bound, c):
                    for x, y in DIRS:
                        nei_r, nei_c = r + x, cc + y
                        if 0 <= nei_r < rows and 0 <= nei_c < cols and not mat[nei_r][nei_c].isdigit() and mat[nei_r][nei_c] != ".":
                            found_symbol = True
                            break
                if found_symbol:
                    result += int("".join(mat[r][left_bound:c]))
            else:
                c += 1

    print(result, "is the result")

def part_two():
    mat = []
    with open("input.txt") as f:
        for l in f.readlines():
            line = l.strip()
            chars = []
            for char in line:
                chars.append(char)
            mat.append(chars)
    
    rows = len(mat)
    cols = len(mat[0])   
    result = 0 
    DIRS = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,1], [1,-1],[-1,-1]]

    for r in range(rows):
        for c in range(cols):
            neighbors = []
            if mat[r][c] == "*":
                for x, y in DIRS:
                    nei_r, nei_c = r + x, c + y
                    digits = []
                    if 0 <= nei_r < rows and 0 <= nei_c < cols and mat[nei_r][nei_c].isdigit():
                        left = nei_c
                        while left >= 0 and mat[nei_r][left].isdigit():
                            digits.insert(0, mat[nei_r][left])
                            left -= 1
                        
                        right = nei_c + 1
                        while right < cols and mat[nei_r][right].isdigit():
                            digits.append(mat[nei_r][right])
                            right += 1
                        neighbors.append(int("".join(digits)))
            if len(neighbors) == 2:
                result += (neighbors[0] * neighbors[1])
    print(result, "is the result")    

if __name__ == "__main__":
    part_one()
    part_two()