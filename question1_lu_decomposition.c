#include <stdio.h>
#include <gsl/gsl_linalg.h>


int main()
{
    double data[] = {1.0, 0.67,0.33,0.45,1.0,0.55,0.67,0.33,1.0};
   

    gsl_matrix_view A = gsl_matrix_view_array(data, 3, 3); //matrix view of a of the given 3*3 data
   

    gsl_permutation *p = gsl_permutation_alloc(3); // memory allocation for storing the permutation matrix

    int sig,i,j,k;
    double L[3][3],U[3][3],mul_LU[3][3],old_A[3][3],mul_PA[3][3];
   
    for (i=0;i<3;i++)
    { for (j=0;j<3;j++)
     {
       old_A[i][j]=gsl_matrix_get(&A.matrix,i,j); //storing the actual A matrix 
     }
    }
    
    gsl_linalg_LU_decomp(&A.matrix,p, &sig); //LU decomposition using gsl function
 
    printf(" U matrix: \n");
    for (i=0;i<3;i++)
      {
	for (j=0;j<3;j++)
     {
     if (i<=j)
       {U[i][j]=gsl_matrix_get(&A.matrix,i,j); //accessing  the ij element of A matrix
       printf("%g  ",U[i][j]);}
     else
       {U[i][j]=0;
       printf("%g  ",U[i][j]);}
     }
     printf("\n\n");
      }
   
    printf(" L matrix: \n");
    for (i=0;i<3;i++)
    {for (j=0;j<3;j++)
     {
     if (i>j)
       {L[i][j]=gsl_matrix_get(&A.matrix,i,j);
       printf("%g  ",L[i][j]);}
     else if (i==j)
       {L[i][j]=1;
       printf("%g  ",L[i][j]);}
     else 
       {L[i][j]=0;
       printf("%g  ",L[i][j]);}
     }
     printf("\n\n");
    }
  
    printf(" LU matrix: \n");
    for (i=0;i<3;i++)
    {for (k=0;k<3;k++)
    {mul_LU[i][k]=0;
    for (j=0;j<3;j++)
      {
	mul_LU[i][k]=mul_LU[i][k]+L[i][j]*U[j][k];
      }
    printf("%g  ",mul_LU[i][k]);
    }
    printf("\n");}
   
    printf(" PA matrix \n");
    for (i=0;i<3;i++) //Applying permutation to A matrix i.e according to the p=(*,*,*) rows of A is swapped 
    {
    for (j=0;j<3;j++)
    {mul_PA[i][j]=old_A[gsl_permutation_get(p,i)][j];
    printf("%g  ",mul_PA[i][j]);
    }
    printf("\n");
    }
   
    gsl_permutation_free(p); //free the memory

    return 0;
}
