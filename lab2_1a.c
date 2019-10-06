/* C libraries */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/* Define the vector length */
#define NP 100000

/* Vector Variable */
int vect1[NP];

/* Main function */
int main(int argc, char *argv[])
{
	/* long integer type i, and long integer vector */
	unsigned long int i, n=(unsigned long int)NP;
	/* Clock Variable */
	clock_t start, end;
	/* FLoating Point variable totsum*/
	double totsum = 0.0;
	/* seeds the random numnber generator with the time function with NULL */
	srand(time(NULL));
	/* the for loop, where the vector,i, equals to the random integer modded by 100 plus 1 */
	for (i=0; i<n; i++) vect1[i] = (rand() % 100 + 1);
	/* start the clock */
	start = clock();
	/* for loop, where the totsum + the floating varible vector and return the value back to totsum */
	for (i=0; i<n; i++)
	{
		totsum += (double) vect1[i];
	}
	/* end the clock */
	end = clock();
	/* elasped time calculation set to t */
	double t = (double) (end-start)/CLOCKS_PER_SEC;
	/* print out the results of the totsum and the time */
	printf("The total sum is %f.\n",totsum);
	printf("Time elapsed is %f secs.\n",t);

	
	return 0;
}
