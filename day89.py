#Koch snowflake fractal
import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10):
    def _koch_snowflake_recursion(p1, p2, depth):
        if depth == 0:
            return [p1, p2]
        else:
            p1 = np.array(p1)
            p2 = np.array(p2)
            delta = p2 - p1

            # Points dividing the segment into thirds
            pA = p1 + delta / 3
            pB = p1 + delta * 2 / 3

            # Point to form the equilateral triangle "bump"
            angle = np.pi / 3
            px, py = pA
            qx, qy = pB
            dx = qx - px
            dy = qy - py
            pC = [px + dx * np.cos(angle) - dy * np.sin(angle),
                  py + dx * np.sin(angle) + dy * np.cos(angle)]

            return (
                _koch_snowflake_recursion(p1, pA, depth - 1)[:-1] +
                _koch_snowflake_recursion(pA, pC, depth - 1)[:-1] +
                _koch_snowflake_recursion(pC, pB, depth - 1)[:-1] +
                _koch_snowflake_recursion(pB, p2, depth - 1)
            )

    # Initial triangle
    height = scale * np.sqrt(3) / 2
    p1 = [0, 0]
    p2 = [scale, 0]
    p3 = [scale / 2, height]

    points = (
        _koch_snowflake_recursion(p1, p2, order)[:-1] +
        _koch_snowflake_recursion(p2, p3, order)[:-1] +
        _koch_snowflake_recursion(p3, p1, order)
    )

    return np.array(points)

# Plot the Koch Snowflake
order = 4  # Increase for more detail
points = koch_snowflake(order)

plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], color='blue')
plt.axis('equal')
plt.axis('off')
plt.title(f'Koch Snowflake (Order {order})')
plt.show()
