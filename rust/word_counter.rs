use std::{collections::HashMap, env, fs};
fn main() {
 let path=env::args().nth(1).expect("usage: word_counter <file>");
 let text=fs::read_to_string(path).expect("cannot read file");
 let mut words=HashMap::new();
 for word in text.split_whitespace().map(|w| w.to_lowercase()) {
  *words.entry(word).or_insert(0)+=1;
 }
 let mut list:Vec<_>=words.into_iter().collect();
 list.sort_by(|a,b| b.1.cmp(&a.1));
 for (word,count) in list.into_iter().take(10) { println!("{count:>3} {word}"); }
}
