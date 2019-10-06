/* C libraries */
#include <stdio.h>
#include <time.h>
#include "mpi.h"

/* the main function */
int main(int argc, char *argv[])
{
	/* Rank and size variables */
	int rank, size;
	/* message is 22 characters long */
	char message[22];
	/* Initialize the MPI execution */
	MPI_Init(&argc,&argv);
	/* Determines the rank of the calling process in the communicator */
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	/* Determines the size of the group associated with a communicator */
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	/* floating variable with the elasped time on the calling processor */
	double start = MPI_Wtime();
	
	/* if the rank is 0, then copies the string pointed to the destination */
	if (rank ==0)
	 strcpy(message, "Hello, john from #0!\n");
	/* Broadcasts a message fron the process with rank "root" to all other processes of the communicator */
	MPI_Bcast(message,22,MPI_CHAR,0,MPI_COMM_WORLD);
	/* prints the message with the rank and message */
	printf("Message at proc#%2d:r% .21s\n", rank,message);
	/* floating variable with the elasped time on the calling processor */
	double end = MPI_Wtime();
	/* if the rank ==0, then stop the timer and print the time elasped */
	if (rank ==0)
	 printf("Time elapsed is %f seconds.\n", end-start);
	/*Terminates the calling MPI process's execution environment */
	MPI_Finalize();
	/* quit the program */
	return 0;
}
