// Author: Eliza Malyshev 
// KUID: 3122318
// Date: 9/19/2024 
// Lab: #3
// Purpose: fast mdoular expansion algorithum 

#include <stdio.h>
void binConverter(int num, int binaryArray[9]) //this will convert any int into its binary version, returned as an array 
{
    for (int i=8; num>0 && i>=0; i--) //incriments backwards so that it makes the array start at LSB 
    {
        binaryArray[i]=num%2; //saves curent least significant bit into array 
        num/=2; //divide by 2 to shift right
    }
}


int recurseExponent(int b, int n, int m, int bit, int arr[]) //this isnt recursive, this just does the modular exponetiation and returns the result 
{
    int x=1; 
    int power=b%m; 
    for (int i=bit-1; i>=0; i--) //starts from the back of the array so that it reads LSB first 
    {
        if(arr[i]==1) //if the bit is set to 1...
        {
            x=(x*power)%m; //multiply x times powermodm to add it according to algorithum 
            // printf("\ncurrent x: %d", x);
        }
        power=(power*power)%m; //after we do the check for bit set we multiply the power again to do (b(n/2))^2 
        // printf("\ncurrent power: %d", power);

        // arr[i]++; // Increment the current element; this was useless, this was the line that messed me up when i was so close 
    }

    return x; 
}



int main()
{
    int b; 
    int n; 
    int m; 
    printf("give integer b: "); 
    scanf("%d", &b); 
    printf("give integer n: "); 
    scanf("%d", &n); 
    printf("give integer m: "); 
    scanf("%d", &m);

    int binary[9]={0,0,0,0,0,0,0,0,0}; //initlaizes array so that binary converter can fill it up, only 9 bits since max is 500 which has 9 bits 
    binConverter(n, binary);
    // printf("Binary representation of %d: ", n);
    // for (int i = 0; i < 9; i++) {
    //     printf("%d", binary[i]);
    // }
    int bit=9; //size of list 
    
    int result=recurseExponent(b,n,m,bit,binary); //calls first recurse which will then split into wether its even or odd exponent; b%m makes sure we have smaller base 
    printf("result: %d", result);

    return 0;
}
