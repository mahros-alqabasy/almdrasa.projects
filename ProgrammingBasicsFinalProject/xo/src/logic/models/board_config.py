from dataclasses import dataclass




@dataclass
class BoardConfig:
  size:int
  canRedo:bool
  crossAxis:bool
  