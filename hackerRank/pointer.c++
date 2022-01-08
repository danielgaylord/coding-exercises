#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Complete this function
    int temp_a = *a;
    *a = temp_a + *b;
    *b = abs(temp_a - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}