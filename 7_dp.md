![telegram-cloud-photo-size-2-5276393089101065723-y](https://github.com/user-attachments/assets/41d6f146-8e73-472c-aeea-3e684f0df920)

# 7.1

```cpp
void solve() {
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    vector<ll> d(n * 2, INF);
    d[0] = -INF;
    for (int i = 0; i < n; i++) {
        int j = int(upper_bound(d.begin(), d.end(), a[i]) - d.begin());
        if (d[j - 1] < a[i] && a[i] < d[j])
            d[j] = a[i];
        cout << d[i] << ' ';
    }
    int cnt = 0, ans = 0;
    for (int i = 1; i <= n; i++)
        if (d[i] < INF) {
            ans++;
        }
    cout << ans << endl;
}
```

# 7.2

```cpp
void solve() {
    int n;
    cin >> n;
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int k = 1; k <= n; k++) 
        for (int i = k; i <= n; i++) 
            dp[i] += dp[i - k];
    cout << dp[n] << endl;
}
```

# 7.3 

```cpp
void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) 
        cin >> a[i];
    vector<int> dp(n);
    dp[0] = a[0];
    dp[1] = a[0] + a[1];
    for (int i = 2; i < n; ++i) 
        dp[i] = a[i] + max(dp[i - 1], dp[i - 2]);
    cout << dp[n - 1] << endl;
}
```
