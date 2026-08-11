import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    # The actual database/redis status depends on if docker is running
    # but the endpoint should at least return a 200 and a JSON dict.
