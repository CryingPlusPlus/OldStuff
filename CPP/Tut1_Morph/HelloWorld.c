#include <stdio.h>
// #include "meineEigeneDatei"

// int add(int a, int b) {
//     return a + b;
// }

double Baby(double x, double a, int n, int i){
    if ( i > n ) {
        return x;
    }
    return Baby(1/2.0 * (x + a/x), a, n, i + 1);
}

float add(float* a, int size) {
    float output;
    for (int i = 0; i < size; i++) {
        output += a[i];
    }
    return output;
}

int main() {

    float arr[10];

    for(int i = 0; i < 10; i++) {
        arr[10] = 1;
    }

    printf("%f\n", add(arr, 10));
    // printf("Hello World!\n");
    // // int a;
    // // int b = 25;
    // // char c = 69;

    // // int d = a & b;
    // // printf("Das ist eine Zahl %d\nund das ist ein Char: %c", a, c);
    // // printf("Deine Zahl bitte: ");
    // // scanf("%d", &a);

    // // if (a == 5){
    // //     printf("\nDeine Zahl ist fuenf\n");
    // // } else {
    // //     printf("Dein Zahl ist was anderes!");
    // // }
    // // printf("Deine Zahl + 1 ist %d", ++a);

    // for (int i = 0; i < 100; i++) {
    //     printf("%d\n", i);
    // }

    // int i = 0;
    // while (1) {
    //     i++;
    //     printf("%d\n", i);

    //     if(i >= 30) {
    //         break;
    //     }
    // }

    // // printf("%d\n", add(12, 12));
    // // printf("%f\n", Baby(1, 25, 100, 0));

    // // double res = Baby(3, 3.141, 25, 0);

    // // printf("\n%p\n", pointer);

    // printf("Arrays :)\n");
    // printf("In C liegt das zweite Element einer Liste genau hinter dem ersten... also phyisch pointer auf 0 + 1 = pointer auf 1\n");
    // float myArray[10];
    // myArray[1] = 42;
    // myArray[2] = 69.0;
    // float *pointer = myArray;
    // printf("%f\n", *pointer);

    // pointer++;
    // printf("%f\n", *pointer);
    // printf("%p\n", *pointer + 1);
    

    

}