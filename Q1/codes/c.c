#include<stdio.h>
#include<math.h>
float sqr(float n)
{
        float c=n*n;
        return c;
}
float d1(float x,float y){
	float d=sqrt(sqr(x)+sqr(y));
	return d;
}
float ratio(float x,float y){
        float r=x/y;
        return r;
}
