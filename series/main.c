//
//  main.c
//  series
//
//  Created by royalty on 2023/3/8.
//

#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897

double approximate()    // 本函数是为了估计k，数学根据是带 x 的余项是小于 x = 0 时的余项，所以可以根据平方倒数和的余项值作为截断误差的上界
{
    double k = 1;
    double epsilon = 1;
    double sum = 0;
    while(epsilon >= 10e-7)
    {
        sum = sum + 1/(k * k);
        epsilon = pow(PI,2)/6 - sum;
        k++;
    }
    return k;
}

double series(double x,double upper)    //求和一直求到 upper 项
{
    double summary = 0;
    int k = 1;
    
    for(k = 1; k<=upper; k++)
    {
        summary = summary + 1/(k * (k + x));
    }
    return summary;
}

int main(int argc, const char * argv[])
{

    double x[7] = {0.0,0.5,1.0,sqrt(2),10.0,100.0,300.0};
    double appro = approximate();
    
    for(int i = 0; i<=6; i++)
    {
        printf("x = %lf, \ty = %lf\n",x[i],series(x[i],appro));
    }
    return 0;
}
