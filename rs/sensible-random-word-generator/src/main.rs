extern crate rand;
extern crate inflector;

use std::env;
use rand::Rng;
use inflector::Inflector;

fn main() {
	// let alphabet: Vec<char> = "abcdefghijklmnopqrstuvwxyz".chars().collect();

	let args: Vec<String> = env::args().collect();
	let mut input: i32 = 10;
	let mut repetition: i32 = 1;

	if args.len() < 2 {
		println!("Didn't specify length and repetition as an argument, default 10 and 1 is used.");
	}else if args.len() < 3 {
		println!("Didn't specify repetition as an argument, default 1 is used.");
		input = args[1].clone().parse::<i32>().unwrap();
	} else {
		input = args[1].clone().parse::<i32>().unwrap();
		repetition = args[2].clone().parse::<i32>().unwrap();
	}
	generate(input, repetition);
}

fn generate(length: i32, repetition: i32) {
	let mut rng = rand::thread_rng();

	let vowels: Vec<char> = "aeiou".chars().collect();
	let consonants: Vec<char> = "bcdfghjklmnpqrstvwxyz".chars().collect();

	for x in 0..repetition {
		let mut result = String::new();
		let mut count: i32 = 1;
		while count <= length {
			if count == 2 {
				result.push(vowels[rng.gen_range(0, vowels.len())]);
			}else if count != 3 && count % rng.gen_range(2, 4) == 0 {
				result.push(vowels[rng.gen_range(0, vowels.len())]);
			}else{
				result.push(consonants[rng.gen_range(0, consonants.len())]);
			}
			count += 1;
		}
		println!("{}", result.to_title_case());
	}
}
