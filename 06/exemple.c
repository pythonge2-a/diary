
#if 0 
double divide(double a, double b) {
    if (b == 0) {
        return 0;
    }
    return a / b;
}
#elif 2 
bool divide(double a, double b, double *c) {
    if (b == 0) {
        return 1;
    }
    *c = a / b;
    return 0;
}
#elif 1
double divide(double a, double b) {
    if (b == 0) {
        raise ZeroDivide; // VILAIN !!!
    }
    return a / b;
}
#endif