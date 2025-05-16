![telegram-cloud-photo-size-2-5276393089101065722-y](https://github.com/user-attachments/assets/880303ba-56b5-4b55-8709-456237d4251e)

# 6.1 

```cpp
void solve() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) 
        cin >> a[i];
    sort(a.begin(), a.end());
    int cnt = 0;
    for (int i = 0; i < n; i++) 
        if (k - a[i] >= 0) {
            k -= a[i];
            cnt++;
        }
    cout << cnt;
}
```

# 6.2

```cpp
void solve() {
    int n;
    cin >> n;
    vector<pair<int, int>> t(n);
    for (int i = 0; i < n; ++i) {
        cin >> t[i].first >> t[i].second;
    }
    sort(t.begin(), t.end());
    priority_queue<int, vector<int>, greater<>> s;
    for (const auto& x : t) {
        int f = x.first;
        int c = x.second;
        if (s.size() < f) s.push(c);
        else if (!s.empty() && s.top() < c) {
            s.pop();
            s.push(c);
        }
    }
    long long ss = 0;
    while (!s.empty()) {
        ss += s.top();
        s.pop();
    }
    cout << ss << endl;
}
```
