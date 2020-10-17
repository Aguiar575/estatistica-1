import numpy as np
import statistics as st

X = np.array([12, 24, 36, 10, 12, 2, 9, 12])

moda = st.mode(X)

print("moda: %s", moda)

# moda: 12
