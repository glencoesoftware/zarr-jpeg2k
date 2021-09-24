# zarr-jpeg2k

### About
Lossy JPEG-2000 encoded and decoder for of zarr chunks using imagecodecs. To be used with isyntax2raw. Works with 2D and interleaved RGB data. 

### Usage
```python3
from zarr_jpeg2k import jpeg2k
import numpy as np
import zarr
codec = jpeg2k(level=50)
data = np.arange(100000000, dtype='uint8').reshape(10000, 10000)
# without zarr
encoded = codec.encode(data)
decoded = codec.decode(encoded)
# with zarr
z = zarr.array(data, chunks=(1000, 1000), compressor=codec)
```
