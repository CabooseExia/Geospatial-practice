import faicons as fa
import plotly.express as px

# Load data and compute static values
from shared import app_dir, country_list, assets_dir
from shinywidgets import output_widget, render_plotly

from shiny import App, reactive, render, ui

# Add page title and sidebar
app_ui = ui.page_fluid(

    ui.tags.h1("🌍 Country Map Viewer", style="margin-bottom: 20px; font-weight: bold;"),

    # Sidebar + Main panel layout
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("country", "Country", choices=country_list),
            ui.input_dark_mode() 
        ),
        ui.card(
            ui.output_ui("map_display")
        ),
    )
)
def server(input, output, session):
    @output
    @render.ui
    def map_display():
        selected_file = f"{input.country()}.html"
        return ui.HTML(
            f'<iframe src="{selected_file}" width="100%" height="600px" style="border:none;"></iframe>'
        )


app = App(app_ui, server, static_assets=assets_dir)
