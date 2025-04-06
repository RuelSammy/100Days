def dynamicFibo(n, table=None):
    if table is None:
        table = [0] * (n + 1)

    # Base cases
    if n <= 1:
        return n

    # Check if value already computed
    if table[n] != 0:
        return table[n]

    # Recursively compute and store in table
    table[n] = dynamicFibo(n - 1, table) + dynamicFibo(n - 2, table)
    return table[n]

# Example usage
print(dynamicFibo(52)) 
