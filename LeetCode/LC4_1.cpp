#include <vector>
#include <iostream>

using std::vector;


struct Mean {
    int a[2];
    
    void append ( int &x ) {
        this -> a[0] = this -> a[1];
        this -> a[1] = x;
    } 
};

std::ostream& operator << (std::ostream &output, Mean &m) {
    output << m.a[0] << " " << m.a[1];
    return output;
}

class Solution {
    public:
        double findMedianSortedArraays( vector<int> &nums1, vector<int> &nums2 ) {
            Mean m;

            int ca = 0;
            int cb = 0;
            int l = (nums1.size() + nums2.size()) / 2;
            std::cout << l << std::endl;
            int i = 0;
            while ( i <= l and ca < nums1.size() and cb < nums2.size()) {
                i++;
                std::cout << m << std::endl;
                if ( nums1[ca] < nums2[cb] ) {
                    m.append(nums1[ca]);
                    ca++;
                } else {
                    m.append(nums2[cb]);
                    cb++;
                }
            }
            while ( i <= l ) {
                if (ca < nums1.size() ) {
                    m.append(nums1[ca]);
                    ca++;
                } else {
                    m.append(nums2[cb]);
                    cb++;
                }
                i++;
            }
            std::cout << m << std::endl;
            std::cout << l - i << std::endl;
            double median = ( nums1.size() + nums2.size() ) % 2 == 0 ? ( m.a[0] + m.a[1] ) / 2.0 : m.a[1];
            return median;
        }
};

int main() {
    Solution S;

    vector<int> nums1 = {1, 1, 3, 3};
    vector<int> nums2 = {1, 1, 3, 3};

    bool v1 = 2 == S.findMedianSortedArraays(nums1, nums2);

    vector<int> nums3 = {1, 2, 3, 4, 5};
    vector<int> nums4 = {6, 7, 8, 9, 10};

    bool v2 = 5.5 == S.findMedianSortedArraays(nums1, nums2);

    vector<int> nums5 = {1, 2, 3, 4, 5};
    vector<int> nums6 = {6, 7, 8, 9};

    bool v3 = 5 == S.findMedianSortedArraays(nums1, nums2);

    std::cout << v1 << " " << v2 << " " << v3 << std::endl;



}