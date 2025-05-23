import requests

def query_remote_node(node_url: str, sql: str):
    try:
        response = requests.post(f"{node_url}/api/query", json={"sql": sql}, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
