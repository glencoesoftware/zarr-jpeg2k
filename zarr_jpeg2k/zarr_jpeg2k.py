# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENSE.txt
# file you can find at the root of the distribution bundle.  If the file is
# missing please request a copy by contacting info@glencoesoftware.com

from numcodecs.abc import Codec
from numcodecs.compat import \
    ensure_bytes, \
    ensure_contiguous_ndarray, \
    ndarray_copy
from numcodecs.registry import register_codec
import imagecodecs
import numpy as np


class jpeg2k(Codec):
    """Codec providing jpeg2k compression via imagecodecs.
    Parameters
    ----------
    level : int
        Compression level defined by imagecodecs. Relates to peak
        signal-to-noise ratio (PSNR). May need to be the reverse of PSNR
        (eg. 40 PSNR = compression level 60 | 90 PSNR = compression level 10).
    """

    codec_id = "jpeg2k"

    def __init__(self, level=50):
        self.level = level
        assert (self.level > 0 and self.level <= 100
                and isinstance(self.level, int))
        super().__init__()

    def encode(self, buf):
        return imagecodecs.jpeg2k_encode(np.squeeze(buf), level=self.level)

    def decode(self, buf, out=None):
        buf = ensure_bytes(buf)
        decoded = imagecodecs.jpeg2k_decode(buf)
        if out is not None:
            out_view = ensure_contiguous_ndarray(out)
            ndarray_copy(decoded, out_view)
        else:
            out = decoded
        return out


register_codec(jpeg2k)
