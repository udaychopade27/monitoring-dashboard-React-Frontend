import httpx
from app.config import settings

class GrafanaClient:
    def __init__(self):
        self.base_url = settings.GRAFANA_URL.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {settings.GRAFANA_SERVICE_ACCOUNT_TOKEN}",
            "Content-Type": "application/json",
        }

    async def list_dashboards(self):
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"{self.base_url}/api/search?type=dash-db",
                headers=self.headers,
            )
            res.raise_for_status()
            return res.json()

    async def get_dashboard_by_uid(self, uid: str):
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"{self.base_url}/api/dashboards/uid/{uid}",
                headers=self.headers,
            )
            res.raise_for_status()
            return res.json()
