#include<stdio.h>
#include<math.h>
float add(float x,float y){
	return x+y;
}
float d1(float x,float y){
	float d=sqrt(add((x*x),(y*y)));
	return d;
}

