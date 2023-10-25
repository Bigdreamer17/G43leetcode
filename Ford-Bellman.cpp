#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = 30000;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<pair<int, int>>> graph(n + 1);
    
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
    }
    
    vector<int> dist(n + 1, INF);
    dist[1] = 0;
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 1});
    
    while (!pq.empty()) {
        int cur_dist = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        
        if (cur_dist > dist[u]) {
            continue;
        }
        
        for (auto edge : graph[u]) {
            int v = edge.first;
            int w = edge.second;
            
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    
    for (int i = 1; i <= n; i++) {
        cout << dist[i] << " ";
    }
    
    return 0;
}