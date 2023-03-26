#include<stdio.h>
#include<wiringPi.h>
#include<stdlib.h>
const int PWM = 1;
int main(void){
    int intensity;
    if (wiringPi.setup() == false){
        exit(-1)
    }
    while (1){
        for (intensity = 0; intensity < 1024; intensity++){
            pwmwrite(PWM, intensity)    
            sleep(10)
            }
        sleep(100)

        for (intensity = 1024; intensity > 0; intensity--){
            pwmwrite(PWM, intensity)    
            sleep(10)
            }
        sleep(100)
    return 0;
}