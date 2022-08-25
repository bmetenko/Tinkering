use druid::widget::{Button, Flex, Label};
use druid::{AppLauncher, LocalizedString, PlatformError, Widget, WidgetExt, WindowDesc};

fn main() -> Result<(), PlatformError> {
    let main_window = WindowDesc::new(ui_builder);
    let data = 0_u32;
    let data0 = 1_u32;
    AppLauncher::with_window(main_window)
        .use_simple_logger()
        .launch(data)
}

fn ui_builder() -> impl Widget<u32> {
    // The label text will be computed dynamically based on the current locale and count
    let text =
        LocalizedString::new("hello-counter").with_arg("count", |data: &u32, _env| (*data).into());
    let label = Label::new(text).padding(10.0).center();

    let text0 = LocalizedString::new("hello-counter").with_arg("count", |data0: &u32, _env| (*data0).into());
    let label0 = Label::new(text0).padding(10.0).center();

    let button = Button::new("increment")
        .on_click(|_ctx, data, _env| *data += 1)
        .padding(5.0);

    let button0 = Button::new("second increment")
        .on_click(|_ctx, data0, _env| *data0 +=2)
        .padding(10.0);

    Flex::column().with_child(label).with_child(button).with_child(label0).with_child(button0)
}