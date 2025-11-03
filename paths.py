from pathlib import Path 

print(__file__) # it just shows whole path from like c: to current 

print(Path(__file__)) # it does the same

print(Path(__file__).parent)

print(Path(__file__).parent.parent)