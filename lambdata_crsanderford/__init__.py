__version__ = "0.1.0"
my_str = "this is my_str from __init__.py"

import pandas as pd
import numpy as np

# test functions

ONES = pd.DataFrame(np.ones(5))
ZEROS = pd.DataFrame(np.zeros(20))

# importing df_utils
from df_utils import list_to_column, datesplit
