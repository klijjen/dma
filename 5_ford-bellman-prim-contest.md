# 5.1 

```cpp
void solve() {
    int n, m, a, b;
    cin >> n >> m >> a >> b;
    vector<tuple<int, int, ll>> g;
    for (int i = 0; i < m; ++i) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        g.emplace_back(u, v, w);
    }
    vector<ll> d(n + 1, INF);
    vector<int> p(n + 1, -1);
    d[a] = 0;
    for (int i = 0; i < n - 1; i++) 
        for (auto [u, v, w] : g) 
            if (d[u] < INF && d[u] + w < d[v]) {
                d[v] = d[u] + w;
                p[v] = u;
            }
    for (auto [u, v, w] : g) 
        if (d[u] < INF && d[u] + w < d[v]) {
            cout << -1 << endl;
            return;
        }
    if (d[b] == INF || d[b] == -1) {
        cout << -1 << endl;
        return;
    }
    vector<int> ans;
    for (int v = b; v != -1; v = p[v]) 
        ans.push_back(v);
    reverse(ans.begin(), ans.end());
    cout << d[b] << endl;
    for (int v : ans) cout << v << ' ';
    cout << endl;
}
```

![telegram-cloud-photo-size-2-5453888140231175733-y](https://github.com/user-attachments/assets/bbd4a306-a236-46ed-9da8-aea3ee66d3a1)

# 5.2

```cpp
void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        g[u - 1][v - 1] = w;
        g[v - 1][u - 1] = w;
    }
    vector<bool> used(n, false);
    vector<int> mn(n, INF), l(n, -1);
    mn[0] = 0;
    vector<pair<int, int>> mst_g;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        int v = -1;
        for (int j = 0; j < n; ++j)
            if (!used[j] && (v == -1 || mn[j] < mn[v]))
                v = j;
        if (mn[v] == INF) {
            cout << -1 << endl;
            return;
        }
        used[v] = true;
        if (l[v] != -1) {
            int u = l[v];
            cnt += mn[v];
            mst_g.emplace_back(min(u, v) + 1, max(u, v) + 1);
        }
        for (int to = 0; to < n; ++to) {
            if (g[v][to] != 0 && !used[to] && g[v][to] < mn[to]) {
                mn[to] = g[v][to];
                l[to] = v;
            }
        }
    }
    cout << cnt << endl;
    sort(mst_g.begin(), mst_g.end());
    for (auto [u, v] : mst_g) {
        cout << u << " " << v << " ";
    }
}
```

![telegram-cloud-photo-size-2-5453888140231175833-y](https://github.com/user-attachments/assets/ecbc8f5e-00f9-435a-acc8-da897a1823f3)

