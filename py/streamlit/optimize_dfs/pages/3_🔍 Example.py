import time

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo

logo_url = "https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png"
add_logo(logo_url)


colored_header(
    label="Optimizations for Iris Dataset",
    description="Batteries? included",
    color_name="orange-70",
)

st.markdown("---")

st.subheader("""
Here, we'll apply some of the optimizations discussed on the previous page to the classic Iris dataset.
""")

st.markdown("---")

iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
iris.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

# Apply some optimizations to the dataset
st.subheader("Optimizations Applied")
st.write("- Dropping the 'class' column")


iris.drop("class", axis=1, inplace=True)


memory_usage_mb = iris.memory_usage(deep=True).sum() / 1024 ** 2

original_memory_usage_mb = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
    header=None
    ).memory_usage(deep=True).sum() / 1024 ** 2
st.write(f" - - Memory Usage: {memory_usage_mb:.2e} MB")
st.write(f"- - Original Memory Usage: {original_memory_usage_mb:.2e} MB")

st.write(f"- - Difference: {np.round(original_memory_usage_mb / memory_usage_mb, 1):.1f}x less memory")


st.write("- Changing the data types")
start_time = time.time()
iris = iris.astype(
    {
        "sepal_length": np.float16, 
        "sepal_width": np.float16, 
        "petal_length": np.float16, 
        "petal_width": np.float16
        }
    )
elapsed_time = time.time() - start_time

st.markdown("""
```python
iris = iris.astype(
    {
        "sepal_length": np.float16, 
        "sepal_width": np.float16, 
        "petal_length": np.float16, 
        "petal_width": np.float16
        }
    )

```
""")

st.write(f"Time to optimize: {elapsed_time:.10f} seconds")

# st.write("- Using vectorized operations")
# iris["sepal_area"] = iris["sepal_length"] * iris["sepal_width"]
# iris["petal_area"] = iris["petal_length"] * iris["petal_width"]

# st.write("- Using in-place operations")
# iris["sepal_area"].apply(np.sqrt, inplace=True)
# iris["petal_area"].apply(np.sqrt, inplace=True)

# Calculate and display the memory usage and elapsed time


st.markdown("---")

st.subheader("Optimizations Telemetry")

memory_usage_mb = iris.memory_usage(deep=True).sum() / 1024 ** 2

st.write(f" - - Memory Usage: {memory_usage_mb:.2e} MB")
st.write(f" - - Original Memory Usage: {original_memory_usage_mb:.2e} MB")

st.write(f" - - Difference: {np.round(original_memory_usage_mb / memory_usage_mb, 1):.1f}x less memory")


st.markdown("---")