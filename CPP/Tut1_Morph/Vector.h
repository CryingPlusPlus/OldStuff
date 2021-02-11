#ifndef VECTOR_H
#define VECTOR_H

class Vector {
    private:
        double x, y, z;

    public:
        static int dimension;
        Vector(double x, double y, double z);
        void printMe();
        Vector operator +(Vector &b);
};
#endif