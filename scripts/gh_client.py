import requests

API_URL = "https://api.github.com/graphql"


def run_query(token, query, variables):
    response = requests.post(
        API_URL,
        json={"query": query, "variables": variables},
        headers={"Authorization": f"bearer {token}"}
    )
    response.raise_for_status()
    data = response.json()
    if "errors" in data:
        raise RuntimeError(data["errors"])
    return data