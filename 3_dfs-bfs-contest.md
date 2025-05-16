# 3.1

```cpp
void solve() {
    int n;
    cin >> n;
    vector<vector<int>> g(n);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int x;
            cin >> x;
            g[i].push_back(x - 1);
        }
    }
    queue<int> q;
    q.push(0);
    vector<bool> used(n);
    used[0] = true;
    while (!q.empty()) {
        int v = q.front();
        cout << v + 1 << ' ';
        q.pop();
        for (int i = 0; i < g[v].size(); i++) {
            int to = g[v][i];
            if (!used[to]) {
                used[to] = true;
                q.push(to);
            }
        }
    }
}
```

![telegram-cloud-photo-size-2-5451848919823806500-y](https://github.com/user-attachments/assets/1b825eba-b35d-4e01-81ba-c98b43cadc0a)

# 3.2

```cpp
vector<vector<int>> g;
vector<bool> used;

void dfs(int v) {
    cout << v + 1 << ' ';
    used[v] = true;
    for (int x : g[v])
        if (!used[x])
            dfs (x);
}

void solve() {
    int n;
    cin >> n;
    g.resize(n);
    used.resize(n);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int x;
            cin >> x;
            g[i].push_back(x - 1);
        }
    }
    dfs(0);
}
```

![telegram-cloud-photo-size-2-5451848919823806502-y](https://github.com/user-attachments/assets/e68c38cf-480e-4452-95c1-35568c3e5d54)

# 3.3

```cpp
vector<vector<int>> g;
vector<bool> used;

void dfs(int v) {
    used[v] = true;
    for (int x : g[v])
        if (!used[x]) dfs (x);
}

void solve() {
    int n;
    cin >> n;
    g.resize(n);
    used.resize(n);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int x;
            cin >> x;
            g[i].push_back(x - 1);
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (!used[i]) {
            dfs(i);
            ans++;
        }
    }
    cout << ans;
}

```
![telegram-cloud-photo-size-2-5451848919823806504-y](https://github.com/user-attachments/assets/a63a1ba6-7186-4039-a490-29e82438af66)

