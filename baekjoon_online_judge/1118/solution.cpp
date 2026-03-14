#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Rect{ll x1,y1,x2,y2;};
struct Event{
    ll x,y1,y2;
    int v;
    bool operator<(const Event& o)const{return x<o.x;}
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll W,H;
    int K;
    cin>>W>>H>>K;

    vector<Rect> rects;

    for(int i=0;i<K;i++){
        ll f,c,x1,y1,x2,y2;
        cin>>f>>c>>x1>>y1>>x2>>y2;

        ll seg=H/(c+1);

        vector<pair<ll,ll>> xs;

        ll l=f-x2, r=f-x1;
        if(r>0 && l<W) xs.push_back({max(0LL,l),min(W,r)});

        l=f+x1, r=f+x2;
        if(r>0 && l<W) xs.push_back({max(0LL,l),min(W,r)});

        for(auto [lx,rx]:xs){
            if(lx>=rx) continue;

            for(int k=0;k<=c;k++){
                ll ly,ry;
                if(k%2==0){
                    ly=k*seg+y1;
                    ry=k*seg+y2;
                }else{
                    ly=(k+1)*seg-y2;
                    ry=(k+1)*seg-y1;
                }
                rects.push_back({lx,ly,rx,ry});
            }
        }
    }

    vector<Event> ev;
    vector<ll> ys;

    for(auto&r:rects){
        ev.push_back({r.x1,r.y1,r.y2,1});
        ev.push_back({r.x2,r.y1,r.y2,-1});
        ys.push_back(r.y1);
        ys.push_back(r.y2);
    }

    sort(ys.begin(),ys.end());
    ys.erase(unique(ys.begin(),ys.end()),ys.end());

    auto gety=[&](ll y){
        return lower_bound(ys.begin(),ys.end(),y)-ys.begin();
    };

    int m=ys.size();
    vector<int> cnt(m*4);
    vector<ll> len(m*4);

    function<void(int,int,int,int,int,int)> upd =
    [&](int node,int l,int r,int ql,int qr,int v){
        if(qr<=l||r<=ql) return;
        if(ql<=l&&r<=qr){
            cnt[node]+=v;
        }else{
            int mid=(l+r)/2;
            upd(node*2,l,mid,ql,qr,v);
            upd(node*2+1,mid,r,ql,qr,v);
        }

        if(cnt[node]) len[node]=ys[r]-ys[l];
        else{
            if(r-l==1) len[node]=0;
            else len[node]=len[node*2]+len[node*2+1];
        }
    };

    sort(ev.begin(),ev.end());

    ll prev=ev[0].x;
    ll area=0;

    for(auto&e:ev){
        ll dx=e.x-prev;
        area+=dx*len[1];
        upd(1,0,m-1,gety(e.y1),gety(e.y2),e.v);
        prev=e.x;
    }

    cout<<W*H-area<<"\n";
}