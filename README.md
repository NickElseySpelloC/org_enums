# org_enums

Shared `StrEnum` definitions for your projects.

## Install (from GitHub tag)
```bash
uv add 'org_enums @ git+https://github.com/NickElseySpelloC/org_enums@v0.1.0'
```
## Install (get latest)
```bash
uv add 'org_enums @ git+https://github.com/NickElseySpelloC/org_enums@main'
```

## Import
```python
from org_enums.enum_power_controller import *           # all PowerController enums
from org_enums.enum_scheduling import *                 # all Scheduling enums
from org_enums.enum_power_controller import AppMode     # Import a specific enum
from org_enums import AppMode                           # Import a specific enum
from org_enums import *                                 # aggregate (same set, explicit)
```
