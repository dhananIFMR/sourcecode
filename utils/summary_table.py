import pandas as pd
import dash_table
from dash_table.Format import Format, Scheme, Sign, Symbol

summary_table = [
    {
        "question": "Split of Business ownership by Gender",
        "path": {"key": "Female", "meta": {"displayName": "Female-led %"}},
    },
    {
        "question": "Average no. of full-time employees before lockdown",
        "path": {
            "key": "",
            "meta": {
                "displayName": "Average no. of full-time employees before lockdown"
            },
        },
    },
    {
        "question": """Is your business registered under any sort of 
Government registration?""",
        "path": {"key": "Yes", "meta": {"displayName": "Registered Business %"}},
    },
    {
        "question": "Does your business fall under Essential services?",
        "path": {
            "key": "Essential",
            "meta": {"displayName": "Essential Business %"},
        },
    },
    {
        "question": "What is the type of business you operate?",
        "path": {
            "key": "Fixed Store/ Shop",
            "meta": {"displayName": "Fixed Store %"},
        },
    },
    {
        "question": "What is the type of business you operate?",
        "path": {
            "key": "Home based business",
            "meta": {"displayName": "Home based business %"},
        },
    },
    {
        "question": "What is the type of business you operate?",
        "path": {
            "key": "Small manufacturing plant",
            "meta": {"displayName": "Small manufacturing plant %"},
        },
    },
    {
        "question": "What is the type of business you operate?",
        "path": {
            "key": "Village enterprise",
            "meta": {"displayName": "Village enterprise %"},
        },
    },
]


def make_summary_table(responses, summary_table):
    summary_headers = ["Category", "All"] + [
        x for x in responses["Total Sample"].keys() if x != "Freq"
    ]
    summary_rows = []

    for row in summary_table:
        data = {}
        data[""] = row["path"]["meta"]["displayName"]
        if row["path"].get("key"):
            data["All"] = (
                responses[row["question"]][row["path"]["key"]]["Freq"]
                / responses["Total Sample"]["Freq"]
                * 100.0
            )
            for header in summary_headers[2:]:
                data[header] = (
                    responses[row["question"]][row["path"]["key"]][header]
                    / responses["Total Sample"][header]
                    * 100.0
                )
        else:
            data["All"] = float(responses[row["question"]]["Freq"])
            for x in summary_headers[2:]:
                data[x] = float(responses[row["question"]][x])
        summary_rows.append(data)

    summary_rows = pd.DataFrame(summary_rows)
    return dash_table.DataTable(
        id="table",
        columns=[
            {"name": i, "id": i, "type": "numeric", "format": Format(precision=0, scheme=Scheme.fixed),}
            if i == "Category"
            else {
                "name": i,
                "id": i,
                "type": "numeric",
                "format": Format(precision=0, scheme=Scheme.fixed),
            }
            for i in summary_rows.columns
        ],
        data=summary_rows.to_dict("records"),
        style_header={
            "backgroundColor": "white",
            "fontWeight": "500",
            "border-top": "0px solid #fff",
            "border-right": "0px solid #fff",
            "border-left": "0px solid #fff",
            "border-bottom": "2px solid #0199D6",
            "text-transform": "uppercase",
        },
        style_data_conditional=[
            {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"}
        ],
        style_cell={
            "textAlign": "left",
            "border-color": "#0199D6",
            "font-family": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"',
        },
        style_cell_conditional=[{"if": {"column_id": "Region"}, "textAlign": "left"}],
    )
