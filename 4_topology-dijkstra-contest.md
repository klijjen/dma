# 4.1

```cpp
vector<vector<int>> g;
vector<bool> used;
vector<int> ans;

void dfs(int v) {
    used[v] = true;
    for (int x : g[v])
        if (!used[x])
            dfs (x);
    ans.push_back (v);
}

void solve() {
    int n;
    cin >> n;
    g.resize(n);
    used.resize(n, false);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int x;
            cin >> x;
            g[i].push_back(x - 1);
        }
    }
    for (int i = 0; i<n; ++i)
        if (!used[i]) dfs (i);
    reverse(ans.begin(), ans.end());
    if (ans.size() < n) cout << -1 << endl;
    else
        for (int x : ans) cout << x << " ";
}
```

![telegram-cloud-photo-size-2-5453888140231175605-y](https://github.com/user-attachments/assets/740e253b-166b-4990-a3e2-858921031bcc)

# 4.2

```cpp
void solve() {
    int n, a, b;
    cin >> n >> a >> b;
    a--;
    b--;
    vector<vector<pair<int, ll>>> g(n);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int v, w;
            cin >> v >> w;
            g[i].emplace_back(v - 1, w);
        }
    }
    vector<ll> d(n, INF);
    vector<int> p(n);
    d[a] = 0;
    vector<char> u(n);
    for (int i = 0; i < n; i++) {
        int v = -1;
        for (int j = 0; j < n; j++)
            if (!u[j] && (v == -1 || d[j] < d[v])) v = j;
        if (d[v] == INF) break;
        u[v] = true;
        for (int j = 0; j < g[v].size(); j++) {
            int to = g[v][j].first;
            ll len = g[v][j].second;
            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
            }
        }
    }
    vector<int> path;
    for (int v = b; v != a; v = p[v])
        path.push_back(v);
    path.push_back(a);
    reverse(path.begin(), path.end());
    if (d[b] != INF) {
        cout << d[b] << endl;
        for (int x : path)
            cout << x + 1 << ' ';
    }
    else 
        cout << -1;
}
```

![telegram-cloud-photo-size-2-5453888140231175607-y](https://github.com/user-attachments/assets/9eef9724-38ad-44fb-9ecd-4bdfdcbbebf9)
