#include <stdio.h>

#define SIZE 4

// Matriz de int: filas = productos, columnas = dias

void inicializarTabla(int tabla[SIZE][SIZE]) {
    for (int p = 0; p < SIZE; p++) {
        for (int d = 0; d < SIZE; d++) {
            tabla[p][d] = 0;
        }
    }
}

void pedirVentas(int tabla[SIZE][SIZE]) {
    for (int p = 0; p < SIZE; p++) {
        for (int d = 0; d < SIZE; d++) {
            printf("Ventas del producto %d en el dia %d: ", p + 1, d + 1);
            scanf("%d", &tabla[p][d]);
        }
    }
}

void mostrarTabla(int tabla[SIZE][SIZE]) {
    printf("\n            ");
    for (int d = 0; d < SIZE; d++) {
        printf("Dia %d  ", d + 1);
    }
    printf("\n");
    for (int p = 0; p < SIZE; p++) {
        printf("Producto %d  ", p + 1);
        for (int d = 0; d < SIZE; d++) {
            printf("%5d  ", tabla[p][d]);
        }
        printf("\n");
    }
}

int main() {
    int tabla[SIZE][SIZE];
    int totalGeneral = 0;

    printf("===== Tienda: registro de ventas =====\n");

    inicializarTabla(tabla);
    pedirVentas(tabla);
    mostrarTabla(tabla);

    printf("\n--- Total por producto ---\n");
    for (int p = 0; p < SIZE; p++) {
        int totalProducto = 0;
        for (int d = 0; d < SIZE; d++) {
            totalProducto += tabla[p][d];
        }
        printf("Producto %d: %d\n", p + 1, totalProducto);
        totalGeneral += totalProducto;
    }

    printf("\nTotal de ventas de todos los productos: %d\n", totalGeneral);

    return 0;
}
