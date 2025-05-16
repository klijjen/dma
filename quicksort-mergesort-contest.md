# 2.1

```cpp
void quickSort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int p = a[(l + r) / 2];
    int i = l, j = r;
    while (i <= j) {
        while (a[i] < p) i++;
        while (a[j] > p) j--;
        if (i <= j) {
            swap(a[i], a[j]);
            i++;
            j--;
        }
    }
    quickSort(a, l, j);
    quickSort(a, i, r);
}

void solve () {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    quickSort(a, 0, n - 1);
    for (auto x : a) {
        cout << x << ' ';
    }
    return;
}
```

![telegram-cloud-photo-size-2-5451848919823806494-y](https://github.com/user-attachments/assets/a235b5ae-398c-4d3f-8c97-8f4e56635e0a)

# 2.2

```cpp
void merge(vector<int>& a, vector<int>& c, int l, int m, int r) {
    int i = l, j = m, k = l;
    while (i < m && j < r) {
        if (a[i] <= a[j]) {
            c[k] = a[i];
            i++;
            k++;
        }
        else {
            c[k] = a[j];
            j++;
            k++;
        }
    }
    while (i < m) {
        c[k] = a[i];
        i++;
        k++;
    }
    while (j < r) {
        c[k] = a[j];
        j++;
        k++;
    }
    for (int i = l; i < r; ++i) {
        a[i] = c[i];
    }
}

void mergeSort(vector<int>& a, vector<int>& c, int l, int r) {
    if (r - l <= 1) return;
    int m = (l + r) / 2;
    mergeSort(a, c, l, m);
    mergeSort(a, c, m, r);
    merge(a, c, l, m, r);
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(n), c(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    mergeSort(a, c, 0, n );
    for (auto x : a) {
        cout << x << ' ';
    }
}
```

![telegram-cloud-photo-size-2-5451848919823806499-y](https://github.com/user-attachments/assets/98bd0b7d-e885-4d40-8719-73d2d1bc895c)



