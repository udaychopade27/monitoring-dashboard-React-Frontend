from fastapi import APIRouter, Request
from fastapi.responses import Response, StreamingResponse
import httpx

from app.config import settings

router = APIRouter(prefix="/api/grafana", tags=["grafana"])

# Headers that MUST NOT be forwarded (causes Content-Length crash)
EXCLUDED_HEADERS = {
    "content-length",
    "transfer-encoding",
    "connection",
}


@router.get("/dashboards")
async def list_dashboards():
    """
    Lists dashboards from Grafana without exposing Grafana URL
    """
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(
            f"{settings.GRAFANA_URL}/api/search",
            params={"type": "dash-db"},
            headers={"Accept": "application/json"},
        )

    return resp.json()


@router.get("/embed/{uid}")
async def get_embed_url(uid: str):
    """
    Returns internal embed path (NOT Grafana URL)
    Frontend will load /api/grafana/ui/...
    """
    return {
        "embedPath": f"/api/grafana/ui/d/{uid}?kiosk&theme=light"
    }


@router.api_route(
    "/ui/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
)
async def grafana_ui_proxy(path: str, request: Request):
    """
    Full reverse proxy for Grafana UI.
    Browser -> Backend -> Grafana
    Grafana URL is NEVER exposed.
    """

    target_url = f"{settings.GRAFANA_URL}/{path}"

    async with httpx.AsyncClient(
        timeout=httpx.Timeout(60.0),
        follow_redirects=True,
    ) as client:
        resp = await client.request(
            method=request.method,
            url=target_url,
            params=request.query_params,
            headers={
                k: v
                for k, v in request.headers.items()
                if k.lower() != "host"
            },
            content=await request.body(),
        )

    # Remove dangerous headers
    headers = {
        k: v
        for k, v in resp.headers.items()
        if k.lower() not in EXCLUDED_HEADERS
    }

    # STREAMING RESPONSE (fixes Content-Length crash)
    return StreamingResponse(
        resp.aiter_bytes(),
        status_code=resp.status_code,
        headers=headers,
    )
