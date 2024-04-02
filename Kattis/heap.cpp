#include "heap.h"

const int MAX_SIZE = 1000000; // Tamaño máximo del montículo
int heap[MAX_SIZE]; // Arreglo para almacenar el montículo
int heapSize = 0; // Tamaño actual del montículo


int getMax(){
    if (heapSize == 0) return -1;
    return heap[0];
}

int getSize(){
    return heapSize;
}

void insert(int element){
    if (heapSize == MAX_SIZE) return;
    
    heap[heapSize] = element;
    int currentIndex = heapSize; 
    heapSize++; 

    while (currentIndex > 0 && heap[currentIndex] > heap[(currentIndex - 1) / 2]) {
        int temp = heap[currentIndex];
        heap[currentIndex] = heap[(currentIndex - 1) / 2];
        heap[(currentIndex - 1) / 2] = temp;
        currentIndex = (currentIndex - 1) / 2; 
    }
}

void removeMax() {
    if (heapSize == 0) {
        return;
    }

    heapSize--;
    heap[0] = heap[heapSize];

    int currentIndex = 0;
    while (true) {
        int leftChildIndex = 2 * currentIndex + 1;
        int rightChildIndex = 2 * currentIndex + 2;
        int maxIndex = currentIndex;

        if (leftChildIndex < heapSize && heap[leftChildIndex] > heap[maxIndex]) {
            maxIndex = leftChildIndex;
        }
        if (rightChildIndex < heapSize && heap[rightChildIndex] > heap[maxIndex]) {
            maxIndex = rightChildIndex;
        }

        if (maxIndex == currentIndex) {
            break;
        }

        int temp = heap[currentIndex];
        heap[currentIndex] = heap[maxIndex];
        heap[maxIndex] = temp;
        currentIndex = maxIndex; 
    }
}