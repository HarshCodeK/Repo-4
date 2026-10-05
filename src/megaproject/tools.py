from .sandbox import Workspace
ALLOWED={"list","read"}
def dispatch(ws:Workspace,name:str,args:dict):
    if name not in ALLOWED: raise ValueError("tool_not_allowed")
    return ws.list(args.get("path",".")) if name=="list" else ws.read(args["path"])
