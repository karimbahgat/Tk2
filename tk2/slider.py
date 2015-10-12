
import ttk
from . import mixins as mx

# Add option for ticklabels along the way

class Slider(ttk.Scale, mx.AllMixins):
    def __init__(self, master, *args, **kwargs):
        ttk.Scale.__init__(self, master, *args, **kwargs)
        mx.AllMixins.__init__(self, master)
