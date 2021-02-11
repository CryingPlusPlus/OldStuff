#include <stdlib.h>
#include <iostream>
#include <vector>

using std::vector;

void fill ( vector<int> &output, vector<int> &a, int current_a, int size_a ) {
    for ( current_a; current_a < size_a; current_a++ ) {
        output.push_back(a[current_a]);
    }
}

vector<int> merge(vector<int> &a, vector<int> &b, int size_a, int size_b) {
    vector<int> output;
    int current_a = 0;
    int current_b = 0;

    while ( current_a < size_a && current_b < size_b ) {
        if ( a[current_a] < b[current_b] ) {
            output.push_back(a[current_a]);
            current_a++;
        } else {
            output.push_back(b[current_b]);
            current_b++;
        }
    }
    fill(output, b, current_b, size_b);
    fill(output, a, current_a, size_a);
    return output;
}

double findMedianSortedArrays( vector<int> &nums1, vector<int> &nums2 ) {
    double median = 0;
    nums1 = merge( nums1, nums2, nums1.size(), nums2.size() );

    for( int el : nums1 ) {
        std::cout << el << " ";
    }

    if( nums1.size() % 2 == 0 ) {
        median = (nums1[nums1.size() / 2] + nums1[nums1.size() / 2 + 1]) / 2.0;
    } else {
        median = nums1[nums1.size() / 2];
    }

    return median;
}

int main() {
    vector<int> nums1 = {1, 3, 5, 7, 9};
    vector<int> nums2 = {2, 4, 6, 8};

    double med = findMedianSortedArrays(nums1, nums2);

    return 0;
}