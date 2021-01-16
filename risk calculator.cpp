#include <bits/stdc++.h>


#define MOD 1000000007
#define int long long int
using namespace std;

int xx = 5;

int32_t main() {
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  map < pair < string, string > , int > m_normal;
  map < pair < string, string > , int > m_malicious;
  int t;
  cin >> t;

  while (t--) {

    int n;
    cin >> n;
    vector < pair < string, string > > v(n);

    for (int i = 0; i < n; i++) {

      string s;
      cin >> s;
      int nn = s.size() - 1;
      string ans;

      while (nn >= 0 && s[nn] != '.') {
        ans += s[nn];
        nn--;
      }

      string temp;
      for (int j = ans.size() - 1; j >= 0; j--) {
        temp += ans[j];

      }

      v[i].first = temp;
    }
    for (int i = 0; i < n; i++) {
      cin >> v[i].second;

    }
    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {

        if (v[i].second == "dangerous" && v[j].second == "dangerous") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 6;
          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 6;
          }
        } else if (v[i].second == "normal" && v[j].second == "normal") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 2;
          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 2;
          }
        } else if (v[i].second == "signature" && v[j].second == "signature") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 4;
          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 4;
          }
        } else if (v[i].second == "normal" && v[j].second == "signature") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 3;
          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 3;
          }
        } else if (v[i].second == "normal" && v[j].second == "dangerous") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 4;
          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 4;
          }

        } else if (v[i].second == "signature" && v[j].second == "normal") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 3;
          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 3;
          }
        } else if (v[i].second == "signature" && v[j].second == "dangerous") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 5;

          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 5;

          }

        } else if (v[i].second == "dangerous" && v[j].second == "normal") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 4;

          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 4;

          }

        } else if (v[i].second == "dangerous" && v[j].second == "signature") {
          if (m_normal.find(make_pair(v[i].first, v[j].first)) == m_normal.end()) {
            m_normal[make_pair(v[i].first, v[j].first)] = 5;

          } else {
            m_normal[make_pair(v[i].first, v[j].first)] += 5;

          }

        }
      }
    }
  }
  cin >> t;
  while (t--) {

    int n;
    cin >> n;
    vector < pair < string, string > > v(n);

    for (int i = 0; i < n; i++) {

      string s;
      cin >> s;
      int nn = s.size() - 1;
      string ans;

      while (nn >= 0 && s[nn] != '.') {
        ans += s[nn];
        nn--;

      }

      string temp;
      for (int j = ans.size() - 1; j >= 0; j--) {
        temp += ans[j];

      }

      v[i].first = temp;

    }
    for (int i = 0; i < n; i++) {
      cin >> v[i].second;

    }
    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {

        if (v[i].second == "dangerous" && v[j].second == "dangerous") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 6;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 6;

          }

        } else if (v[i].second == "normal" && v[j].second == "normal") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 2;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 2;

          }

        } else if (v[i].second == "signature" && v[j].second == "signature") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 4;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 4;

          }

        } else if (v[i].second == "normal" && v[j].second == "signature") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 3;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 3;

          }

        } else if (v[i].second == "normal" && v[j].second == "dangerous") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 4;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 4;

          }

        } else if (v[i].second == "signature" && v[j].second == "normal") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 3;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 3;

          }

        } else if (v[i].second == "signature" && v[j].second == "dangerous") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 5;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 5;

          }

        } else if (v[i].second == "dangerous" && v[j].second == "normal") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 4;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 4;

          }

        } else if (v[i].second == "dangerous" && v[j].second == "signature") {
          if (m_malicious.find(make_pair(v[i].first, v[j].first)) == m_malicious.end()) {
            m_malicious[make_pair(v[i].first, v[j].first)] = 5;

          } else {
            m_malicious[make_pair(v[i].first, v[j].first)] += 5;

          }

        }

      }
    }

  }
  cin >> t;
  //cout << t << endl;
  while (t--) {
    int n;
    cin >> n;
    //cout << n << endl;
    vector < pair < string, string > > v(n);

    for (int i = 0; i < n; i++) {

      string s;
      cin >> s;
      int nn = s.size() - 1;
      string ans;

      while (nn >= 0 && s[nn] != '.') {
        ans += s[nn];
        nn--;

      }

      string temp;
      for (int j = ans.size() - 1; j >= 0; j--) {
        temp += ans[j];

      }

      v[i].first = temp;

    }
    for (int i = 0; i < n; i++) {
      cin >> v[i].second;

    }

    int Normal_score = 0;
    int Malicious_score = 0;

    sort(v.begin(), v.end());
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        Normal_score += m_normal[make_pair(v[i].first, v[j].first)];
        Malicious_score += m_malicious[make_pair(v[i].first, v[j].first)];
      }
    }
    if (Malicious_score > (5 * (Normal_score)) / 2) {
      cout << "High Risk" << endl;

    } else if (Malicious_score > (3 * (Normal_score)) / 2) {
      cout << "Moderate Risk" << endl;

    } else if (Malicious_score > Normal_score) {
      cout << "Low risk" << endl;

    } else {
      cout << "Safe" << endl;
    }
    cout << "Normal score:"<< Normal_score << ", Malicious score:" << Malicious_score << endl;
  }
  return 0;
}
