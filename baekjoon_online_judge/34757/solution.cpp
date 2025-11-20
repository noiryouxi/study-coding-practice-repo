#include <bits/stdc++.h>
using namespace std;

struct Seg {
    struct Node {
        long long sum, mn;
    };
    int n;
    vector<Node> t;
    Seg(int n):n(n),t(4*n){}

    Node merge(Node a, Node b){
        return {a.sum+b.sum, min(a.mn,b.mn)};
    }

    void build(int p,int l,int r,const vector<long long> &s){
        if(l==r){ t[p]={s[l],s[l]}; return; }
        int m=(l+r)/2;
        build(p*2,l,m,s);
        build(p*2+1,m+1,r,s);
        t[p]=merge(t[p*2],t[p*2+1]);
    }

    void update(int p,int l,int r,int i,long long v){
        if(l==r){ t[p]={v,v}; return; }
        int m=(l+r)/2;
        if(i<=m) update(p*2,l,m,i,v);
        else update(p*2+1,m+1,r,i,v);
        t[p]=merge(t[p*2],t[p*2+1]);
    }

    long long query_sum(int p,int l,int r,int ql,int qr){
        if(r<ql||qr<l) return 0;
        if(ql<=l&&r<=qr) return t[p].sum;
        int m=(l+r)/2;
        return query_sum(p*2,l,m,ql,qr)
             +query_sum(p*2+1,m+1,r,ql,qr);
    }

    // find first position ≥ L with remaining snow > 0
    int find_first(int p, int l, int r, int L){
        if(r < L || t[p].sum == 0) return -1;    // ← sum으로 판단 !!!
        if(l == r) return l;

        int m = (l + r) / 2;
        if(L <= m){
            int left = find_first(p*2, l, m, L);
            if(left != -1) return left;
            return find_first(p*2+1, m+1, r, L);
        } else {
            return find_first(p*2+1, m+1, r, L);
        }
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N,M,Q;
    cin>>N>>M>>Q;

    vector<long long> S(N+1);
    for(int i=1;i<=N;i++) cin>>S[i];

    vector<int> L(M+1), R(M+1);
    vector<long long> C(M+1);
    for(int t=1;t<=M;t++){
        cin>>L[t]>>R[t]>>C[t];
    }

    struct Query {int A,B; long long T; int idx;};
    vector<Query> qs(Q);
    for(int i=0;i<Q;i++){
        cin>>qs[i].A>>qs[i].B>>qs[i].T;
        qs[i].idx=i;
    }

    vector<long long> pref(N+1,0);
    for(int i=1;i<=N;i++) pref[i]=pref[i-1]+S[i];

    vector<int> lo(Q,1), hi(Q,M+1);
    vector<vector<int>> bucket(M+2);

    while(true){
        bool any=false;
        for(int t=1;t<=M+1;t++) bucket[t].clear();

        for(int i=0;i<Q;i++){
            if(lo[i]<hi[i]){
                any=true;
                int mid=(lo[i]+hi[i])/2;
                bucket[mid].push_back(i);
            }
        }
        if(!any) break;

        Seg seg(N);
        seg.build(1,1,N,S);

        int cur=0;
        for(int t=1;t<=M;t++){
            long long cap=C[t];
            int l=L[t], r=R[t];

            while(cap>0){
                int pos = seg.find_first(1,1,N,l);
                if(pos==-1 || pos>r) break;

                long long now = seg.query_sum(1,1,N,pos,pos);
                long long rm = min(now,cap);
                seg.update(1,1,N,pos,now-rm);
                cap -= rm;
            }

            for(int qi : bucket[t]){
                auto &q = qs[qi];
                long long init = pref[q.B] - pref[q.A-1];
                long long remain = seg.query_sum(1,1,N,q.A,q.B);
                long long removed = init - remain;

                if(removed >= q.T) hi[qi]=t;
                else lo[qi]=t+1;
            }
        }
    }

    vector<int> ans(Q);
    for(int i=0;i<Q;i++){
        ans[qs[i].idx] = (lo[i]==M+1 ? -1 : lo[i]);
    }

    for(int x: ans) cout<<x<<"\n";
}