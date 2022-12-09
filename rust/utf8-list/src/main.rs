use std::fs::File;
use std::io::Write;

fn main() -> std::io::Result<()> {

    let file_path = "utf8.txt";
    let mut output = File::create(file_path).expect("Unable to create file");

    let x: Vec<u8> = (240..255).collect();
    let y: Vec<u8> = (150..160).collect();
    let z: Vec<u8> = (145..155).collect();
    let a: Vec<u8> = (150..160).collect();

    for x0 in x.iter() {
        for y0 in y.iter(){
            for z0 in z.iter(){
                for a0 in a.iter(){
                    let check_utf: Vec<u8> = vec![*x0, *y0, *z0, *a0];
                    println!("{:?}", &check_utf);

                    let s = std::str::from_utf8(&check_utf);
                
                    match s {
                        Err(_s) => println!("{:?}", check_utf),
                        Ok(s) => writeln!(output, "{:?} : {:?}", check_utf, s).expect("Could not write line...")
                    }
                }
            }
        }
    }



    Ok(())
}
