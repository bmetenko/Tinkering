
fn main() {

    let check_utf = vec![240, 159, 141, 137];
    let s = std::str::from_utf8(&check_utf);

    if s.is_err(){
        println!("{:?}", check_utf);
    } else {
        println!("{:?}", s)
    }    

}
