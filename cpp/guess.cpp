#include <iostream>
#include <random>
int main(){
 std::mt19937 gen(std::random_device{}()); std::uniform_int_distribution<> d(1,100);
 int target=d(gen), guess=0, tries=0;
 std::cout<<"Guess a number from 1 to 100\n";
 while(guess!=target){std::cin>>guess;tries++;std::cout<<(guess<target?"Higher\n":guess>target?"Lower\n":"Correct!\n");}
 std::cout<<"Solved in "<<tries<<" tries.\n";
}
