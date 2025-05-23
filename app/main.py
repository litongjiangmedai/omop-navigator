from app.query_generator import generate_sql_from_prompt
from app.sql_generator import run_sql_query
from app.federated.federated_query import run_federated_query
import gradio as gr

def handle_query(prompt: str, use_federated: bool):
    sql = generate_sql_from_prompt(prompt)

    if use_federated:
        result_dict = run_federated_query(sql)
        results_text = ""
        federated_total = 0
        for node_result in result_dict["results"]:
            for node, res in node_result.items():
                try:
                    count = int(res[0][0])  # 假设返回是 [[数字]]
                    federated_total += count
                    results_text += f"\U0001F4C4 {node}: {count}\n"
                except:
                    results_text += f"\U0001F4C4 {node}: {res}\n"

        results_text += f"\n\U0001F9EE Federated total: {federated_total}\n"

        if result_dict["errors"]:
            results_text += "\n\u26A0\uFE0F Errors:\n"
            for err in result_dict["errors"]:
                for node, msg in err.items():
                    results_text += f"{node}: {msg}\n"
    else:
        local_result = run_sql_query(sql)
        results_text = f"\U0001F4CD Local DB Result:\n{local_result}"

    return sql, results_text

def main():
    gr.Interface(
        fn=handle_query,
        inputs=[
            gr.Textbox(lines=2, label="Enter your clinical question"),
            gr.Checkbox(label="\u2611\uFE0F Enable federated mode")
        ],
        outputs=[
            gr.Textbox(lines=3, label="\U0001F50D SQL Generated"),
            gr.Textbox(lines=20, label="\U0001F4CA Results")
        ],
        title="OMOP Navigator Demo",
        description="Enter a question in natural language and choose local or federated query mode."
    ).launch()

if __name__ == "__main__":
    main()
