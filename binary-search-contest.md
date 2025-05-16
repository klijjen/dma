# 1.1

# 1.1

```cpp
void solve() {
    int n, x;
    cin >> n >> x;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int l = 0, r = n - 1;
    int res = -1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] >= x) {
            res = m;
            r = m - 1;
        }
        else {
            l = m + 1;
        }
    }
    cout << (res != -1 ? a[res] : -1) << endl;
    return;
}
```

![telegram-cloud-photo-size-2-5451848919823806461-y](https://github.com/user-attachments/assets/2f256efa-6d74-4054-bda0-3682b2bfec12)
