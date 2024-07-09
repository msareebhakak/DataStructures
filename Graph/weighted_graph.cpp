/*
# Author: Sareeb Hakak
# Purpose: Adjacency Matrix and List for Graph
# Date: 05 March 24
*/

#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

vector<vector<int>> create_adjacencyMatrix ()
{ //weighted adjacency matrix
    int n = 4;
    vector<vector<int> > adjacencyMatrix(n, vector<int>(n, 0)); // unweighted adjacency matrix
    vector<vector<int> > weightMatrix(n, vector<int>(n, 0)); // integer weight matrix

    // add edges using a loop over a vector of (source, target, weight) tuples
    vector<tuple<int, int, int> > edges;
    edges.push_back(make_tuple(0, 1, -2));
    edges.push_back(make_tuple(1, 0, 3));
    edges.push_back(make_tuple(1, 2, 0));
    edges.push_back(make_tuple(1, 3, 0));
    edges.push_back(make_tuple(2, 0, -6));
    edges.push_back(make_tuple(2, 3, 4));

    for (vector<tuple<int, int, int> >::iterator it = edges.begin(); it != edges.end(); ++it) {
        int v = get<0>(*it);
        int u = get<1>(*it);
        int w = get<2>(*it);
        adjacencyMatrix[u][v] = 1;
        weightMatrix[u][v] = w;
    }

    cout << "Edge from 1 to 2: adjacency " << adjacencyMatrix[1][2] << ", weight " << weightMatrix[1][2] << endl;
    cout << "No edge from 0 to 3: adjacency " << adjacencyMatrix[0][3] << endl;

    return adjacencyMatrix;
}


vector<vector<pair<int, int>>> create_adjacencyList ()
{ // weighted adjacency list
    int n = 4;
    vector<vector<pair<int, int>>> adjacencyList(n); // create empty adjacency list

    // add edges using a loop over a vector of (source, target, weight) tuples
    vector<tuple<int, int, int>> edges {
        make_tuple(0, 1, 5),
        make_tuple(1, 0, 3),
        make_tuple(1, 2, 7),
        make_tuple(1, 3, 4),
        make_tuple(2, 0, 11),
        make_tuple(2, 3, 4)
    };
    for (vector<tuple<int, int, int>>::iterator i = edges.begin(); i < edges.end(); i++) {
        auto u = get<0>(*i);
        auto v = get<1>(*i);
        auto w = get<2>(*i);
        adjacencyList[u].push_back({v, w});
    }
    cout << "Neighbors of node 1:";
    for (int i = 0; i < adjacencyList[1].size(); ++i) {
        auto [u, w] = adjacencyList[1][i];
        cout << " " << u << " (weight " << w << ")";
        if (i < adjacencyList[1].size() - 1) {
            cout << ",";
        }
    }
    cout << endl;

    return adjacencyList;
}
