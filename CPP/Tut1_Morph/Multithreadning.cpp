#include <stdio.h>
#include <iostream>
#include <string>
#include <thread>

using namespace std;

void *ll(int* tid){
    cout << "Working at " << *tid << endl;
}

int main() {
}