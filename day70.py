import numpy as np

def main():
    # 1. Create arrays
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Array a:", a)
    print("Array b:", b)

    # 2. Element-wise operations
    print("a + b:", a + b)
    print("a * b:", a * b)
    print("a squared:", a ** 2)

    # 3. Matrix operations
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)
    print("Matrix multiplication (A @ B):\n", A @ B)

    # 4. Statistics
    data = np.random.randn(1000)
    print("\nRandom Data Sample Mean:", np.mean(data))
    print("Standard Deviation:", np.std(data))

    # 5. Solve system of linear equations
    # Ax = b => Solve for x
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    x = np.linalg.solve(A, b)
    print("\nSolving Ax = b")
    print("Solution x:", x)

if __name__ == "__main__":
    main()
