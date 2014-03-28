#include <iostream>
#include <vector>

using namespace std;

vector<unsigned long long int> factorize (unsigned long long int number);
unsigned long long int vector_max (vector<unsigned long long int> maxVector);

int main() {
  vector<unsigned long long int> factors = factorize (600851475143);

  cout << vector_max (factors) << endl;

  return 0;
}

vector<unsigned long long int> factorize (unsigned long long int number) {
  vector<unsigned long long int> factors;
  
  int divisor = 2;
  if (number % divisor == 0) {
    factors.push_back (divisor);
    while (number % divisor == 0) number /= divisor;
  }
  do {
    for (divisor = 3; !(number % divisor == 0) || divisor < number / 2; divisor += 2);
    if (number % divisor == 0) {
      cout << divisor << " " << number << endl;
      factors.push_back (divisor);
      while (number % divisor == 0) number /= divisor;
    }
  } while (number > 1);

  return factors;
}

unsigned long long int vector_max (vector<unsigned long long int> maxVector) {
  unsigned long long int max = 0;
  if (!maxVector.empty()) {
    for (vector<unsigned long long int>::iterator it = maxVector.begin(); it != maxVector.end(); ++it) {
      if ((*it) > max) max = (*it);
    }
  } else {
    max = 0;
  }
  return max;
}
