/**************************************
* nome: decay.c
* description: A radioactive decay
* date: 08/12/2019
* last update: 19/05/2021
***************************************/
#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#define MAX 100

//Declaring global variables

double n_uranium[MAX];   /*Number of Uranium atoms*/
double t[MAX];           /*store tome values here*/
double dt;               /*time step*/
double tau;              /*decay time constant*/
double t_max;            /*time to end simulation*/

//functions to call in the main program

/*initializing variables*/

int initialize(nuclei, t, tc, dt) double *nuclei,*t,*tc,*dt;
{
    printf("Initial number of nuclei:\n");
    scanf("%lf",&(nuclei[0]));              //initial value of the  vector
    printf("time constant:\n");
    scanf("%lf",tc);
    printf("time step:\n");
    scanf("%lf",dt);
    t[0] = 0.0;
    return(0);
}

/*Calculating the results and store them in an array t() and n_u() */
int calculate(nuclei,t,tc,dt) double *nuclei,*t,tc,dt;
{
    int i;
    for(i=0; i<MAX-1; i++){
                    nuclei[i+1] = nuclei[i]-(nuclei[i]/tc)*dt;
                         t[i+1] = t[i]+dt;
                        }
    return(0);
}

/*Save the results to a file*/
int store(nuclei, t) double *nuclei,*t;
{
    FILE *fp_out;
    int i;
    fp_out = fopen("decay_0,5.dat","w");
    for(i = 0 ; i < MAX; i++){
        fprintf(fp_out,"%g\t%g\n",t[i], nuclei[i]);
                             }
    fclose(fp_out);
    return(0);

}


int main(){

    initialize(n_uranium, t,&tau,&dt);
    calculate(n_uranium,t,tau,dt);
    store(n_uranium, t);
}
