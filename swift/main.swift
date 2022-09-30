class Rect {
    var len = 0
    var width = 0

    init(len: Int, width: Int){
        self.len = len
        self.width = width
    }

    func area() -> Int {
        return (len * width)
    }
    
}

func main() {
    // 
    print("Running main function...")
    let r1 = Rect(len: 2, width: 3)
    print(r1.area())

}

main()