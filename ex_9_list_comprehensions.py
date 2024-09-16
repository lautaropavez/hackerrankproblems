if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
"""
# forma 1
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(y + 1):
                if i+j+k != n:
                    print(i, j, k)

# forma 2 con compresion lists
resultado = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(resultado)
"""
# resumido forma final 3
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

