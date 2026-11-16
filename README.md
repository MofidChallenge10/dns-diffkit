# DNS Diffkit

Spot DNS drift without installing a DNS client library. Save a baseline once, then compare the system resolver's current answer set and see added or removed addresses.

![Animated DNS record rings](assets/hero.svg)

## Features
- Resolves A/AAAA results through the operating system resolver.
- Deduplicates and sorts addresses for stable diffs.
- Saves or reads a plain JSON baseline.
- Reports additions and removals without modifying DNS.

## Run

Python 3.10+, standard library only.

```bash
python tool.py example.com --save baseline.json
python tool.py example.com --baseline baseline.json
python -m unittest -v
```

## Scope
This compares the resolver configured on the machine running the command. It does not query authoritative nameservers, bypass caches, or guarantee global propagation. Run from the same network context for meaningful comparisons.

## Design
A constellation of address nodes uses a deep indigo palette. Its orbit motion stops for reduced-motion preferences.

## License
MIT.
