# zarr-jpeg2k

### About
JPEG-2000 encoded and decoder for of Zarr chunks using [imagecodecs](https://pypi.org/project/imagecodecs/).  Works with 2D and interleaved RGB data.

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

### References
This repo is heavily influenced by [zarr-jpeg](https://github.com/d-v-b/zarr-jpeg) which uses JPEG encoding to compress chunks of data.
