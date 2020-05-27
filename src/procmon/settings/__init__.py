from .base import *

try:
    from .production import *
except:
    pass

if DEBUG:
    try:
        from .development import *
    except:
        pass
