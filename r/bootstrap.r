library(bslib)
library(shiny)
library(rmarkdown)
library(plotly)

library(plotly)

sparkline <- plot_ly(economics) |>
  add_lines(
    x = ~date, y = ~psavert,
    color = I("blue"), span = I(1),
    fill = 'yellow', alpha = 0.3,
    name="Personal Savings Rate"
  ) |>
    add_lines(
    x = ~date, y = ~uempmed,
    color = I("red"), span = I(2),
    fill = 'green', alpha = 0.3,
    name="Unemployment"
  ) |>
  layout(
    xaxis = list(visible = F, showgrid = F, title = ""),
    yaxis = list(visible = F, showgrid = F, title = ""),
    hovermode = "x",
    margin = list(t = 0, r = 0, l = 0, b = 0),
    font = list(color = "white"),
    paper_bgcolor = "transparent",
    plot_bgcolor = "transparent"
  ) |>
  config(displayModeBar = F) %>%
  htmlwidgets::onRender(
    "function(el) {
      var ro = new ResizeObserver(function() {
         var visible = el.offsetHeight > 200;
         Plotly.relayout(el, {'xaxis.visible': visible});
      });
      ro.observe(el);
    }"
  )




light_theme <- bs_theme(bootswatch = "minty", version=5)
dark_theme <- bs_theme(bootswatch = "cyborg", version=5)

ui <- fluidPage(
    theme=light_theme,
    checkboxInput("dark_mode_toggle", "Dark Mode"),
    value_box(
        title = "Personal Savings Rate",
        value = "7.6%",
        p("Started at 12.6%"),
        p("Averaged 8.6% over that period"),
        p("Peaked 17.3% in May 1975"),
        showcase = sparkline,
        full_screen = TRUE,
        theme_color = "success"
    ),
    "Hello, world!"
)

server <- function(input, output, session) {
    bs_themer()
    observe(
        session$setCurrentTheme(
            if (isTRUE(input$dark_mode_toggle)) dark_theme else light_theme
        )
    )
}

shinyApp(ui, server)