#!/usr/bin/env python3
"""Compare current system DNS answers with a saved baseline."""
import argparse, json, socket
from pathlib import Path

def normalize(addresses):
    return sorted({str(item) for item in addresses})

def compare(baseline, current):
    before=set(normalize(baseline)); after=set(normalize(current))
    return {"added":sorted(after-before),"removed":sorted(before-after),"unchanged":sorted(before & after)}

def resolve(host, port=443):
    answers=socket.getaddrinfo(host,port,type=socket.SOCK_STREAM)
    return normalize(row[4][0] for row in answers)

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("host"); p.add_argument("--port",type=int,default=443); p.add_argument("--baseline",type=Path); p.add_argument("--save",type=Path)
    a=p.parse_args(argv)
    try:
        current=resolve(a.host,a.port)
        if a.save:
            a.save.write_text(json.dumps({"host":a.host,"addresses":current},indent=2)+"\n",encoding="utf-8")
            print(f"Saved {len(current)} address(es) to {a.save}"); return 0
        if not a.baseline:
            print(json.dumps({"host":a.host,"addresses":current},indent=2)); return 0
        data=json.loads(a.baseline.read_text(encoding="utf-8"))
        before=data.get("addresses",[]) if isinstance(data,dict) else data
        result=compare(before,current); print(json.dumps(result,indent=2))
        return 1 if result["added"] or result["removed"] else 0
    except (OSError,ValueError,socket.gaierror) as exc: p.error(str(exc))
if __name__=="__main__": raise SystemExit(main())
