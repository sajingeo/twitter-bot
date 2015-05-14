#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
// build with cc -o myprog myprog.c -lwiringPi -lpthread
#define M1PWM   12
#define M2PWM   13
#define M1PH    9
#define M2PH    10

#define PWMSPEED 100

int main ( int argc, char *argv[] )
{

if ( argc != 2 ) /* argc should be 2 for correct execution */
    {
        /* We print argv[0] assuming it is the program name */
        printf( "usage: %s motor-nume[1/2] left/right[1/0]", argv[0] );
    }
    //setup GPIO
    if (wiringPiSetupGpio() < 0) return 1; // setup wiring Pi

    //setup PWM I/Os
    pinMode(M1PWM, OUTPUT);
    pinMode(M2PWM, OUTPUT);
    pinMode(M1PH, OUTPUT);
    pinMode(M2PH, OUTPUT);
   	digitalWrite(M1PWM, LOW);
   	digitalWrite(M2PWM, LOW);
   	digitalWrite(M1PH, LOW);
   	digitalWrite(M2PH, LOW);

   	//Create PWM for the PWM lines
   	softPwmCreate(M1PWM, 0, PWMSPEED);
   	softPwmCreate(M2PWM, 0, PWMSPEED);


    if (argv[1] == 1) // motor 1
    {
    	if (argv[2] == 1)
    	{
    		digitalWrite(M1PH, LOW);
    	}
    	else
    	{
    		digitalWrite(M1PH, HIGH);
    	}
    }
    else if (argv[1] == 2)
    {
       	if (argv[2] == 1)
    	{
    		digitalWrite(M2PH, LOW);
    	}
    	else
    	{
    		digitalWrite(M2PH, HIGH);
    	}
    }
    delay (100) ;
    return 0;
}
