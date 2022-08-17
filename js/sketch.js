let img;
let x_max = 600;
let y_max = 400;
let pos;

function preload() {
  img = loadImage('grass.png');
  pos = {"x": random(x_max), "y": random(y_max)};
}

function setup() {
    createCanvas(x_max, y_max);
    // line(15, 25, 70, 90);
    // drawingContext.shadowOffsetX = 5;
    // drawingContext.shadowOffsetY = -5;
    // drawingContext.shadowBlur = 10;
    // drawingContext.shadowColor = "black";
    // background(200);
    // ellipse(width/2, height/2, 50, 50);

    image(img, pos["x"], pos["y"]);
}

function draw() {

}