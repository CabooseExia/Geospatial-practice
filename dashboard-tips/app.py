import faicons as fa
import plotly.express as px

# Load data and compute static values
from shared import app_dir, country_list, assets_dir
from shinywidgets import output_widget, render_plotly

from shiny import App, reactive, render, ui


# Add page title and sidebar
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "country",
            "Country",
            choices=country_list,
        ),
    ),
    ui.output_ui("map_display"),
)
def server(input, output, session):
    @output
    @render.ui
    def map_display():
        selected_map = input.country()
        # selected_map = f'{assets_dir}/{selected_map}_map.html'
        # selected_map = f'{assets_dir}/Cambodia_map.html'
        print(selected_map)
        return ui.HTML(
            f'<iframe src="{assets_dir}/{selected_map}" width="100%" height="600px" style="border:none;"></iframe>'
        )
        # with open(selected_map, "r") as file:
        #     map_html = file.read()
        # return ui.HTML(map_html)


app = App(app_ui, server, static_assets=assets_dir)
