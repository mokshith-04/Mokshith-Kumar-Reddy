#include <stdio.h>
float div(float,float);
float coord(float,float,float);

int main()
{
	int i;
    char *filename = "dat.txt";
    float x[3],y[3];
    FILE *fp = fopen(filename, "w");
    if (fp == NULL)
    {
        printf("Error opening the file %s", filename);
        return -1;
    }
    x[0]=1; y[0]=-5;
    x[1]=-4; y[1]=5;
    x[2]=-1.5; y[2]=0;
	    fprintf(fp, "%.2f;%.2f;A[%.2f,%.2f]\n",x[0],y[0],x[0],y[0]);
	    fprintf(fp, "%.2f;%.2f;B[%.2f,%.2f]\n",x[1],y[1],x[1],y[1]);
	    fprintf(fp, "%.2f;%.2f;C[%.2f,%.2f]\n",x[2],y[2],x[2],y[2]);
    fclose(fp);

  float a,b,k;
  k=-div(y[0],y[1]);
  a=coord(x[0],x[1],k);
  b=coord(y[0],y[1],k);
   printf("Ratio=%lf:1\n",k);
  printf("Point of division=(%lf,%lf)\n",a,b);
    return 0;
}
