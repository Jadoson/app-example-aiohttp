import logging
import time

from aiohttp import web

log = logging.getLogger(__name__)


@web.middleware
async def timing_middleware(request, handler):
    started = time.perf_counter()
    response = await handler(request)
    elapsed = (time.perf_counter() - started) * 1000
    response.headers["X-Response-Time"] = f"{elapsed:.1f}ms"
    log.info("%s %s -> %s (%.1f ms)", request.method, request.path, response.status, elapsed)
    return response
