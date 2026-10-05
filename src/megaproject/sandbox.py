from pathlib import Path
class SandboxError(ValueError): pass
class Workspace:
    def __init__(self,root): self.root=Path(root).resolve()
    def path(self,relative):
        p=Path(relative)
        if p.is_absolute() or ".." in p.parts or str(p).startswith("~"): raise SandboxError("unsafe path")
        resolved=(self.root/p).resolve()
        if resolved!=self.root and self.root not in resolved.parents: raise SandboxError("outside workspace")
        return resolved
    def read(self,relative,max_bytes=100_000):
        p=self.path(relative); data=p.read_bytes()
        if len(data)>max_bytes: raise SandboxError("file too large")
        return data.decode("utf-8","replace")
    def list(self,relative="."):
        return sorted(x.name for x in self.path(relative).iterdir())
