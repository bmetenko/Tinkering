use std::fs::File;
use std::io::{Result, Write};

fn main() -> Result<()> {
    let file_path = "utf8.txt";
    let mut output = File::create(file_path)?;

    let x = (200..255).collect::<Vec<u8>>();
    let y = (150..160).collect::<Vec<u8>>();
    let z = (145..155).collect::<Vec<u8>>();
    let a = (150..160).collect::<Vec<u8>>();

    for x0 in &x {
        for y0 in &y {
            for z0 in &z {
                for a0 in &a {
                    let check_utf: Vec<u8> = vec![*x0, *y0, *z0, *a0];
                    println!("{:?}", &check_utf);

                    let s = std::str::from_utf8(&check_utf);

                    match s {
                        Err(_) => println!("{:?}", check_utf),
                        Ok(s) => writeln!(output, "{:?} : {:?}", check_utf, s)?,
                    }
                }
            }
        }
    }

    Ok(())
}

