#include <stdio.h>


void print_arr(int *arr)
{
	int i;

	for (i = 0; i < 5; i++)
		printf("%i\n", arr[i]);

}



int main(void)
{
	int arr[] = {1, 2, 3, 4, 5};


	print_arr(arr);

	return (0);



}
