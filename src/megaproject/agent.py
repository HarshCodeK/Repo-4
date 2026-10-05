from dataclasses import dataclass
from .tools import dispatch
@dataclass
class Agent:
    workspace:object
    max_rounds:int=4
    def run(self,steps):
        trace=[]
        for i,step in enumerate(steps[:self.max_rounds],1):
            result=dispatch(self.workspace,step["tool"],step.get("args",{}))
            trace.append({"round":i,"tool":step["tool"],"result":result})
        return {"mode":"agent" if len(steps)<=self.max_rounds else "max_rounds","trace":trace}
