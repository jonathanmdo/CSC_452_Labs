/* C libraries */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mpi.h"
/* define the vector length */
#define NP 1000
/* vector variable */
int vect1[NP];

/* Main function */
int main(int argc, char *argv[])
{
	/* long integer type i, and long integer vector */
	unsigned long int i, n = (unsigned long int)NP;
	/* Clock Variable */
	clock_t start, end;
	/* FLoating Point variable totsum*/
	double totsum, locsum = 0.0;
	/* rank and size variable */
	int rank, size;
	/* Initialize the MPI execution */
	MPI_Init(&argc,&argv);
	/* Determines the rank of the calling process in the communicator */
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	/* Determines the size of the group associated with a communicator */
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	/* seeds the random numnber generator with the time function with NULL */
	srand(time(NULL)+rank);
	/* the for loop, where the vector,i, equals to the random integer modded by 100 plus 1 */
	for (i=rank; i<n; i+=size) vect1[i] = (rand() % 100 + 1);
	/* start the clock */
	start = clock();
	/* for loop, where the totsum + the floating varible vector and return the value back to totsum */
	for (i=rank; i<n; i+=size)
	{
		locsum += (double) vect1[i];
	}
	/* Reduces values on all processes to a single value */
	MPI_Reduce(&locsum,&totsum,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);
	/* end the time of elasped time on the calling processor*/
	end = MPI_Wtime();
	/* print the final results of the rank and locsum */
	printf("Local sum on process #%2d is %f.\n",rank,locsum);
	/* if the rank ==0, then stop the timer and print the total sum and the time elasped */
	if (rank ==0)
	{	
	double t = (end-start);
	printf("The total sum is %f.\n",totsum);
	printf("Time elapsed is %f secs.\n",t);	
	}
	/* Terminates the calling MPI process's execution environment */
	MPI_Finalize();
	/* quit the program */
	return 0;
}
