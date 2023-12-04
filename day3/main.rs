/*
 467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
 */

use std::env;
use std::fs;

fn main () {
    let file_path = "./input.txt";
    println!("in file {}", file_path);
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read");
    println!("With text:\n{contents}");
}