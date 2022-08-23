#[derive(Debug)]
struct Rectangle {
    width: i32,
    height: i32,
}

impl Rectangle {
    fn area(&self) -> i32 {
        self.height * self.width
    }

    fn diagonal(&self) -> f32 {
        let mut out: f32 = (self.height.pow(2) + self.width.pow(2)) as f32;
        out = out.sqrt();
        out
    }
}

fn main() {
    let a = Rectangle {
        width: 4,
        height: 3
    };

    println!("rect area: {}", a.area());
    println!("rect diagonal: {}", a.diagonal());

}
