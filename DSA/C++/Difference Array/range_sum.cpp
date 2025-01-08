#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int main() {
    int size, query;

    cout << "Enter size of the array: ";
    cin >> size;
    vector<int> nums(size, 0); // Initialize nums with 0

    cout << "Enter Values of the array: ";
    for (int i = 0; i < size; i++) {
        cin >> nums[i];
    }

    cout << "Enter number of queries: ";
    cin >> query;

    vector<tuple<int, int, int>> queries;
    int start, end, value;
    for (int q = 0; q < query; q++) {
        cout << "Start Index: ";
        cin >> start;
        cout << "End Index: ";
        cin >> end;
        cout << "Enter Value: ";
        cin >> value;

        // Push this tuple into the queries vector
        queries.push_back(make_tuple(start, end, value));
    }

    // Difference array logic
    for (const auto& t : queries) {
        start = get<0>(t);
        end = get<1>(t);
        value = get<2>(t);

        nums[start] += value;
        if (end + 1 < size) {
            nums[end + 1] -= value;
        }
    }

    // Cumulative sum calculation if impact needs to be calculated( Range addition)
    vector<int> prefixsum(size, 0);
    prefixsum[0] = nums[0];
    for (int c = 1; c < nums.size(); c++) {
        prefixsum[c] = prefixsum[c - 1] + nums[c];
    }

    // Print the resulting array
    cout << "Resulting Array: ";
    for (int num : prefixsum) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
