import copy

import dash_core_components as dcc


def make_question_pie(responses, question):
    business_recovery_data = responses[question]
    first_key = list(responses[question].keys())[0]
    p_key = None
    for k in responses[question][first_key].keys():
        if k.startswith("Percentage"):
            p_key = k
            break
    raw_vals = {k: v["Freq"] for k, v in business_recovery_data.items()}
    business_recovery_data = {
        k: float(v[p_key].replace("%", "")) for k, v in business_recovery_data.items()
    }
    business_recovery_data_keys, business_recovery_data_values = zip(
        *business_recovery_data.items()
    )
    unnormed_vals = ["%d" % raw_vals[x] for x in business_recovery_data_keys]
    data = [
        {
            "values": business_recovery_data_values,
            "labels": business_recovery_data_keys,
            "type": "pie",
            "hovertext": unnormed_vals,
            "hoverinfo": "text",
            "marker": {
                "colors": [
                    "#005DA6",
                    "#FFC52F",
                    "#BAE1FF",
                    "#75C2FF",
                    "#31A4FF",
                    "#00467D",
                    "#CBC53E",
                    "#0199D6",
                    "#6D6E71",
                ]
            },
        }
    ]
    business_recovery_data_plot = dcc.Graph(
        id=question,
        className="graphbox",
        figure={"data": data, "layout": {"height": "200px", "title": question}},
        config={'modeBarButtonsToRemove': ['toggleSpikelines', 'autoScale2d',
                                           'pan2d', 'zoom2d', 'select2d',
                                           'lasso2d', 'hoverClosestGl2d', 'resetScale2d',
                                           'toggleHover', 'hoverClosestCartesian', 'hoverCompareCartesian']}
    )
    return business_recovery_data_plot


def make_bar(responses, question, barmode="group", orientation="v"):
    household_data = copy.deepcopy(responses[question])
    unnormed = {}
    for key in household_data.keys():
        if household_data[key].get("Freq") is not None:
            household_data[key].pop("Freq")
        if household_data[key].get("Percentage") is not None:
            household_data[key].pop("Percentage")
        if household_data[key].get("Percentage of case") is not None:
            household_data[key].pop("Percentage of case")
        if household_data[key].get("Percentage in case") is not None:
            household_data[key].pop("Percentage in case")
        unnormed[key] = {
            k: v
            for k, v in household_data[key].items()
        }
        household_data[key] = {
            k: v / responses["Total Sample"].get(k, 1) * 100
            for k, v in household_data[key].items()
        }

    data_list = []
    colors = [
                        "#005DA6",
                        "#FFC52F",
                        "#BAE1FF",
                        "#75C2FF",
                        "#31A4FF",
                        "#00467D",
                        "#CBC53E",
                        "#0199D6",
                        "#6D6E71",
                    ]
    for i, key in enumerate(household_data.keys()):
        columns, values = zip(*household_data[key].items())
        unnormed_vals = ["%d" % unnormed[key][x] for x in columns]
        t = ["%0.2f %%" % x for x in values]
        if orientation == "h":
            columns, values = values, columns
            t = ["%0.2f %%" % x for x in columns]
        data_list.append(
            {
                "x": columns,
                "y": values,
                "text": t,
                "textposition": "auto",
                "type": "bar",
                "name": key,
                "orientation": orientation,
                "hovertext": unnormed_vals,
                "hoverinfo": "text",
                "color": "x",
                "marker": {
                    "color": colors[i]
                },
            }
        )
    fig = dcc.Graph(
        id="question",
        className="graphbox",
        figure={
            "data": data_list,
            "layout": {
                "title": {"text": question},
                "legend": {"orientation": "h"},
                "barmode": barmode,
                "yaxis": {"title": "% of Responses"},
                "xaxis": {"automargin": True}
            },
        },
        config={'modeBarButtonsToRemove': ['toggleSpikelines', 'autoScale2d',
                                           'pan2d', 'zoom2d', 'select2d',
                                           'lasso2d', 'hoverClosestGl2d', 'resetScale2d',
                                           'toggleHover', 'hoverClosestCartesian', 'hoverCompareCartesian']}
    )
    return fig
