#include "printlib.h"

int main() {
    bool b;
    if (true) { println_string("Vrai"); }
    if (b && true) {
        println_int(0);
    } else {
        println_int(1);
    }
    return 0;
}

// EXPECTED
// Vrai
// 1
