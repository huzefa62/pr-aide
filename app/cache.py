from __future__ import annotations
from typing import Optional


from app.config import settings


try:
# redis 5.x includes asyncio under redis.asyncio
import redis.asyncio as redis # type: ignore
except Exception: # pragma: no cover
redis = None # type: ignore




class Cache:
def __init__(self) -> None:
self._backend = settings.cache_backend
self._mem: dict[str, str] = {}
self._redis: Optional["redis.Redis"] = None


async def init(self) -> None:
if self._backend == "redis":
assert redis is not None, "redis package missing; install 'redis>=5'"
self._redis = redis.from_url(settings.redis_url, decode_responses=True)


async def get(self, key: str) -> Optional[str]:
if self._backend == "memory":
return self._mem.get(key)
assert self._redis is not None
return await self._redis.get(key)


async def set(self, key: str, value: str, ttl: int = 300) -> None:
if self._backend == "memory":
self._mem[key] = value
return
assert self._redis is not None
await self._redis.set(key, value, ex=ttl)




cache = Cache()