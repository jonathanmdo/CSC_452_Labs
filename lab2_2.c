/* C libraries */
#include <stdio.h>
#include <time.h>
#include "mpi.h"

/* the main function */
int main(int argc, char *argv[])
{
	/* Variables */
	int rank, size;
	/* Initialize the MPI execution */
	MPI_Init(&argc,&argv);
	/* Determines the rank of the calling process in the communicator */
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	/* Determines the size of the group associated with a communicator */
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	/* Floating point variable start time */
	double start = MPI_Wtime();
	/* Print out the results with the rank and size */
	printf("Hello, John from #%d of %d!\n", rank, size);
	/* stop the timer */
	double end = MPI_Wtime();
	/* print out the final time elaspsed */
	printf("Time elaspsed is %f secs.\n", end-start);
	/* Terminates the calling MPI process's execution environment */
	MPI_Finalize();
	/* quits the program */
	return 0;
}
