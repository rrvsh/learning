use std::io::{self};

use rand::{thread_rng, Rng};

fn main() {
    println!("Enter your guess.");
    let secret_number = thread_rng().gen_range(1..=100);
    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("test");
        let input: u32 = match input.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        match input.cmp(&secret_number) {
            std::cmp::Ordering::Greater => println!("Too high!"),
            std::cmp::Ordering::Less => println!("Too low!"),
            std::cmp::Ordering::Equal => {
                println!("Guessed correctly.");
                break;
            }
        }
    }
}
