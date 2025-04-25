# import faicons as fa
# import plotly.express as px
# import os

# # Load data and compute static values
# from shared import app_dir, assets_dir, country_list
# from shinywidgets import render_plotly

# from shiny import reactive, render, ui as core_ui
# from shiny.express import input, ui, render
# import shiny.express as sx
# from pathlib import Path

# # bill_rng = (min(tips.total_bill), max(tips.total_bill))
# MAP_DIR = "www/"
# map_files = [f for f in os.listdir(MAP_DIR) if f.endswith(".html")]

# # Add page title and sidebar
# ui.page_opts(title="Country ROP maps", fillable=True)

# with ui.sidebar(open="desktop"):
#     ui.input_select(
#         "country",
#         "Country",
#         choices=map_files,
#     )
    
    # ui.input_checkbox_group(
    #     "time",
    #     "Food service",
    #     ["Lunch", "Dinner"],
    #     selected=["Lunch", "Dinner"],
    #     inline=True,
    # )
    # ui.input_action_button("reset", "Reset filter")

# Add main content
# ICONS = {
#     "user": fa.icon_svg("user", "regular"),
#     "wallet": fa.icon_svg("wallet"),
#     "currency-dollar": fa.icon_svg("dollar-sign"),
#     "ellipsis": fa.icon_svg("ellipsis"),
# }
# @render.ui
# def map_display():
#     selected_map = f'{input.country()}_map.html'
#     iframe_html = f'''
#         <iframe src="/{assets_dir}/{selected_map}" width="100%" height="600px" style="border:none;"></iframe>
#     '''

#     return core_ui.HTML(iframe_html)

# with ui.layout_columns(fill=False):
#     with ui.card(full_screen=True):
#         ui.card_header("Free Churro")
        
#         @render.ui
#         def map_display():
#             selected_map = input.country()
#             # selected_map = f'{selected_map}_map.html'
#             iframe_html = f'''
#                 <iframe src="/{selected_map}" width="100%" height="600px" style="border:none;"></iframe>
#             '''
#             return core_ui.HTML(iframe_html)

# with ui.layout_columns(fill=False):
#     with ui.value_box(showcase=ICONS["user"]):
#         "Total tippers"

#         @render.express
#         def total_tippers():
#             tips_data().shape[0]

#     with ui.value_box(showcase=ICONS["wallet"]):
#         "Average tip"

#         @render.express
#         def average_tip():
#             d = tips_data()
#             if d.shape[0] > 0:
#                 perc = d.tip / d.total_bill
#                 f"{perc.mean():.1%}"

#     with ui.value_box(showcase=ICONS["currency-dollar"]):
#         "Average bill"

#         @render.express
#         def average_bill():
#             d = tips_data()
#             if d.shape[0] > 0:
#                 bill = d.total_bill.mean()
#                 f"${bill:.2f}"


# with ui.layout_columns(col_widths=[6, 6, 12]):
#     with ui.card(full_screen=True):
#         ui.card_header("Tips data")

#         @render.data_frame
#         def table():
#             return render.DataGrid(tips_data())

#     with ui.card(full_screen=True):
#         with ui.card_header(class_="d-flex justify-content-between align-items-center"):
#             "Total bill vs tip"
#             with ui.popover(title="Add a color variable", placement="top"):
#                 ICONS["ellipsis"]
#                 ui.input_radio_buttons(
#                     "scatter_color",
#                     None,
#                     ["none", "sex", "smoker", "day", "time"],
#                     inline=True,
#                 )

#         @render_plotly
#         def scatterplot():
#             color = input.scatter_color()
#             return px.scatter(
#                 tips_data(),
#                 x="total_bill",
#                 y="tip",
#                 color=None if color == "none" else color,
#                 trendline="lowess",
#             )

#     with ui.card(full_screen=True):
#         with ui.card_header(class_="d-flex justify-content-between align-items-center"):
#             "Tip percentages"
#             with ui.popover(title="Add a color variable"):
#                 ICONS["ellipsis"]
#                 ui.input_radio_buttons(
#                     "tip_perc_y",
#                     "Split by:",
#                     ["sex", "smoker", "day", "time"],
#                     selected="day",
#                     inline=True,
#                 )

#         @render_plotly
#         def tip_perc():
#             from ridgeplot import ridgeplot

#             dat = tips_data()
#             dat["percent"] = dat.tip / dat.total_bill
#             yvar = input.tip_perc_y()
#             uvals = dat[yvar].unique()

#             samples = [[dat.percent[dat[yvar] == val]] for val in uvals]

#             plt = ridgeplot(
#                 samples=samples,
#                 labels=uvals,
#                 bandwidth=0.01,
#                 colorscale="viridis",
#                 colormode="row-index",
#             )

#             plt.update_layout(
#                 legend=dict(
#                     orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5
#                 )
#             )

#             return plt


ui.include_css(app_dir / "dashboard" / "styles.css")

# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------


# @reactive.calc
# def tips_data():
#     bill = input.total_bill()
#     idx1 = tips.total_bill.between(bill[0], bill[1])
#     idx2 = tips.time.isin(input.time())
#     return tips[idx1 & idx2]


# @reactive.effect
# @reactive.event(input.reset)
# def _():
#     ui.update_slider("total_bill", value=bill_rng)
#     ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])
# sx.static_assets(assets_dir)