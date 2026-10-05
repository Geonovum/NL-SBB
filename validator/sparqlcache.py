"""Cache voor rdflib's SPARQL-parser. pySHACL bouwt per focus node dezelfde
querytekst opnieuw; zonder cache gaat ~90% van de tijd naar parsen."""
from functools import lru_cache
import rdflib.plugins.sparql.processor as proc

_parse, _translate = proc.parseQuery, proc.translateQuery
_cache = {}


@lru_cache(maxsize=512)
def _parse_cached(q):
    return _parse(q)


def parseQuery(q):
    return _parse_cached(q) if isinstance(q, str) else _parse(q)


def translateQuery(tree, base=None, initNs=None):
    key = (id(tree), base, tuple(sorted((initNs or {}).items())))
    hit = _cache.get(key)
    if hit is None or hit[0] is not tree:
        hit = (tree, _translate(tree, base, initNs))
        _cache[key] = hit
    return hit[1]


proc.parseQuery, proc.translateQuery = parseQuery, translateQuery
