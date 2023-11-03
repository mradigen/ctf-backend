# Both work, but routes.ctf is more clear to indicate that the router is from ctf
# from . import router
from routes.ctf import router


@router.get("/start/{ctf_id}")
async def ctf_start(ctf_id: int):
    # Do the whole big starting code thingy
    return {"status": "CTF started"}
