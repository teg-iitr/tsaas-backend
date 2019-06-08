try:
   from .local_settings import *
except:
	from .production_settings import *

