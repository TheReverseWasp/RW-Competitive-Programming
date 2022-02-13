#include <bits/stdc++.h>

using namespace std;

using vi = vector<int>;
using vvi = vector<vi>;
using mit = map<int, bool>;

long long count_ways(vvi vertices, vi colors, mit actual_colors, mit visited, int deep, int actual, bool inicio) {
  long long answer = 1;
  if(inicio) {
    answer = 0;
  }
  visited[actual] = true;
  actual_colors[colors[actual]] = true;
  if (deep == 1) {
    return answer;
  }
  for (size_t i = 0; i < vertices[actual].size(); i++) {
    int t = vertices[actual][i];
    int c = colors[t];
    if(visited.find(t) == visited.end() && actual_colors.find(c) == actual_colors.end()) {
      answer += count_ways(vertices, colors, actual_colors, visited, deep-1, t, false);
    }
  }
  return answer;
}

long long find_all_paths(vvi vertices, vi colors, int n, int c) {
  long long answer = 0;
  for (size_t i = 0; i < n; i++) {
    mit actual_colors, visited;
    answer += count_ways(vertices, colors, actual_colors, visited, c, i, true);
  }
  return answer;
}

int main(int argc, char const *argv[]) {
  int n, v, c;
  cin >> n >> v >> c;
  vi colors(n, 0);
  vvi vertices;
  for (size_t i = 0; i < n; i++) {
    cin >> colors[i];
    vi temp;
    vertices.push_back(temp);
  }
  for (size_t i = 0; i < v; i++) {
    int t1, t2;
    cin >> t1 >> t2;
    vertices[t1-1].push_back(t2-1);
    vertices[t2-1].push_back(t1-1);
  }
  cout << find_all_paths(vertices, colors, n, c) << endl;
  return 0;
}
