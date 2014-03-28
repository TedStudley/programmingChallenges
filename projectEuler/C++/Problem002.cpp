#include <iostream>

using namespace std;

unsigned long long int sumEvenNumbers();
unsigned long long int iterativeFibonacci (int index);

int main()
{

  cout << sumEvenNumbers() << endl;

  return 0;
}

unsigned long long int sumEvenNumbers() {
  unsigned long long int sum = 0;
  int i = 1;
  unsigned long long int fib = iterativeFibonacci (i);
  
  do {
        sum += fib;
        i += 3;
        fib = iterativeFibonacci (i);
  } while (fib < 4000000);

  return sum;
}

unsigned long long int iterativeFibonacci (int index) {
  unsigned long long int first = 1;
  unsigned long long int second = 1;
  unsigned long long int third;

  for (int i = 0; i < index; ++i) {
    third = first + second;
    first = second;
    second = third;
  }

  return third;
}
