#include <stdio.h>
#include <math.h>

int main()
{
    char *filename = "dat.txt";
    FILE *fp = fopen(filename, "w");
    
    if (fp == NULL)
    {
        printf("Error opening the file %s\n", filename);
        return -1;
    }

    // Circle parameters
    float radius = 1.5;
    int num_points_circle = 100;

    // Generate points on the circle
    for (int i = 0; i < num_points_circle; i++) {
        float angle = 2 * M_PI * i / num_points_circle;
        float x = radius * cos(angle);
        float y = radius * sin(angle);
        fprintf(fp, "%.2f;%.2f;Circle\n", x, y);
    }

    // Generate points on the line
    float x_start = 0, x_end = 1.5;  // From (0, 3/2) to (3/2, 0)
    fprintf(fp, "%.2f;%.2f;Line\n", x_start, 1.5); // Point (0, 1.5)
    fprintf(fp, "%.2f;%.2f;Line\n", 1.5, 0.0); // Point (1.5, 0)

    fclose(fp);
    
    return 0;
}

