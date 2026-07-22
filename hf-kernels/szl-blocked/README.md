# SZL blocked — immutable loading contract

`szl-blocked` makes a refusal an explicit, hash-chained result. The retained
first-class Kernel Hub artifact is loaded with an immutable revision and
explicit remote-code trust.

## Quickstart

```python
from kernels import get_kernel

blk = get_kernel(
    "SZLHOLDINGS/szl-blocked",
    revision="a6642f7346be5839049eb9a5e29361da18a12562",
    trust_remote_code=True,
)

policy = blk.deny_by_default([blk.allow_if_capability("run")])
result = blk.governed_call(
    lambda: "executed",
    policy=policy,
    request={"capabilities": []},
)
assert result.blocked is True
assert result.output is None
```

## Public API in the retained artifact

| Export | Purpose |
|---|---|
| `GovernedGate` | Produce explicit allow/block decisions. |
| `governed_call` | Run an operation only after an allow decision. |
| `deny_by_default` | Build a hard deny-by-default policy. |
| `allow_if_capability` | Grant a named capability narrowly. |
| `deny_if_flag` / `deny_if_action_in` | Apply hard deny rules. |
| `UnifiedReceiptChain` | Verify decision ordering and integrity. |

Advance the pin only after a new Kernel Hub revision is published and verified.
