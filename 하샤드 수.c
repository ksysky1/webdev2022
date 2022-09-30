#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int copy = x;
    int sum = 0;
    while(copy > 0){
        sum += copy % 10;
        copy = copy / 10;
    }
    if (x % sum == 0)
        answer = true;
    else 
        answer = false;
        
    return answer;
}
