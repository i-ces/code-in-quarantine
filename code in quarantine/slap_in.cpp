#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        double x[n], y[n];
        for (int i = 0; i < n; i++)
        {
            cin >> x[i];
            x[i] = log(x[i]) / (1.0 * x[i]);
        }
        for (int i = 0; i < n; i++)
        {
            cin >> y[i];
            y[i] = log(y[i]) / (y[i] * (1.0));
        }
        sort(x, x + n);
        sort(y, y + n);
        double res = 0;

        int i = 0, j = 0;
        while (i < n)
        {
            while (x[i] > y[j] && j < n)
            {

                j++;
            }
            res += (j);
            i++;
        }
        printf("%lf\n", res / (double)n);
    }
    return 0;
}