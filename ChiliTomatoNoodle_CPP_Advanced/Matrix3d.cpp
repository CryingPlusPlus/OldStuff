#include <iostream>
#include <array>
#include <cmath>

template<class T>
class Vec3d
{
    public:
        std::array<T, 4> cells;
        constexpr Vec3d()
        {
            cells = {0, 0, 0, 0};
        }
        Vec3d(std::array<T, 3> in)
        {
            cells = {in[0], in[1], in[2], 1};
        }
        void print_self()
        {
            for(auto el : cells)
                std::cout << el << " ";
            std::cout << std::endl;
        }
};

template<class T>
class Matrix3d
{
    public:
        std::array<std::array<T, 4>, 4> cells;
        
        constexpr Matrix3d()
        {
            cells = {
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0
            };
        }
        Matrix3d(std::array<std::array<T, 4>, 4> in)
        {
            cells = in;
        }

        ~Matrix3d(){}

        constexpr static Matrix3d<T> IDENTITY()
        {
            return Matrix3d<T>{{
                1, 0, 0, 0, 
                0, 1, 0, 0,
                0, 0, 1, 0,
                0, 0, 0, 1
            }};
        }
        static Matrix3d<T> X_ROTATION(const double theta)
        {
           const T cos_t = std::cos(theta);
           const T sin_t = std::sin(theta);

           Matrix3d<float> end = Matrix3d<float>::IDENTITY();
           end.cells[1][0] = cos_t;
           end.cells[1][1] = sin_t;
           end.cells[2][0] = -sin_t;
           end.cells[2][1] = cos_t;
           return end;
        }

        static Matrix3d<T> Y_ROTATION(const double theta)
        {
           const T cos_t = std::cos(theta);
           const T sin_t = std::sin(theta);

           Matrix3d<float> end = Matrix3d<float>::IDENTITY();
           end.cells[0][0] = -sin_t;
           end.cells[0][1] = cos_t;
           end.cells[2][0] = cos_t;
           end.cells[2][1] = sin_t;
           return end;
        }

        static Matrix3d<T> Z_ROTATION(const double theta)
        {
           const T cos_t = std::cos(theta);
           const T sin_t = std::sin(theta);

           Matrix3d<float> end = Matrix3d<float>::IDENTITY();
           end.cells[0][0] = cos_t;
           end.cells[0][1] = sin_t;
           end.cells[1][0] = -sin_t;
           end.cells[1][1] = cos_t;
           return end;
        }
        
        void print_self()
        {
            for(auto arr : cells)
            {
                for(auto el : arr)
                    std::cout << el << " ";
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }

        Vec3d<T> operator * (Vec3d<T> rhs)
        {
            Vec3d<T> end;
            for(int r = 0; r < 4; r++)
            {
                for(int c = 0; c < 4; c++)
                    end.cells[r] += cells[r][c] * rhs.cells[c];
            }
            return end;
        }

        Matrix3d<T> operator * (Matrix3d<T> rhs)
        {
            Matrix3d<T> end;
            for(int r = 0; r < 4; r++)
            {
                for(int x = 0; x < 4; x++)
                {
                    for(int c = 0; c < 4; c++)
                        end.cells[r][x] += cells[r][c] * rhs.cells[c][x];
                }
            }
            return end;
        }

        static Matrix3d<T> TRANSLATION(std::array<T, 3> t)
        {
            Matrix3d<T> end = Matrix3d<T>::IDENTITY();
            for(int i = 0; i < 2; i++)
                end.cells[i][3] = t[i];
            return end;
        }

        static Matrix3d<T> SCALING(std::array<T, 3> F)
        {
            Matrix3d<T> end = Matrix3d<T>::IDENTITY();
            for(int i = 0; i < 3; i++)
                end.cells[i][i] = F[i];
            return end;
        }

        static Matrix3d<T> SCALING(T f)
        {
            Matrix3d<T> end = Matrix3d<T>::IDENTITY();
            for(int i = 0; i < 3; i++)
                end.cells[i][i] = f;
            return end;
        }
};

int main()
{
    return 0;
}
