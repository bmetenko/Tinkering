let img;
let x_max = 600;
let y_max = 400;
let pos;

// idea >> person of interest identifier reticle
// Square and Triangle
function quad_line(begin, end, width, height, spacing, use_color=color(255, 255, 255)){
    let line_path = end - begin["x"];
    let draw_x_middle = {"x": begin["x"], "y": begin["y"]};

    console.log(draw_x_middle)
    console.log(line_path)
    while (draw_x_middle["x"] < line_path){
        console.log(draw_x_middle)
        fill(use_color);
        beginShape();
            vertex(draw_x_middle["x"], draw_x_middle["y"] + height/2);
            vertex(draw_x_middle["x"], draw_x_middle["y"] - height/2);
            vertex(draw_x_middle["x"] + width, draw_x_middle["y"] - height/2);
            vertex(draw_x_middle["x"] + width, draw_x_middle["y"] + height/2);
        endShape(CLOSE)

        draw_x_middle["x"] = draw_x_middle["x"] + width + spacing
    }

};

function preload() {
  img = loadImage('grass.png');
  pos = {"x": random(x_max), "y": random(y_max)};
};

function setup() {
    createCanvas(x_max, y_max);
    // line(15, 25, 70, 90);
    // drawingContext.shadowOffsetX = 5;
    // drawingContext.shadowOffsetY = -5;
    // drawingContext.shadowBlur = 10;
    // drawingContext.shadowColor = "black";
    background(200);
    // ellipse(width/2, height/2, 50, 50);

    // image(img, pos["x"], pos["y"]);
    quad_line({"x": 25, "y": 25}, 330, 20, 5, 10);
};

function draw() {

};