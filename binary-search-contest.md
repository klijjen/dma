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

# 1.2

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
    if (res != 0)
        cout << (abs(a[res] - x) < abs(a[res - 1] - x) ? res : res - 1) << endl;
    else
        cout << res;
    return;
}
```

![telegram-cloud-photo-size-2-5451848919823806472-y](https://github.com/user-attachments/assets/06239bd2-b0ab-4314-9c76-f8a1e9c0b40d)

# 1.3 

```cpp
void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int l = 0, r = n - 1;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < a[m + 1]) {
            l = m + 1;
        }
        else {
            r = m;
        }
    }

    cout << l << endl;
    return;
}
```

![telegram-cloud-photo-size-2-5451848919823806475-y](https://github.com/user-attachments/assets/584fd4e0-5aed-48bb-b7a8-248491d6a042)



