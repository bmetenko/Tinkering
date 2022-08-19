let img;
let x_max = 600;
let y_max = 400;
let pos;

// idea >> person of interest identifier reticle
// Square and Triangle
// https://personofinterest.fandom.com/wiki/The_Machine/MPOV#Season_1

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

        draw_x_middle["x"] = draw_x_middle["x"] + width + spacing;
    }

};

function quad_vert_line(begin, end, width, height, spacing, use_color=color(255, 255, 255)){
    let line_path = end - begin["x"];
    let draw_x_middle = {"x": begin["x"], "y": begin["y"]};

    console.log(draw_x_middle)
    console.log(line_path)
    while (draw_x_middle["y"] < line_path){
        console.log(draw_x_middle)
        fill(use_color);
        beginShape();
            vertex(draw_x_middle["x"] - height/2, draw_x_middle["y"]);
            vertex(draw_x_middle["x"] + height/2, draw_x_middle["y"]);
            vertex(draw_x_middle["x"] + height/2, draw_x_middle["y"] + width);
            vertex(draw_x_middle["x"] - height/2, draw_x_middle["y"] + width);
        endShape(CLOSE)

        draw_x_middle["y"] = draw_x_middle["y"] + width + spacing;
    }

};

function corner_cap(position, corner){

    corner_x = position["x"]
    corner_y = position["y"]
    use_color=color(255, 255, 255)

    width = 10
    height = 20

    switch (corner) {
        case "top_left":
            fill(color(255,255,255));
            strokeWeight(5);
            // stroke(25);
            arc(corner_x, corner_y, 20, 20, PI, -HALF_PI, PIE);


            fill(use_color);
            beginShape();
                vertex(corner_x - height/2 + 10, corner_y - 10);
                vertex(corner_x + height/2 + 3, corner_y - 10);
                vertex(corner_x + height/2 + 3, corner_y + width - 10);
                vertex(corner_x - height/2 + 3, corner_y + width - 10);
            endShape(CLOSE)
            fill(use_color);
            beginShape();
                vertex(corner_x - height/2, corner_y + 10 + 3);
                vertex(corner_x + height/2 - 10, corner_y + 10 + 3);
                vertex(corner_x + height/2 - 10, corner_y + width - 7);
                vertex(corner_x - height/2, corner_y + width - 7);
            endShape(CLOSE)
        break;

        case "top_right":
            fill(color(255,255,255));
            strokeWeight(5);
            // stroke(25);
            arc(corner_x, corner_y, 20, 20, PI + HALF_PI, PI + PI, PIE);
            beginShape();
                vertex(corner_x - height/2 - 3, corner_y - 10);
                vertex(corner_x - height/2 + 7, corner_y - 10);
                vertex(corner_x - height/2 + 7, corner_y + width - 10);
                vertex(corner_x - height/2 - 3 , corner_y + width - 10);
            endShape(CLOSE)
            fill(use_color);
            beginShape();
                vertex(corner_x - height/2 + 10, corner_y + 10 + 3);
                vertex(corner_x + height/2, corner_y + 10 + 3);
                vertex(corner_x + height/2, corner_y + width - 7);
                vertex(corner_x - height/2 + 10, corner_y + width - 7);
            endShape(CLOSE)
        break;
        
        case "bottom_left":
            fill(color(255,255,255));
            strokeWeight(5);
            // stroke(25);
            arc(corner_x, corner_y, 20, 20, HALF_PI, PI, PIE);
            beginShape();
                vertex(corner_x - height/2, corner_y - 10 - 3);
                vertex(corner_x - height/2 + 10, corner_y - 10 - 3);
                vertex(corner_x - height/2 + 10, corner_y + width - 10);
                vertex(corner_x - height/2, corner_y + width - 10);
            endShape(CLOSE)
            fill(use_color);
            beginShape();
                vertex(corner_x - height/2 + 10 + 3, corner_y + 10);
                vertex(corner_x + height/2 + 3, corner_y + 10);
                vertex(corner_x + height/2 + 3, corner_y + width - 10);
                vertex(corner_x - height/2 + 10 + 3, corner_y + width - 10);
            endShape(CLOSE)
        break;

        case "bottom_right":
            fill(color(255,255,255));
            strokeWeight(5);
            // stroke(25);
            arc(corner_x, corner_y, 20, 20, PI + PI, PI - HALF_PI, PIE);
            beginShape();
                vertex(corner_x - height/2 + 10, corner_y - 10 - 2.5);
                vertex(corner_x - height/2 + 10 + 10, corner_y - 10 - 2.5);
                vertex(corner_x - height/2 + 10 + 10, corner_y + width - 10);
                vertex(corner_x - height/2 + 10, corner_y + width - 10);
            endShape(CLOSE)
            fill(use_color);
            beginShape();
                vertex(corner_x - height/2, corner_y + 10);
                vertex(corner_x + height/2 - 10, corner_y + 10);
                vertex(corner_x + height/2 - 10, corner_y + width - 10);
                vertex(corner_x - height/2, corner_y + width - 10);
            endShape(CLOSE)
        break;
    
        // default:
        // break;
    }

}

function setLineDash(list) {
    drawingContext.setLineDash(list);
  }

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
    stroke(255)
    quad_line({"x": 25, "y": 25}, 330, 20, 5, 10);
    quad_line({"x": 25, "y": 325}, 330, 20, 5, 10);
    console.log("vert_line");
    quad_vert_line({"x": 25, "y": 25}, 330, 20, 5, 10);
    quad_vert_line({"x": 315, "y": 25}, 630, 20, 5, 10);   

    stroke(255);
    // strokeWeight(2);
    noFill();
    // setLineDash([40, 10]); //create the dashed line pattern here
    
    // rect(25, 25, 290, 300);

    fill(255);
    let quad_height = 10;
    let quad_width = 40;
    rect(25, 180, quad_width, quad_height);
    rect(165, 25, quad_height, quad_width);
    rect(275, 180, quad_width, quad_height);
    rect(165, 285, quad_height, quad_width);

    corner_cap({"x": 30, "y": 30}, "top_left");
    corner_cap({"x": 310, "y": 30}, "top_right");
    corner_cap({"x": 30, "y": 320}, "bottom_left");
    corner_cap({"x": 310, "y": 320}, "bottom_right");

};

function draw() {

};

// CustomShape(QUADS)
// Curve vertices
// Pixel based approximations for bounds.