from .elements import create_air
from .elements import strength_potion
from .elements import healing_potion as heal
from .transmutation.recipes import lead_to_gold

def __getattr__(mname):
    raise AttributeError(f"module '{__name__}' has no attribute '{mname}'")