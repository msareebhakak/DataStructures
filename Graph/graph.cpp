/*
# Author: Sareeb Hakak
# Purpose: Weighted Adjacency Matrix and List for Graph
# Date: 05 March 24
*/

#include <vector>
#include <iostream>
using namespace std;


vector<vector<int>> create_adjacencyMatrix ()
 { // adjacency matrix
    int n = 4;
    vector<vector<int>> adjacencyMatrix(n, vector<int>(n, 0)); // initialize with zeros

    for (int i=0; i<adjacencyMatrix.size(); i++)
    {
        for (int j=0; j<adjacencyMatrix[0].size(); j++)
        {
            cout << adjacencyMatrix[i][j] << " ";
        }
        cout << endl;

        return adjacencyMatrix;
    }

    // add edges using a loop over a vector of (source, target) pairs
    vector<pair<int, int>> edges {{0, 1}, {1, 0}, {1, 2}, {1, 3}, {2, 0}, {2, 3}};
    for (vector<pair<int, int>>::iterator i = edges.begin(); i != edges.end(); i++) {
        int u = i->first;
        int v = i->second;
        adjacencyMatrix[u][v] = 1;
    }
    cout << "Edge from 0 to 1: " << adjacencyMatrix[0][1] << endl;
    cout << "No edge from 0 to 3: " << adjacencyMatrix[0][3] << endl;
}


vector<vector<int>> create_adjacencyList ()
{ // adjacency list
    int n = 4;
    vector<vector<int>> adjacencyList(n); // create empty adjacency list

    // add edges using a loop over a vector of (source, target) pairs
    vector<pair<int, int>> edges {{0, 1}, {1, 0}, {1, 2}, {1, 3}, {2, 0}, {2, 3}};
    for (auto [u, v] : edges) {
        adjacencyList[u].push_back(v);
    }

    cout << "Neighbors of node 1:";
    for (size_t i = 0; i < adjacencyList[1].size(); i++) {
        std::cout << " " << adjacencyList[1][i];
    }
    cout << endl;

    return adjacencyList;
}


vector<vector<int>> adjacencyMatrixToList(vector<vector<int>> adjacencyMatrix) {
    int n = adjacencyMatrix.size();
    vector<vector<int>> adjacencyList(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (adjacencyMatrix[i][j]) {
                adjacencyList[i].push_back(j);
            }
        }
    }
    return adjacencyList;
}


vector<vector<int>> adjacencyListToMatrix(vector<vector<int>> adjacencyList) {
    int n = adjacencyList.size();
    vector<vector<int>> adjacencyMatrix(n, vector<int>(n, 0));

    for (auto i = 0; i <n; i++)
    {
        for (auto it = adjacencyList[i].begin();  it < adjacencyList[i].end(); it++)
        {
            int j = *it;
            adjacencyMatrix[i][j] = 1;
        }
    }

    return adjacencyMatrix;
}