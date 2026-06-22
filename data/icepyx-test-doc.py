# Loading in data: using icepyx 
## This document is where I will try accessing ICESat-2 from different sources to find the best one before individual analysis
## I will use this file as the main import file of functions to use in later docs

import icepyx as ipx
import h5py
import os

# example from icepyx site, with random parameters

query = ipx.Query(
    # Collection short name
    "ATL06",
    # Bounding box
    [-55, 68, -48, 71],
    # Time bounds
    ['2019-02-20','2019-02-28'],
)
query.download_granules('/tmp/icepyx')