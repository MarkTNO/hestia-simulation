# hestia-simulation

Hestia simulation package

## Quick start

1. Install uv: https://docs.astral.sh/uv/
2. Sync dependencies:

   ```bash
   uv sync --all-groups
   ```

3. Run checks:

   ```bash
   uv run ruff check .
   uv run ty check src
   uv run pytest
   ```

## Example

```python
from hestia_simulation import Add

add_op = Add(2, 3)
print(f"Add(2, 3) = {add_op.compute()}")
```
