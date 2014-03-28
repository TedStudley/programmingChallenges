#include <iostream>

using namespace std;

int countSetMultiples();

int main() {
  
  cout << countSetMultiples() << endl;

  return 0;
}

int countSetMultiples() {
  int count = 0;
  for (int i = 3; i < 1000; i += 3)
    count += i;
  for (int i = 5; i < 1000; i += 5)
    count += i;
  for (int i = 15; i < 1000; i += 15)
    count -= i;

  return count;
}
