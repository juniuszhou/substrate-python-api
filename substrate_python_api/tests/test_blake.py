import asyncio
import websockets
import json
from substrate_python_api.utils.blake2 import get_blake2_256
import base58


balance = b'Balances FreeBalance'
print([x for x in b'Balances FreeBalance'])

print(get_blake2_256(balance))


