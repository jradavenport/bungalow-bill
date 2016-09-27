'''
do basic rotation period search in all K2-Everest light curves

use CDS X-Match Service to match:
EPIC catalog = J/ApJS/224/2/table5
Gaia DR1 = I/337/tgas
=> 1475009220738A.csv
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gatspy.periodic import LombScargleFast

# get bundles of EVEREST lc's here:
e_url = 'https://archive.stsci.edu/missions/hlsp/everest/bundles/'


