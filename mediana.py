import numpy as np
import statistics as st

X = np.array([12, 24, 36, 10, 12.5, 2, 9, 18])

media = st.median(X)
median_low = st.median_low(X)
median_high = st.median_high(X)

print("median: %s", media)
print("median_low: %s", median_low)
print("median_high: %s", median_high)

# median: 12.25
# median_low: 12.0
# median_high: 12.5