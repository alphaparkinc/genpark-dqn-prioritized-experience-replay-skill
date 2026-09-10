import sys
import json
from client import SumTree

tree = SumTree(1024)

def handle_call(name, arguments):
    if name == "add":
        p = arguments["priority"]
        item = arguments["item"]
        tree.add(p, item)
        return {"total_priority": tree.total_priority(), "count": tree.count}
    elif name == "sample":
        v = arguments["value"]
        idx, prio, item = tree.sample(v)
        return {"data_index": idx, "priority": prio, "item": item}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
