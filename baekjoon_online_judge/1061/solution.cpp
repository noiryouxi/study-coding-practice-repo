#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define sz size
#define pb push_back
#define pop pop_back
#define all(v) v.begin(),v.end()
#define bb(v) v.back(),v[v.size()-2]
struct pt {
    int y,x;
    bool operator==(pt a) {
        return x==a.x&&y==a.y;
    }
    bool operator!=(pt a){
        return x!=a.x||y!=a.y;
    }
    int operator/(pt a) {
        return x*a.y-y*a.x;
    }
    int ccw(pt b, pt c) {
        pt a = *this;
        return a/b+b/c+c/a;
    }
    int tri(pt b, pt c) {
        pt a = *this;
        return abs(a/b+b/c+c/a);
    }
    bool operator<(pt a) {
        return x<a.x||(x==a.x&&y<a.y);
    }
};
typedef vector<pt> pts;
pts r,g,b,R,G,B;

pts convex(pts p) {
    if (p.sz()<=1) return p;
    sort(all(p));

    pts h1;
    for (pt x:p) {
        while (h1.sz()>=2 && x.ccw(bb(h1))<0)
            h1.pop();
        h1.pb(x);
    }
    reverse(all(p));
    pts h2;
    for (pt x:p) {
        while (h2.sz()>=2 && x.ccw(bb(h2))<0)
            h2.pop();
        h2.pb(x);
    }
    for (pt x:h2) if (find(all(h1),x)==h1.end()) h1.pb(x);
    return h1;
}

pts furth(pt a, pt b, pts C) {
    pts c;
    int m = -1;
    for (pt x:C)
        if (x.tri(a,b)>m)
            m = x.tri(a,b);
    for (pt x:C)
        if (x.tri(a,b)==m)
            c.pb(x);
    return c;
}

int get() {
    int k = r.sz()*g.sz()*b.sz();
    if (!k) return k;
    R = convex(r);
    G = convex(g);
    B = convex(b);
    for (pt r:R)
        for (pt g:G)
            for (pt b:furth(r,g,B)) {
                pt fr = furth(g,b,R)[0];
                int a = b.tri(r,g);
                if (fr.tri(g,b)!=a) continue;
                pt fg = furth(b,r,G)[0];
                if (fg.tri(b,r)!=a) continue;
                k--;
            }
    return k;
}

int main() {
    int n,m;
    cin>>n>>m;
    char c;
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++) {
            cin>>c;
            if (c=='R') r.pb({i,j});
            if (c=='G') g.pb({i,j});
            if (c=='B') b.pb({i,j});
        }
    cout << get();
}