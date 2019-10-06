/* C libraries */
#include <stdio.h>
#include <time.h>
#include "mpi.h"

/* main function */
int main(int argc, char *argv[])
{
	/* Rank and size variables with type 99*/
	int rank, size,type=99;
	/* message 1 and 2 with both 23 characters */
	char m1[23], m2[23];
	/* structure that represents the status of the received message */
	MPI_Status status;
	/* Initialize the MPI execution */
	MPI_Init(&argc,&argv);
	/* Determines the rank of the calling process in the communicator */
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	/* Determines the size of the group associated with a communicator */
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	/* floating variable with the elasped time on the calling processor */
	double start = MPI_Wtime();
	/* sends a formatted string output to a string pointed to the rank */
	sprintf(m2,"Hello, John from #%2d!\n",rank);
	/* if the rank is 0, send the message to MPI Comm World and receive the message from status then print the message with rank and final message*/
	if (rank ==0){
	 MPI_Send(m2,23,MPI_CHAR,1,type,MPI_COMM_WORLD);
	 MPI_Recv(m1,23,MPI_CHAR,size-1,type,MPI_COMM_WORLD,&status);
	 printf("Message at proc #%2d: %.22s\n",rank,m1);
	}
	/* receive the message and print the message with the rank and final output then send the m2 */
	else{
	 MPI_Recv(m1,23,MPI_CHAR,rank-1,type,MPI_COMM_WORLD,&status);
	 printf("Message at proc #%2d: %.22s\n",rank,m1);	
	 MPI_Send(m2,23,MPI_CHAR,(rank+1)%size,type,MPI_COMM_WORLD);
	}
	/* floating variable with the elasped time on the calling processor */
	double end = MPI_Wtime();
	/* if the rank is 0, print the time elapsed */
	if (rank ==0)
	 printf("Time elapsed is %f seconds.\n", end-start);
	/*Terminates the calling MPI process's execution environment */
	MPI_Finalize();
	/* quit the program */
	return 0;
}
