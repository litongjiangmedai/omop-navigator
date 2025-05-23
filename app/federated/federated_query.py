from .node_interface import query_remote_node

REMOTE_NODES = [
    "http://localhost:5001",
    "http://localhost:5002"
]

def run_federated_query(sql: str):
    results = []
    errors = []
    for node in REMOTE_NODES:
        res = query_remote_node(node, sql)
        if "error" in res:
            errors.append({node: res["error"]})
        else:
            results.append({node: res["result"]})
    return {"results": results, "errors": errors}
