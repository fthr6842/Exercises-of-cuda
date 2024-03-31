#include <stdio.h>

__global__ void hello_from_gpu()
{
    printf("hello world form the GPU\n");
}

int main(void)
{
    hello_from_gpu<<<2, 4>>>(); //2個線程塊、每個線程塊有4個線程，共輸出8次
    cudaDeviceSynchronize();

    return 0;
}