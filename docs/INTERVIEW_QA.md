# Interview Q&A

**Why resolve paths?** Security decisions should use canonical paths.

**Is this a real sandbox?** No. It is an application-level workspace boundary.

**Why allowlist tools?** It minimizes attack surface and makes behavior auditable.

**Why cap rounds?** Agent loops otherwise become unbounded resource consumers.
