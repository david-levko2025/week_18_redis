from fastapi import APIRouter

import dal

route = APIRouter(prefix='analytics',tags=['Analytics'])

@route.get("/alerts-by-border-and-priority")
async def alerts_by_border_and_priority():
    return dal.alerts_by_border_and_priority()

@route.get("/top-urgent-zones")
async def top_urgent_zones():
    return dal.top_urgent_zones()

@route.get("/distance-distribution")
async def distance_distribution():
    return dal.distance_distribution()

@route.get("/low-visibility-high-activity")
async def low_visibility_high_activity():
    return low_visibility_high_activity()

@route.get("/hot-zones")
async def hot_zones():
    return dal.hot_zones()