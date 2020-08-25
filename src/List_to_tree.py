import collections
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper.Kernel import GH_Author


def unpackList(lst, path=GH_Path(0)):
    tree = DataTree[object]()
    
    for elem in lst:
        
        if isinstance(elem, collections.Iterable):
            tree.MergeTree(unpackList(elem,path.AppendElement(0)))
        else:
            print(path)
            tree.Add(elem,path)
        path = path.Increment(-1)
    return tree



tree_out = unpackList(list) 